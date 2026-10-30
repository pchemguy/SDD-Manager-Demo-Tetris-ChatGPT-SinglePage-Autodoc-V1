"""Bounded isolated rendering/interaction capability probe; invoked per browser."""
from pathlib import Path
import os
import sys
from playwright.sync_api import sync_playwright
root = Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    kind = sys.argv[1]
    browser = getattr(p, kind).launch(headless=True, timeout=10000)
    for cycle in range(2):
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(5000)
        page.set_content('<button onclick="this.textContent=\'done\'">probe</button><canvas id="c" width="80" height="80"></canvas>')
        page.get_by_role('button').click()
        assert page.get_by_role('button').inner_text() == 'done'
        page.evaluate("const c=document.querySelector('canvas').getContext('2d');c.fillStyle='rgb(210,80,40)';c.fillRect(0,0,80,80)")
        assert page.evaluate("document.querySelector('canvas').getContext('2d').getImageData(4,4,1,1).data[0]") == 210
        page.screenshot(path=str(root / '.test-artifacts' / (kind + '-probe-' + str(cycle) + '.png')))
        context.close()
    print(kind + ' ' + browser.version + ': two context/input/Canvas/screenshot/teardown cycles passed', flush=True)
    browser.close()
