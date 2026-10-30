"""Extract the runtime JSON Schema from the single authoritative application."""
from pathlib import Path
import re
import subprocess
ROOT=Path(__file__).resolve().parents[1]
source=re.search(r'<script id="app">([\s\S]*?)</script>',(ROOT/'index.html').read_text()).group(1)
program="let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>console.log(require('node:vm').runInNewContext(s+';JSON.stringify(EXPORT_SCHEMA,null,2)',{__TETRIS_TEST__:true})));"
result=subprocess.check_output(['node','-e',program],input=source,text=True,timeout=15)
(ROOT/'schema/session.schema.json').write_text(result)
