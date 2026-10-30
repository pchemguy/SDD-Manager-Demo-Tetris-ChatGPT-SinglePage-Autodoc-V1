import hashlib
from pathlib import Path
import re
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]

def test_reproducible_single_file_artifact():
    if (ROOT/'tools/package.py').exists():
        subprocess.run([sys.executable,'tools/package.py'],cwd=ROOT,check=True,capture_output=True)
    source=(ROOT/'index.html').read_bytes()
    version=re.search(rb"const VERSION\s*=\s*['\"]([^'\"]+)",source).group(1).decode()
    artifact=ROOT/'dist'/version/('tetris-v'+version+'.html')
    assert artifact.is_file()
    assert artifact.read_bytes()==source
    assert hashlib.sha256(source).hexdigest() in (artifact.parent/'SHA256SUMS.txt').read_text()
    assert b'<style id="styles">' in source and b'<script id="app">' in source
    assert not re.search(rb'<(?:script|img)[^>]+src=',source)
