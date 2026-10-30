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
