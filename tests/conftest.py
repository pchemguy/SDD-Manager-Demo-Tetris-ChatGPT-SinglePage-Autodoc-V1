import json
import os
from pathlib import Path
import re
import subprocess
import pytest

ROOT = Path(__file__).resolve().parents[1]

@pytest.fixture
def js():
    def evaluate(expression):
        source = re.search(r'<script id="app">([\s\S]*?)</script>', (ROOT / 'index.html').read_text()).group(1)
        runner = "const vm=require('node:vm');let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{const p=JSON.parse(s);const c={__TETRIS_TEST__:true,console};vm.createContext(c);vm.runInContext(p.source,c);console.log(JSON.stringify(vm.runInContext(p.expression,c)));});"
        result = subprocess.run(['node', '-e', runner], input=json.dumps({'source': source, 'expression': expression}), text=True, capture_output=True, timeout=15)
        assert result.returncode == 0, result.stderr
        return json.loads(result.stdout)
    return evaluate
