#!/usr/bin/env python3
"""Run DOM checks with isolated, pinned dependencies; never modify the repository."""
import os
from pathlib import Path
import subprocess
import tempfile
import shutil
import knowledge

ROOT = Path(__file__).resolve().parents[1]


def check():
    with tempfile.TemporaryDirectory(prefix='knowledge-dom-') as directory:
        subprocess.run([
            shutil.which('npm') or 'npm', 'install', '--prefix', directory, 'jsdom@24.1.3',
            '--ignore-scripts', '--no-audit', '--no-fund',
        ], check=True)
        env = dict(os.environ, NODE_PATH=str(Path(directory) / 'node_modules'))
        demo = Path(directory) / 'demo'
        knowledge.build(ROOT / 'docs/knowledge/examples', demo, '/knowledge/demo', True)
        env['COURSE_DEMO_ROOT'] = str(demo)
        subprocess.run(['node', 'tests/knowledge.dom.cjs'], cwd=ROOT, env=env, check=True)


if __name__ == '__main__':
    check()
