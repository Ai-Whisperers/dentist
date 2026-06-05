#!/usr/bin/env python3
"""Validate intra-repo markdown links and clean stale values."""
import re
import sys
from pathlib import Path

ROOT = Path('.').resolve()

LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
SKIP_RE = re.compile(r'(`[^`]*\[[^\]]+\]\([^)]+\)[^`]*`)')

STALE = [
    ("Gs 1.5M threshold", re.compile(r'Gs 1[.,]5M')),
    ("~135 files", re.compile(r'~135\s+(files|documents)')),
    ("~138 files", re.compile(r'~138\s+(files|documents)')),
    ("~181 files", re.compile(r'~181\s+(files|documents)')),
    ("165+ files", re.compile(r'165\+?\s+(files|documents?|archivos)')),
]

EXCLUDE_DIRS = {'ARCHIVE', '.git', 'node_modules', '.venv', 'swarm', 'opencode'}


def md_files():
    for p in ROOT.rglob('*.md'):
        if not any(d in p.parts for d in EXCLUDE_DIRS):
            if p.name not in {'REPO-WORK-PLAN.md', 'TODO.md', 'COMPLETE-INDEX.md'}:
                yield p


def cmd_links(_=None):
    broken = []
    for p in md_files():
        text = p.read_text(errors='ignore')
        clean = SKIP_RE.sub('', text)
        for m in LINK_RE.finditer(clean):
            target = m.group(1)
            if target.startswith('#') or '://' in target or target.startswith('mailto:'):
                continue
            tp = (p.parent / target).with_name((p.parent / target).name.split('#')[0])
            if not tp.exists():
                try:
                    rel = str(tp.relative_to(ROOT))
                except ValueError:
                    rel = str(tp)
                broken.append((str(p.relative_to(ROOT)), target, rel))
    if broken:
        print('Broken intra-repo links:')
        for src, tgt, path in broken:
            print(f'  {src} => {tgt}  (missing: {path})')
        return 1
    print('All checked intra-repo links resolve.')
    return 0


def cmd_stale(_=None):
    hits = 0
    for p in md_files():
        if p.name in {'REPO-WORK-PLAN.md', 'TODO.md', 'COMPLETE-INDEX.md'}:
            continue
        text = p.read_text(errors='ignore')
        for label, pat in STALE:
            if pat.search(text):
                print(f'{p}: [{label}]')
                hits += 1
    if hits == 0:
        print('No stale hits found.')
    else:
        return 1
    return 0


def cmd_prices(_=None):
    """Cross-check pricing docs have the canonical top-of-file block."""
    canonical = '00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md'
    block = re.compile(r'00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2\.md', re.I)
    priced_dirs = [
        Path('00_STRATEGIC/financial-pricing'),
        Path('04_SALES'),
        Path('03_LAUNCH/corporate-sales/programs'),
        Path('03_LAUNCH/corporate-sales/clubs'),
    ]
    files = []
    for d in priced_dirs:
        rp = ROOT / d
        if not rp.exists():
            continue
        for f in rp.glob('*.md'):
            files.append(f)
    missing = []
    for f in files:
        text = f.read_text(errors='ignore')
        if not block.search(text):
            missing.append(str(f.relative_to(ROOT)))
    if missing:
        print('Docs missing canonical pricing block:')
        for m in missing:
            print(f'  {m}')
        return 1
    print('All priced docs have canonical pricing block.')
    return 0


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in {'links', 'stale', 'prices', 'all'}:
        print('Usage: validate-refs.py [links|stale|prices|all]')
        sys.exit(2)
    cmd = sys.argv[1]
    rc = 0
    if cmd in {'links', 'all'}:
        rc |= cmd_links()
    if cmd in {'stale', 'all'}:
        rc |= cmd_stale()
    if cmd in {'prices', 'all'}:
        rc |= cmd_prices()
    sys.exit(rc)


if __name__ == '__main__':
    main()
