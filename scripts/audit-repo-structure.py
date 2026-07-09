#!/usr/bin/env python3
"""audit-repo-structure.py — reusable repo analyzer"""
import subprocess, os
from collections import Counter
import sys

def scan(path=".", ext="md"):
    r = subprocess.run(['find', path, '-type', 'f', f'-name=*.{ext}',
                        '-not', '-path', './.git/*',
                        '-not', '-path', './ARCHIVE/*',
                        '-not', '-path', './.hermes/*'],
                       capture_output=True, text=True, cwd='/tmp/dentist-repo')
    return [l for l in r.stdout.strip().split('\n') if l]

if __name__ == "__main__":
    files = scan()
    print(f"Total: {len(files)}")
