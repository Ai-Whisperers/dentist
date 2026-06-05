#!/usr/bin/env python3
"""Price propagation: sync docs to canonical pricing reference."""
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path('.').resolve()
CANONICAL = ROOT / '00_STRATEGIC' / 'financial-pricing' / 'canonical-pricing-reference-v2.md'
CHANGELOG = ROOT / 'CHANGELOG.md'

# Parse canonical prices: service -> Gs value
CANONICAL_RE = re.compile(r'^\|\s*([^|]+?)\s*\|\s*([0-9,]+)\s*Gs\s*\|', re.MULTILINE)

def parse_canonical():
    text = CANONICAL.read_text(errors='ignore')
    prices = {}
    for m in CANONICAL_RE.finditer(text):
        service = m.group(1).strip()
        value = int(m.group(2).replace(',', ''))
        prices[service.lower()] = value
    return prices

# Lightweight heuristic: find price mentions in non-canonical active docs
PRICE_MENTION_RE = re.compile(r'Gs\s*(\d{3,}(?:[.,]\d{3})*)')

def scan_docs():
    prices = parse_canonical()
    changes = defaultdict(list)  # file -> [(old_price, new_price, match_context)]
    for p in ROOT.rglob('*.md'):
        if not p.is_relative_to(ROOT):
            continue
        rel = p.relative_to(ROOT)
        # Skip canonical, ARCHIVE, meta files
        if p.resolve() == CANONICAL.resolve():
            continue
        if any(d in p.parts for d in ('ARCHIVE', '.git', 'node_modules', '.venv', 'meal-prerp-website')):
            continue
        text = p.read_text(errors='ignore')
        # Skip files that already have the pricing cross-ref block? No, still scan
        for m in PRICE_MENTION_RE.finditer(text):
            raw = m.group(1)
            try:
                value = int(raw.replace('.', '').replace(',', ''))
            except ValueError:
                continue
            # Find closest canonical match by keyword proximity
            # Simple: if any canonical service keyword appears near the price line
            line_start = text.rfind('\n', 0, m.start()) + 1
            line_end = text.find('\n', m.end())
            line = text[line_start:line_end] if line_end != -1 else text[line_start:]
            context = line.strip()
            matched_service = None
            for svc, canon in prices.items():
                if svc in context.lower() and value != canon:
                    matched_service = svc
                    break
            if matched_service:
                changes[str(rel)].append((raw, f"{prices[matched_service]:,}", context[:120]))
    return changes

def dry_run():
    changes = scan_docs()
    if not changes:
        print('No pricing mismatches found against canonical.')
        return 0
    total = sum(len(v) for v in changes.values())
    print(f'Found {total} proposed price changes across {len(changes)} files:')
    for file, items in sorted(changes.items()):
        print(f'\n{file}:')
        for old, new, ctx in items:
            print(f'  - {old} -> {new}  [{ctx}]')
    print('\nRun with --apply to confirm each change interactively.')
    return 1

def apply_changes():
    changes = scan_docs()
    if not changes:
        print('No pricing mismatches found.')
        return 0
    log_entries = []
    for file, items in sorted(changes.items()):
        path = ROOT / file
        text = path.read_text(errors='ignore')
        new_text = text
        for old, new, ctx in items:
            # Simple string replace; careful with locale formats
            old_raw = old.replace('.', '').replace(',', '') if '.' in old else old
            new_raw = new.replace('.', '').replace(',', '') if '.' in new else new
            if old_raw in new_text:
                confirm = input(f'Update {file}: {old_raw} -> {new_raw}? [Y/n] ').strip().lower()
                if confirm in ('', 'y', 'yes'):
                    new_text = new_text.replace(old_raw, new_raw)
                    log_entries.append((file, old_raw, new_raw))
            else:
                print(f'  SKIP {file}: {old_raw} not found (format mismatch?)')
        if new_text != text:
            path.write_text(new_text)
    if not log_entries:
        print('No changes applied.')
        return 0
    # Update CHANGELOG.md
    changelog_entry = f'\n## Pricing sync — {datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
    for f, old, new in log_entries:
        changelog_entry += f'- `{f}`: {old} -> {new}\n'
    if CHANGELOG.exists():
        existing = CHANGELOG.read_text()
        CHANGELOG.write_text(existing.rstrip() + '\n' + changelog_entry)
    else:
        CHANGELOG.write_text('# CHANGELOG\n' + changelog_entry)
    # Git commit
    files = [str(ROOT / f) for f, _, _ in log_entries] + [str(CHANGELOG)]
    msg = f'chore(pricing): sync {len(log_entries)} prices to canonical reference'
    subprocess.run(['git', 'add', '-A'], cwd=ROOT, check=True)
    subprocess.run(['git', 'commit', '-m', msg], cwd=ROOT, check=True)
    print(f'Committed: {msg}')
    return 0

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print('Usage: update-pricing.py [dry-run|--dry-run] [--apply]')
        return 0
    if sys.argv[1] in ('dry-run', '--dry-run'):
        return dry_run()
    if sys.argv[1] == '--apply':
        return apply_changes()
    print('Unknown command. Use dry-run or --apply.')
    return 1

if __name__ == '__main__':
    sys.exit(main())
