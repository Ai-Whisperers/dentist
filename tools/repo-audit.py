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
    'summary': 'SUMMARY',
}

STALE_PATTERNS = [
    # Original estimates or values that are now canonicalized to 3M or actual counts
    ("Gs 1.5M/1,5M (stale threshold)", re.compile(r'Gs 1[.,]5M')),
    ("~135 files (stale count)", re.compile(r'~135\s+(files|documents)')),
    ("~138 files (stale count)", re.compile(r'~138\s+(files|documents)')),
    ("~181 files (stale count)", re.compile(r'~181\s+(files|documents)')),
]

CROSSREF_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')

# Patterns to skip (inline code, code fences, images)
SKIP_RE = re.compile(r'(`[^`]*\[[^\]]+\]\([^)]+\)[^`]*`)')

def md_files(exclude_dirs=('ARCHIVE', '.git', 'node_modules', '.venv')):
    for p in ROOT.rglob('*.md'):
        if not any(d in p.parts for d in exclude_dirs):
            yield p

def cmd_counts(args=None):
    by_folder = Counter()
    # Count all .md files in the entire repository, then categorize by top-level folder
    all_md_files = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'node_modules' not in p.parts and '.venv' not in p.parts]
    
    for p in all_md_files:
        # Determine the top-level directory or if it's a root-level file
        if p.is_relative_to(ROOT):
            # Take the first part of the relative path, which is the top-level dir/file
            relative_path_parts = p.relative_to(ROOT).parts
            if len(relative_path_parts) > 0 and relative_path_parts[0] != '.':
                top_level_folder = relative_path_parts[0]
            else:
                top_level_folder = 'ROOT_LEVEL_MISC' # For .md files directly in root (excluding known meta files)
        else:
            # Files outside ROOT, should not happen with rglob(ROOT) but for safety
            top_level_folder = 'EXTERNAL'
            
        by_folder[top_level_folder] += 1

    print('Per-folder .md counts (recursive):')
    for k in sorted(by_folder):
        print(f'  {k}: {by_folder[k]}')
    
    total_sum_of_folders = sum(by_folder.values())
    actual_overall_total = len(all_md_files)

    print(f'TOTAL (sum of categorized files): {total_sum_of_folders}')
    print(f'TOTAL (overall rglob for verification): {actual_overall_total}')


def cmd_stale(args=None):
    hits = 0
    for p in md_files():
        if 'REPO-WORK-PLAN' in str(p) or 'REPO-ROAST' in str(p) or 'AGENTS.md' in str(p) or 'CLAUDE.md' in str(p): # Exclude meta files for stale check
            continue
        text = p.read_text(errors='ignore')
        for label, pat in STALE_PATTERNS:
            if pat.search(text):
                print(f'{p}: [{label}]')
                hits += 1
    if hits == 0:
        print('No stale hits found in active tree.')

def cmd_crossrefs(args=None):
    broken = []
    for p in md_files():
        text = p.read_text(errors='ignore')
        # Remove inline code snippets to avoid false positives like `[text](path)`
        clean_text = SKIP_RE.sub('', text)
        for m in CROSSREF_RE.finditer(clean_text):
            target = m.group(1)
            # Skip external links, anchor links, and mailto
            if target.startswith('#') or '://' in target or target.startswith('mailto:'):
                continue
            
            # Resolve path relative to the current markdown file
            target_path = (p.parent / target)
            
            # Remove any anchor links from the target_path for existence check
            # Example: path/to/file.md#anchor -> path/to/file.md
            target_path_no_anchor = target_path.with_name(target_path.name.split('#')[0])

            if not target_path_no_anchor.exists():
                try:
                    missing_path_str = str(target_path_no_anchor.relative_to(ROOT))
                except ValueError: # Path is not a subpath of ROOT, so just report the absolute path
                    missing_path_str = str(target_path_no_anchor)
                broken.append((str(p.relative_to(ROOT)), target, missing_path_str))

    if broken:
        print('Broken intra-repo links:')
        for src, tgt, path in broken:
            print(f'  {src} => {tgt}  (missing: {path})')
    else:
        print('All checked intra-repo links resolve.')

def cmd_sizes(args=None):
    rows = []
    for p in md_files():
        sz = p.stat().st_size
        rows.append((sz, str(p.relative_to(ROOT))))
    for sz, p in sorted(rows, reverse=True)[:25]:
        print(f'{sz:>10}  {p}')

def cmd_summary(args=None):
    cmd_counts(args)
    print('\n---')
    cmd_stale(args)
    print('\n---')
    cmd_crossrefs(args)

def usage():
    print('Usage: repo-audit.py [' + '|'.join(SECTION) + ']')
    sys.exit(1)

def main():
    args = sys.argv[1:]
    if not args:
        cmd_summary(args)
        return
    name = args[0]
    if name not in SECTION:
        usage()
    {'counts': cmd_counts, 'stale': cmd_stale, 'crossrefs': cmd_crossrefs, 'sizes': cmd_sizes, 'summary': cmd_summary}[name](args)

if __name__ == '__main__':
    main()
