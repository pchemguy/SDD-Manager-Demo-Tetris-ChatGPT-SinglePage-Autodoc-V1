"""Acceptance checks against the actual single-file application and isolated runtimes."""
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
        runner = "const vm=require('node:vm');let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{const p=JSON.parse(s);const c={__TETRIS_TEST__:true,console,URL,URLSearchParams,TextDecoder,TextEncoder};vm.createContext(c);vm.runInContext(p.source,c);console.log(JSON.stringify(vm.runInContext(p.expression,c)));});"
        result = subprocess.run(['node', '-e', runner], input=json.dumps({'source': source, 'expression': expression}), text=True, capture_output=True, timeout=15)
        assert result.returncode == 0, result.stderr
        return json.loads(result.stdout)
    return evaluate

@pytest.fixture(scope='session')
def base_url():
    import functools
    from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
    import threading
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield 'http://127.0.0.1:' + str(server.server_port)
    server.shutdown()
    server.server_close()

@pytest.fixture(scope='session', params=['chromium', 'firefox'])
def browser(request):
    from playwright.sync_api import sync_playwright
    provisioning = json.loads((ROOT / '.test-artifacts/provisioning.json').read_text())
    with sync_playwright() as p:
        options = {'headless': True, 'timeout': 10000}
        if provisioning[request.param]['sandbox_override']:
            options['env'] = {**os.environ, 'MOZ_DISABLE_CONTENT_SANDBOX': '1'}
        b = getattr(p, request.param).launch(**options)
        yield b
        b.close()

@pytest.fixture
def page(browser, base_url):
    context = browser.new_context(viewport={'width':1440,'height':1000}, accept_downloads=True)
    page = context.new_page()
    errors=[]
    page.on('pageerror',lambda error:errors.append(str(error)))
    page.set_default_timeout(5000)
    page.add_init_script('globalThis.__TETRIS_TEST__ = true')
    page.goto(base_url + '/index.html')
    yield page
    context.close()
    assert not errors, errors


@pytest.fixture
def sql_page(page):
    info=json.loads((ROOT/'.test-artifacts/sqljs-manifest.json').read_text())
    body=(ROOT/'.test-artifacts/sqljs-inline.js').read_bytes()
    import hashlib,base64
    assert info['integrity']=='sha384-'+base64.b64encode(hashlib.sha384(body).digest()).decode()
    page.route(info['url'],lambda route:route.fulfill(status=200,body=body,content_type='application/javascript',headers={'access-control-allow-origin':info['cors']}))
    return page
