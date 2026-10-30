"""Acceptance checks against the actual single-file application and isolated runtimes."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_board_information_and_render(page):
    assert page.locator('#board').count() == 1
    assert page.get_by_role('button', name='Start/Restart', exact=True).count() == 1
    assert page.get_by_role('button', name='Pause/Start', exact=True).count() == 1
    assert page.locator('#board').evaluate("c=>c.getContext('2d').getImageData(20,20,1,1).data[3]") == 255
    assert page.locator('#score').inner_text() == '0'
    box = page.locator('#board').bounding_box()
    assert abs(box['x'] + box['width']/2 - 720) < 2

def test_real_keyboard_pause_and_restart(page):
    page.get_by_role('button', name='Start/Restart', exact=True).click()
    assert page.locator('#state').text_content() == 'In motion'
    before = page.evaluate('Tetris.ui.game.p.x')
    page.keyboard.press('ArrowLeft')
    assert page.evaluate('Tetris.ui.game.p.x') == before - 1
    page.keyboard.press('Escape')
    frozen = page.evaluate('[Tetris.ui.game.p.y,Tetris.ui.game.elapsed]')
    page.wait_for_timeout(150)
    assert page.evaluate('[Tetris.ui.game.p.y,Tetris.ui.game.elapsed]') == frozen
    assert page.locator('#state').text_content() == 'Paused'
    page.get_by_role('button', name='Pause/Start', exact=True).click()
    assert page.locator('#state').text_content() == 'In motion'
    page.evaluate('Tetris.ui.game.score=999;Tetris.render()')
    page.get_by_role('button', name='Start/Restart', exact=True).click()
    assert page.locator('#score').inner_text() == '0'

import pytest

@pytest.mark.parametrize('width',[360,768,1440])
def test_required_panels_and_centering(page, width):
    page.set_viewport_size({'width':width,'height':1000})
    before = page.locator('#board').bounding_box()
    assert abs(before['x'] + before['width']/2 - width/2) < 2
    info = page.locator('.info').bounding_box()
    assert info['x'] >= 0 and info['x'] + info['width'] <= width
    for control in page.locator('.game-buttons button').all():
        rect=control.bounding_box()
        assert rect['x'] >= info['x'] and rect['x']+rect['width'] <= info['x']+info['width']
        assert control.evaluate('(b)=>b.scrollWidth<=b.clientWidth')
    page.get_by_role('button',name='Controls / help',exact=True).click()
    assert not page.locator('#help').is_visible()
    after = page.locator('#board').bounding_box()
    assert abs(after['x'] - before['x']) < 1
    assert abs(after['width'] - before['width']) < 1


def test_game_over_render_and_restart(page, browser):
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    page.evaluate("const g=Tetris.ui.game;g.board[0]=Array(10).fill('J');g.spawn('O');Tetris.render()")
    assert page.locator('#state').text_content() == 'Game over'
    assert page.locator('#veil').is_visible()
    page.screenshot(path=str(Path(__file__).resolve().parents[1]/'.test-artifacts'/('classic-'+browser.browser_type.name+'.png')))
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    assert page.evaluate('Tetris.ui.game.board.flat().filter(Boolean).length') == 0
    assert page.locator('#state').text_content() == 'In motion'

def test_packaged_download_plays_without_server(browser):
    import re, subprocess, sys
    root=Path(__file__).resolve().parents[1]
    subprocess.run([sys.executable,'tools/package.py'],cwd=root,check=True,capture_output=True)
    version=re.search(r"const VERSION\s*=\s*'([^']+)'",(root/'index.html').read_text()).group(1)
    artifact=root/'dist'/version/('tetris-v'+version+'.html')
    context=browser.new_context()
    p=context.new_page()
    try:
        p.goto(artifact.as_uri())
        p.get_by_role('button',name='Start/Restart',exact=True).click()
        assert p.locator('#state').text_content() == 'In motion'
        p.keyboard.press('Escape')
        assert p.locator('#state').text_content() == 'Paused'
        assert p.locator('#board').evaluate("c=>c.getContext('2d').getImageData(10,10,1,1).data[3]") == 255
    finally:
        context.close()


def test_modern_keys_and_shared_ghost(page):
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    original=page.evaluate('Tetris.ui.game.p.type')
    page.keyboard.press('c')
    assert page.evaluate('Tetris.ui.game.held') == original
    after=page.evaluate('Tetris.ui.game.p.type')
    page.keyboard.press('c')
    assert page.evaluate('Tetris.ui.game.p.type') == after
    page.evaluate("const g=Tetris.ui.game;g.board=Array.from({length:20},()=>Array(10).fill(0));g.p={type:'O',rot:0,x:4,y:0};g.config.lockPolicy='failed';g.syncGround();Tetris.render()")
    assert page.locator('#board').evaluate("c=>c.getContext('2d').getImageData(246,1086,1,1).data[0]") > 30
    page.keyboard.press('Space')
    assert page.evaluate('Tetris.ui.game.board.flat().filter(Boolean).length') == 4


def test_penetrator_key_indicator_and_hold(page):
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    page.evaluate('Tetris.ui.game.bonuses=2;Tetris.render()')
    page.keyboard.press('p')
    assert page.evaluate('Tetris.ui.game.p.penetrator') is True
    assert page.locator('#bonuses').text_content().count('⚡') == 1
    page.keyboard.press('c')
    assert page.evaluate('Tetris.ui.game.held') is None


def test_six_labeled_settings(page):
    assert page.locator('#settings select[id^=setting-]').count() == 6
    assert page.get_by_label('Ghost piece',exact=True).input_value() == 'show'
    assert page.get_by_label('General locking',exact=True).input_value() == 'interval'
    assert page.get_by_label('Hold piece',exact=True).input_value() == 'true'


def test_session_settings_and_panel_visibility(page):
    page.get_by_label('Hard drop',exact=True).select_option('false')
    assert page.evaluate('Tetris.ui.game.config.hardDrop') is False
    durable=page.evaluate('!!Tetris.persistence')
    if not durable:
        assert page.context.cookies() == []
        assert '?' not in page.url
    page.reload()
    assert page.evaluate('Tetris.ui.game.config.hardDrop') is (not durable)
    center=page.locator('#board').bounding_box()
    page.get_by_role('button',name='Settings',exact=True).click()
    assert not page.locator('#settings').is_visible()
    assert abs(page.locator('#board').bounding_box()['x']-center['x']) < 1
    page.get_by_role('button',name='Settings',exact=True).click()
    assert page.locator('#settings').is_visible()


def test_url_cookie_precedence_reload_and_omission(page,base_url):
    page.context.add_cookies([{'name':'tetris_ghost','value':'hide','url':base_url},{'name':'tetris_hardDrop','value':'off','url':base_url},{'name':'tetris_hold','value':'off','url':base_url}])
    page.goto(base_url+'/index.html?ghost=show&nextPreview=off&keep=1#frag')
    assert page.evaluate('[Tetris.ui.game.config.ghost,Tetris.ui.game.config.hardDrop,Tetris.ui.game.config.nextPreview,Tetris.ui.game.config.hold]') == ['show',False,False,False]
    cookies={x['name']:x['value'] for x in page.context.cookies()}
    assert cookies['tetris_ghost']=='show' and cookies['tetris_hardDrop']=='off'
    page.get_by_label('Hold piece',exact=True).select_option('true')
    assert 'hold=on' in page.url and 'keep=1' in page.url and page.url.endswith('#frag')
    page.reload()
    assert page.evaluate('Tetris.ui.game.config.hold') is True


def test_cookie_rejection_is_a_visible_nonfatal_warning(page,base_url):
    page.add_init_script("Object.defineProperty(document,'cookie',{get(){return ''},set(){throw Error('blocked')}})")
    page.goto(base_url+'/index.html?ghost=show')
    page.get_by_label('Hard drop',exact=True).select_option('false')
    assert page.evaluate('Tetris.ui.game.config.hardDrop') is False
    assert 'unavailable' in page.locator('#message').text_content()


def test_history_rejection_preserves_session_value(page,base_url):
    page.add_init_script("History.prototype.replaceState=function(){throw Error('blocked history')}")
    page.goto(base_url+'/index.html')
    before=page.url
    page.get_by_label('Hard drop',exact=True).select_option('false')
    assert page.evaluate('Tetris.ui.game.config.hardDrop') is False
    assert page.url==before
    assert 'URL persistence is unavailable' in page.locator('#message').text_content()


def test_leaderboard_panel_and_stable_center(page):
    assert page.locator('#leaderboard').is_visible()
    before=page.locator('#board').bounding_box()
    page.get_by_role('button',name='Leaderboard',exact=True).click()
    assert not page.locator('#leaderboard').is_visible()
    assert abs(page.locator('#board').bounding_box()['x']-before['x'])<1


def test_completed_history_restart_and_reload(page):
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    page.evaluate('Tetris.ui.game.score=500;Tetris.ui.game.finish();Tetris.render();Tetris.render()')
    assert page.locator('#results li').count()==1
    assert page.evaluate('Tetris.ui.results.records[0].score')==500
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    page.evaluate('Tetris.ui.game.score=900')
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    assert page.locator('#results li').count()==1
    page.reload()
    assert page.locator('#results li').count()==0


def test_save_json_snapshot_and_hidden_file_controls(page):
    import json
    assert page.get_by_role('button',name='Save',exact=True).count()==1
    page.evaluate("Tetris.ui.results.replace([{id:'stable-1',score:42,timestamp:'2026-10-30T00:00:00.000Z'}]);Tetris.render()")
    with page.expect_download() as received:
        page.get_by_role('button',name='Save',exact=True).click()
    data=json.loads(Path(received.value.path()).read_text())
    assert data['formatVersion']==1 and data['results'][0]=={'id':'stable-1','score':42,'timestamp':'2026-10-30T00:00:00.000Z'}
    assert len(data['settings'])==6 and isinstance(data['settings']['hold'],bool)
    page.get_by_role('button',name='Settings',exact=True).click()
    assert not page.get_by_role('button',name='Save',exact=True).is_visible()
    assert not page.get_by_role('button',name='Restore',exact=True).is_visible()


def test_json_restore_validation_is_atomic(page):
    import json
    assert page.get_by_role('button',name='Restore',exact=True).is_enabled()
    before=page.evaluate('({results:Tetris.ui.results.records,settings:Tetris.ui.game.config,cookies:document.cookie,url:location.href})')
    for broken in [dict(formatVersion=2,results=[],settings=before['settings']),dict(formatVersion=1,results=[{'id':'bad','score':3,'timestamp':'2025-02-29T00:00:00.000Z'}],settings=before['settings'])]:
        page.evaluate("document.getElementById('message').textContent=''")
        page.locator('#restore-input').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':json.dumps(broken).encode()})
        page.wait_for_function("document.getElementById('message').textContent.startsWith('Could not restore:')")
        after=page.evaluate('({results:Tetris.ui.results.records,settings:Tetris.ui.game.config,cookies:document.cookie,url:location.href})')
        assert after==before
    good={'formatVersion':1,'results':[{'id':'restored-stable','score':123,'timestamp':'2026-10-30T01:02:03.004Z'}],'settings':before['settings']}
    page.locator('#restore-input').set_input_files({'name':'good.json','mimeType':'application/json','buffer':json.dumps(good).encode()})
    page.wait_for_function("document.getElementById('message').textContent==='Session restored.'")
    assert page.evaluate('Tetris.ui.results.records')==good['results']
    assert len(page.context.cookies())==6
    assert 'ghost=show' in page.url and 'hold=on' in page.url


def test_sql_runtime_lazy_single_file_load(sql_page):
    requests=[]
    sql_page.on('request',lambda request:requests.append(request.url))
    assert sql_page.evaluate("async()=>{if(!Tetris.loadSQL)return null;const unloaded=typeof initSqlJs==='undefined',a=Tetris.loadSQL(),b=Tetris.loadSQL(),SQL=await a,db=new SQL.Database();try{return [unloaded,a===b,db.exec('SELECT 42')[0].values[0][0]]}finally{db.close()}}") == [True,True,42]
    assert len([url for url in requests if url.startswith('https://')])==1


def test_sqlite_export_is_standard_and_preserves_values(sql_page):
    import sqlite3
    assert sql_page.evaluate("async()=>{if(!Tetris.encodeSQLite)return null;const b=await Tetris.encodeSQLite({formatVersion:1,results:[],settings:{...Tetris.DEFAULTS}});return String.fromCharCode(...b.slice(0,15))}") == 'SQLite format 3'
    sql_page.evaluate("Tetris.ui.results.replace([{id:'zero',score:0,timestamp:'2026-10-30T00:00:00.000Z'},{id:'max',score:Number.MAX_SAFE_INTEGER,timestamp:'2026-10-30T01:02:03.004Z'}]);Tetris.render()")
    sql_page.locator('#file-format').select_option('sqlite')
    with sql_page.expect_download() as received:
        sql_page.get_by_role('button',name='Save',exact=True).click()
    file=Path(received.value.path())
    assert file.read_bytes().startswith(b'SQLite format 3'+bytes([0]))
    db=sqlite3.connect('file:'+str(file)+'?mode=ro',uri=True)
    try:
        assert db.execute('PRAGMA user_version').fetchone()[0]==1
        assert db.execute('PRAGMA application_id').fetchone()[0]==1414812243
        assert db.execute('SELECT id,score,timestamp,typeof(score) FROM high_scores ORDER BY score DESC').fetchall()==[('max',9007199254740991,'2026-10-30T01:02:03.004Z','integer'),('zero',0,'2026-10-30T00:00:00.000Z','integer')]
        assert db.execute('SELECT count(*) FROM settings').fetchone()[0]==6
        assert db.execute("SELECT value FROM settings WHERE key='hold'").fetchone()[0]=='on'
    finally:
        db.close()


def test_sqlite_restore_and_complete_invalid_content(sql_page):
    assert sql_page.evaluate("async()=>{const data={formatVersion:1,results:[{id:'sql-stable',score:777,timestamp:'2026-10-30T00:00:00.000Z'}],settings:{...Tetris.DEFAULTS}};const bytes=await Tetris.encodeSQLite(data);return await Tetris.restoreFile(new File([bytes],'valid.json'))}") is True
    assert sql_page.evaluate('Tetris.ui.results.records[0].id')=='sql-stable'
    before=sql_page.evaluate('({results:Tetris.ui.results.records,settings:Tetris.ui.game.config,cookies:document.cookie,url:location.href})')
    for mutation in ["UPDATE high_scores SET timestamp='2025-02-29T00:00:00.000Z'","UPDATE settings SET value='invalid' WHERE key='hold'","PRAGMA user_version=999","CREATE VIEW extra AS SELECT 1","ALTER TABLE high_scores ADD COLUMN hidden_extra TEXT GENERATED ALWAYS AS ('x') VIRTUAL"]:
        assert sql_page.evaluate("async sql=>{const SQL=await Tetris.loadSQL(),bytes=await Tetris.encodeSQLite({formatVersion:1,results:[{id:'reject-me',score:1,timestamp:'2026-10-30T00:00:00.000Z'}],settings:{...Tetris.DEFAULTS}}),db=new SQL.Database(bytes);try{db.run(sql);return await Tetris.restoreFile(new File([db.export()],'invalid.sqlite'))}finally{db.close()}}",mutation) is False
        assert sql_page.evaluate('({results:Tetris.ui.results.records,settings:Tetris.ui.game.config,cookies:document.cookie,url:location.href})')==before


def test_transfer_parity_and_newest_restore_wins(sql_page):
    assert sql_page.evaluate("async()=>{const data={formatVersion:1,results:[{id:'roundtrip',score:9007199254740991,timestamp:'2026-10-30T01:02:03.004Z'}],settings:{ghost:'dynamic',hardDrop:false,nextPreview:false,hardDropLock:'immediate',lockPolicy:'failed',hold:false}};const a=Tetris.parseExportJSON(JSON.stringify(data)),b=await Tetris.decodeSQLite(await Tetris.encodeSQLite(a));return JSON.stringify(a)===JSON.stringify(b)}") is True
    assert sql_page.evaluate("async()=>{const data=id=>JSON.stringify({formatVersion:1,results:[{id,score:1,timestamp:'2026-10-30T00:00:00.000Z'}],settings:{...Tetris.DEFAULTS}});const bytes=new TextEncoder().encode(data('old'));const old={size:bytes.length,arrayBuffer:()=>new Promise(resolve=>setTimeout(()=>resolve(bytes.buffer),40))};const a=Tetris.restoreFile(old),b=Tetris.restoreFile(new File([data('new')],'new.json'));return [await a,await b,Tetris.ui.results.records[0].id]}") == [False,True,'new']


def test_sql_dependency_failure_is_retryable(page):
    import json
    info=json.loads((ROOT/'.test-artifacts/sqljs-manifest.json').read_text())
    page.route(info['url'],lambda route:route.abort())
    assert page.evaluate('async()=>{try{await Tetris.loadSQL();return false}catch{return true}}') is True
    assert page.evaluate('Tetris.captureExport().formatVersion')==1
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    assert page.evaluate('Tetris.ui.game.status')=='running'
    page.unroute(info['url'])
    body=(ROOT/'.test-artifacts/sqljs-inline.js').read_bytes()
    page.route(info['url'],lambda route:route.fulfill(status=200,body=body,content_type='application/javascript',headers={'access-control-allow-origin':'*'}))
    assert page.evaluate('async()=>{const SQL=await Tetris.loadSQL(),db=new SQL.Database();try{return db.exec("SELECT 7")[0].values[0][0]}finally{db.close()}}')==7


def test_extreme_score_remains_inside_panels(page):
    page.evaluate("Tetris.ui.results.replace([{id:'maximum',score:Number.MAX_SAFE_INTEGER,timestamp:'2026-10-30T00:00:00.000Z'}]);Tetris.ui.game.score=Number.MAX_SAFE_INTEGER;Tetris.render()")
    assert page.locator('#results li').evaluate('(el)=>el.scrollWidth<=el.clientWidth')


def test_lifecycle_announcements_and_disabled_help(page):
    assert page.locator('#state').get_attribute('aria-live')=='polite'
    page.get_by_role('button',name='Start/Restart',exact=True).click()
    page.keyboard.press('Escape')
    assert page.locator('#state').text_content()=='Paused'
    page.get_by_label('Hold piece',exact=True).select_option('false')
    page.get_by_label('Hard drop',exact=True).select_option('false')
    assert 'off' in page.locator('#help-hold').inner_text()
    assert 'off' in page.locator('#help-hardDrop').inner_text()
    page.get_by_label('Hold piece',exact=True).select_option('true')
    assert 'off' not in page.locator('#help-hold').inner_text()


def test_packaged_json_transfer_without_network(browser):
    import json,re,subprocess,sys
    root=Path(__file__).resolve().parents[1]
    subprocess.run([sys.executable,'tools/package.py'],cwd=root,check=True,capture_output=True)
    version=re.search(r"const VERSION\s*=\s*'([^']+)'",(root/'index.html').read_text()).group(1)
    context=browser.new_context(accept_downloads=True)
    p=context.new_page()
    p.route('https://**',lambda route:route.abort())
    p.set_default_timeout(5000)
    try:
        p.goto((root/'dist'/version/('tetris-v'+version+'.html')).as_uri())
        assert p.evaluate('typeof Tetris')=='undefined'
        data={'formatVersion':1,'results':[{'id':'offline-stable','score':123,'timestamp':'2026-10-30T00:00:00.000Z'}],'settings':{'ghost':'dynamic','hardDrop':False,'nextPreview':True,'hardDropLock':'immediate','lockPolicy':'interval','hold':False}}
        previous={**data,'results':[{'id':'old','score':999,'timestamp':'2026-10-30T00:00:00.000Z'}]}
        p.locator('#restore-input').set_input_files({'name':'previous.json','mimeType':'application/json','buffer':json.dumps(previous).encode()})
        p.wait_for_function("document.querySelector('#results')?.textContent.includes('999')")
        p.locator('#restore-input').set_input_files({'name':'session.json','mimeType':'application/json','buffer':json.dumps(data).encode()})
        p.wait_for_function("document.querySelector('#results')?.textContent.includes('123')")
        assert p.locator('#results li').count()==1
        assert '123' in p.locator('#results').inner_text()
        assert p.get_by_label('Hold piece',exact=True).input_value()=='false'
        with p.expect_download() as received:
            p.get_by_role('button',name='Save',exact=True).click()
        assert json.loads(Path(received.value.path()).read_text())==data
    finally:
        context.close()
