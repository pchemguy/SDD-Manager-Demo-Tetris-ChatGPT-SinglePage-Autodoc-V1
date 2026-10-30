"""Run the pinned project checks without modifying global Python packages."""
import os
from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parents[1]
env = os.environ.copy()
env['PYTHONPATH'] = str(root / '.devdeps') + os.pathsep + env.get('PYTHONPATH', '')
env['PLAYWRIGHT_BROWSERS_PATH'] = str(root / '.browser-runtime')
raise SystemExit(subprocess.call([sys.executable, '-m', 'pytest', *sys.argv[1:]], cwd=root, env=env))
