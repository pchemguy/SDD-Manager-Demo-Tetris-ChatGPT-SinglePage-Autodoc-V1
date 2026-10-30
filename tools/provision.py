"""Provision pinned, isolated browsers and verify real rendering and SQLite assets.

Run after installing requirements-dev.txt into .devdeps. No system browser or
personal browser profile is used. A diagnosed Firefox namespace failure permits
only a child-process sandbox override, recorded in provisioning.json.
"""
from pathlib import Path
import base64
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / '.test-artifacts'
ARTIFACTS.mkdir(exist_ok=True)
env = os.environ.copy()
env['PYTHONPATH'] = str(ROOT / '.devdeps')
env['PLAYWRIGHT_BROWSERS_PATH'] = str(ROOT / '.browser-runtime')


def bounded(args, child_env, seconds):
    """Reap the owned process group if an external runtime hangs."""
    child = subprocess.Popen(args, cwd=ROOT, env=child_env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             start_new_session=os.name != 'nt')
    try:
        out, err = child.communicate(timeout=seconds)
    except subprocess.TimeoutExpired:
        if os.name == 'nt':
            subprocess.run(['taskkill', '/PID', str(child.pid), '/T', '/F'],
                           capture_output=True, timeout=10)
        else:
            os.killpg(child.pid, signal.SIGKILL)
        out, err = child.communicate(timeout=10)
        raise RuntimeError('Owned subprocess timed out: ' + err[-1200:])
    return child.returncode, out, err


catalog = json.loads((ROOT / '.devdeps/playwright/driver/package/browsers.json').read_text())
missing = [item for item in catalog['browsers']
           if item['name'] in ['chromium-headless-shell', 'firefox']
           and not (ROOT / '.browser-runtime' / (item['name'].replace('-', '_') + '-' + item['revision'])).exists()]
if missing:
    code, out, err = bounded([sys.executable, '-m', 'playwright', 'install', '--only-shell', 'chromium', 'firefox'], env, 180)
    print(out, flush=True)
    if code:
        raise RuntimeError('Managed browser install failed: ' + err[-1500:])
record = {}
for kind in ['chromium', 'firefox']:
    for attempt in range(2):
        child_env = env.copy()
        child_env['DEBUG'] = 'pw:browser'
        if attempt:
            child_env['MOZ_DISABLE_CONTENT_SANDBOX'] = '1'
        code, out, err = bounded([sys.executable, 'tools/browser_probe.py', kind], child_env, 35)
        (ARTIFACTS / f'probe-{kind}-{attempt}.log').write_text(out + err)
        if code == 0:
            record[kind] = {'ready': True, 'sandbox_override': bool(attempt), 'evidence': out.strip()}
            print(out, flush=True)
            break
        if kind != 'firefox' or attempt or not any(term in err for term in ['EPERM', 'uid_map', 'CanCreateUserNamespace', 'Sandbox']):
            raise RuntimeError('Browser capability unavailable: ' + err[-1500:])
    else:
        raise RuntimeError('Browser probe failed')
(ARTIFACTS / 'provisioning.json').write_text(json.dumps(record, indent=2))
source = (ROOT / 'index.html').read_text()
url = re.search(r"const SQLJS_URL='([^']+)'", source).group(1)
integrity = re.search(r"const SQLJS_INTEGRITY='([^']+)'", source).group(1)
asset = ARTIFACTS / 'sqljs-inline.js'
if not asset.exists():
    with urllib.request.urlopen(urllib.request.Request(url, headers={'Accept-Encoding': 'identity'}), timeout=25) as response:
        if response.geturl() != url or response.headers.get('Access-Control-Allow-Origin') != '*':
            raise RuntimeError('Unexpected SQLite dependency redirect or CORS response')
        raw = response.read(3000001)
    asset.write_bytes(raw)
raw = asset.read_bytes()
if integrity != 'sha384-' + base64.b64encode(hashlib.sha384(raw).digest()).decode():
    raise RuntimeError('SQLite dependency integrity mismatch')
(ARTIFACTS / 'sqljs-manifest.json').write_text(json.dumps({
    'version': '1.15.0', 'url': url, 'integrity': integrity,
    'sha256': hashlib.sha256(raw).hexdigest(), 'cors': '*'}, indent=2))
print('Isolated browser probes and pinned SQLite dependency verified.', flush=True)
