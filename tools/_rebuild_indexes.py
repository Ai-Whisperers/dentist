#!/usr/bin/env python3
"""_rebuild_indexes.py — rebuild every 00-index.md with real links to children."""
import pathlib, re
from collections import defaultdict

ROOT = pathlib.Path('.').resolve()
FOLDERS = [
'00_STRATEGIC', '01_RESEARCH', '02_MEETINGS', '03_LAUNCH', '04_SALES',
'05_OPERATIONS', '06_MARKETING', '07_DESIGN', '08_MESSAGING', '09_TEMPLATES',
]

def title_of(path: pathlib.Path) -> str:
    text = path.read_text(errors='ignore').splitlines()
    for line in text:
        m = re.match(r'^#+\s*(.+)', line)
        if m:
            t = m.group(1).strip()
            # skip cross-ref blocks
            if 'PRICING CROSS-REFERENCE' in t:
                continue
            return t
    return path.name

def rel_link(path: pathlib.Path, parent: pathlib.Path) -> str:
    return str(path.relative_to(parent))

def child_md(folder: pathlib.Path):
    # return .md files under this folder, excluding 00-index.md (and 00-INDEX.md), sorted
    out = []
    for p in sorted(folder.rglob('*.md')):
        name = p.name
        if name in {'00-index.md', '00-INDEX.md'}:
            continue
        out.append(p)
    return out

def group_by_top(paths, folder):
    # group by top-level subdir relative to folder
    groups = defaultdict(list)
    for p in paths:
        rel = p.relative_to(folder)
        if len(rel.parts) == 1:
            key = ''
        else:
            key = rel.parts[0]
        groups[key].append(p)
    return dict(sorted(groups.items(), key=lambda kv: (kv[0] == '', kv[0])))

def build_index(folder: pathlib.Path):
    fname = folder.name
    lines = []
    lines.append(f'# {fname} — Index\n')

    # natural-language intro
    descriptions = {
        '00_STRATEGIC': 'Strategic layer: financials, pricing, options, rollout plan, and phase checklist.',
        '01_RESEARCH': 'Research reports across market, legal, payments, locations, procurement, and community.',
        '02_MEETINGS': 'Meeting materials split by audience: client prep and Kiki sessions.',
        '03_LAUNCH': 'Execution plans: roadmap, corporate and institutional sales, CRM, website content, Messaging outreach.',
        '04_SALES': 'Corporate agreements and contracts ready for client execution.',
        '05_OPERATIONS': 'Day-to-day operations, clinical routines, patient communications, and legal docs.',
        '06_MARKETING': 'Digital presence: Carrd, Google Business, SEO blog posts, website spec.',
        '07_DESIGN': 'Brand assets and website page content (core + transactional + service pages).',
        '08_MESSAGING': 'Messaging Business automation, operation guides, and setup templates.',
        '09_TEMPLATES': 'Patient communication templates: appointment, recall, referral, email.',
    }
    lines.append(descriptions.get(fname, ''))
    lines.append('')

    children = child_md(folder)
    if not children:
        lines.append('_(empty)_\n')
        return '\n'.join(lines)

    groups = group_by_top(children, folder)
    for key, paths in groups.items():
        if key == '':
            lines.append('## Root files')
        else:
            lines.append(f'## {key}/')
        for p in paths:
            t = title_of(p)
            l = rel_link(p, folder)
            lines.append(f'- [`{t}`]({l})')
        lines.append('')

    # canonical pricing reminder
    if fname != 'ARCHIVE':
        lines.append('---')
        lines.append('> **PRICING CROSS-REFERENCE:** Prices in this folder reference `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` unless noted otherwise.')
        lines.append('')

    # audit reminder
    lines.append('---')
    lines.append('Audit this folder anytime: `tools/repo-audit.py summary`')
    lines.append('')
    return '\n'.join(lines)

for folder_name in FOLDERS:
    folder = ROOT / folder_name
    if not folder.exists():
        continue
    idx = folder / '00-index.md'
    content = build_index(folder)
    idx.write_text(content, encoding='utf-8')
    print(f'wrote {idx}')
