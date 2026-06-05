#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path('.').resolve()

SECTION = {
    'counts': 'COUNTS',
    'stale': 'STALE',
    'crossrefs': 'CROSS_REFS',
    'sizes': 'SIZES',
    'prices': 'PRICES',
    'summary': 'SUMMARY',
    'all': 'ALL',
}

STALE_PATTERNS = [
    ("Gs 1.5M/1,5M (stale threshold)", re.compile(r'Gs\s*1[,.]5M')),
    ("~135 files (stale count)", re.compile(r'~135\s+(files|documents)')),
    ("~138 files (stale count)", re.compile(r'~138\s+(files|documents)')),
    ("~181 files (stale count)", re.compile(r'~181\s+(files|documents)')),
    ("165+ .md files (stale count)", re.compile(r'165\+\s*\.md\s+files')),
    ("168 documents", re.compile(r'168\s+documents')),
    ("173 docs (stale count)", re.compile(r'173\s+docs')),
]

CROSSREF_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
SKIP_RE = re.compile(r'(`[^`]*\[[^\]]+\]\([^)]+\)[^`]*`)')

PRICE_BLOCK_RE = re.compile(r'PRICING CROSS-REFERENCE', re.IGNORECASE)


def md_files(exclude_dirs=('ARCHIVE', '.git', 'node_modules', '.venv', 'meal-prerp-website')):
    for p in ROOT.rglob('*.md'):
        if not any(d in p.parts for d in exclude_dirs):
            yield p


def cmd_counts(args=None):
    all_md_files = [
        p for p in ROOT.rglob('*.md')
        if not any(d in p.parts for d in ('.git', 'node_modules', '.venv', 'meal-prerp-website'))
    ]

    by_folder = Counter()
    for p in all_md_files:
        rel = p.relative_to(ROOT)
        top = rel.parts[0] if rel.parts else 'ROOT'
        by_folder[top] += 1

    print('Per-folder .md counts (recursive):')
    for k in sorted(by_folder):
        print(f'  {k}: {by_folder[k]}')
    total = sum(by_folder.values())
    print(f'TOTAL (sum of categorized files): {total}')
    print(f'TOTAL (overall rglob for verification): {len(all_md_files)}')


def cmd_stale(args=None):
    hits = 0
    for p in md_files():
        text = p.read_text(errors='ignore')
        for label, pat in STALE_PATTERNS:
            if pat.search(text):
                print(f'{p.relative_to(ROOT)}: [{label}]')
                hits += 1
                break
    if hits == 0:
        print('No stale hits found.')


def cmd_crossrefs(args=None):
    broken = []
    for p in md_files():
        text = p.read_text(errors='ignore')
        clean_text = SKIP_RE.sub('', text)
        for m in CROSSREF_RE.finditer(clean_text):
            target = m.group(1)
            if target.startswith('#') or '://' in target or target.startswith('mailto:'):
                continue
            target_path = (p.parent / target).resolve()
            target_path = target_path.with_name(target_path.name.split('#')[0])
            if not target_path.exists():
                try:
                    missing_str = str(target_path.relative_to(ROOT))
                except ValueError:
                    missing_str = str(target_path)
                broken.append((str(p.relative_to(ROOT)), target, missing_str))
    if broken:
        print('Broken intra-repo links:')
        for src, tgt, path in broken:
            print(f'  {src} => {tgt}  (missing: {path})')
    else:
        print('All checked intra-repo links resolve.')


def cmd_prices(args=None):
    missing = []
    for p in md_files():
        text = p.read_text(errors='ignore')
        if re.search(r'PRICING CROSS-REFERENCE', text, re.IGNORECASE):
            continue
        if re.search(r'price|pricing|Gs\s*\d', text, re.IGNORECASE):
            missing.append(str(p.relative_to(ROOT)))
    if missing:
        print('Priced docs missing canonical pricing block:')
        for f in sorted(missing):
            print(f'  {f}')
    else:
        print('All priced docs have canonical pricing block.')


def cmd_sizes(args=None):
    rows = []
    for p in md_files():
        rows.append((p.stat().st_size, str(p.relative_to(ROOT))))
    for sz, p in sorted(rows, reverse=True)[:25]:
        print(f'{sz:>10}  {p}')


def cmd_summary(args=None):
    cmd_counts(args)
    print('\n---')
    cmd_stale(args)
    print('\n---')
    cmd_crossrefs(args)
    print('\n---')
    cmd_prices(args)


def cmd_all(args=None):
    cmd_summary(args)
    print('\n---')
    cmd_sizes(args)


def usage():
    print('Usage: repo-audit.py [' + '|'.join(SECTION) + ']')
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if not args:
        cmd_all(args)
        return
    name = args[0]
    if name not in SECTION:
        usage()
    dispatch = {
        'counts': cmd_counts,
        'stale': cmd_stale,
        'crossrefs': cmd_crossrefs,
        'sizes': cmd_sizes,
        'prices': cmd_prices,
        'summary': cmd_summary,
        'all': cmd_all,
    }
    dispatch[name](args)


if __name__ == '__main__':
    main()
