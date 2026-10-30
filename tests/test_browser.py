from pathlib import Path

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
    assert page.locator('#settings select').count() == 6
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
