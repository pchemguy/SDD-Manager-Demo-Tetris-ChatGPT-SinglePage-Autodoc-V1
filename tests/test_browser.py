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
