#!/usr/bin/env python3
"""
audit-structure.py — auditoría estructural del repo
Uso: python3 scripts/audit-structure.py
Output: stats de carpetas, archivos grandes, duplicados, etc.
"""
import subprocess
from collections import Counter
import sys

REPO = "/tmp/dentist-repo"

def run(cmd, **kwargs):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kwargs)

def main():
    print("=" * 80)
    print(f"AUDITORÍA ESTRUCTURAL — {REPO}")
    print("=" * 80)

    # 1. Tree depth 2
    print("\n📁 CARPETAS (top-level + level 2)")
    result = run(['find', '.', '-maxdepth', '2', '-type', 'd',
                  '-not', '-path', './.git*',
                  '-not', '-path', './ARCHIVE*',
                  '-not', '-path', './.hermes*'])
    dirs = sorted([d for d in result.stdout.strip().split('\n') if d])
    for d in dirs:
        name = d.replace('./', '') if d != '.' else 'ROOT'
        count_run = run(['find', d, '-maxdepth', '1', '-type', 'f'])
        n = len([f for f in count_run.stdout.strip().split('\n') if f])
        print(f"  {name:50} {n:4} archivos")

    # 2. Densidad por subcarpeta
    print("\n📊 DENSIDAD POR CARPETA (md files)")
    result = run(['find', '.', '-type', 'f', '-name', '*.md',
                  '-not', '-path', './.git/*',
                  '-not', '-path', './ARCHIVE/*',
                  '-not', '-path', './.hermes/*'])
    dir_counts = Counter()
    for path in result.stdout.strip().split('\n'):
        if not path: continue
        parts = path.split('/')
        if len(parts) >= 3:
            dir_ = '/'.join(parts[1:3])
            dir_counts[dir_] += 1

    for dir_, count in dir_counts.most_common(25):
        print(f"  {count:4}  {dir_}")

    # 3. Archivos grandes
    print("\n💾 ARCHIVOS GRANDES (>10KB)")
    result = run(['find', '.', '-type', 'f', '-name', '*.md',
                  '-not', '-path', './.git/*',
                  '-not', '-path', './ARCHIVE/*',
                  '-not', '-path', './.hermes/*',
                  '-exec', 'du', '-k', '{}', ';'])
    sizes = []
    for line in result.stdout.strip().split('\n'):
        if not line: continue
        parts = line.split('\t')
        if len(parts) >= 2:
            try:
                kb = int(parts[0])
                sizes.append((kb, parts[1]))
            except ValueError:
                pass
    sizes.sort(reverse=True)
    for kb, path in sizes[:30]:
        print(f"  {kb:5}KB  {path}")

    # 4. Root .md files
    print("\n📋 ARCHIVOS .MD EN ROOT (deberían estar en docs/)")
    result = run(['ls', '-la', './'])
    import os
    for f in sorted(os.listdir(REPO)):
        full = os.path.join(REPO, f)
        if os.path.isfile(full) and f.endswith('.md'):
            size = os.path.getsize(full) // 1024
            print(f"  {size:5}KB  {f}")

if __name__ == "__main__":
    main()
