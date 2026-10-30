"""Create reproducible, standalone release files from the verified HTML source."""
from pathlib import Path
import hashlib
import re
import shutil
ROOT = Path(__file__).resolve().parents[1]

def package():
    source = (ROOT / 'index.html').read_bytes()
    version = re.search(rb"const VERSION\s*=\s*['\"]([^'\"]+)", source).group(1).decode()
    output = ROOT / 'dist' / version
    output.mkdir(parents=True, exist_ok=True)
    artifact = output / ('tetris-v' + version + '.html')
    artifact.write_bytes(source)
    files = [artifact]
    schema = ROOT / 'schema/session.schema.json'
    if schema.exists():
        target = output / 'session.schema.json'
        shutil.copyfile(schema, target)
        files.append(target)
    checksums = ''.join(hashlib.sha256(f.read_bytes()).hexdigest() + '  ' + f.name + '\n' for f in files)
    (output / 'SHA256SUMS.txt').write_text(checksums)
    return output

if __name__ == '__main__':
    print(package())
