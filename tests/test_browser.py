from pathlib import Path

def test_board_information_and_render(page):
    assert page.locator('#board').count() == 1
    assert page.get_by_role('button', name='Start/Restart', exact=True).count() == 1
    assert page.get_by_role('button', name='Pause/Start', exact=True).count() == 1
    assert page.locator('#board').evaluate("c=>c.getContext('2d').getImageData(20,20,1,1).data[3]") == 255
    assert page.locator('#score').inner_text() == '0'
    box = page.locator('#board').bounding_box()
    assert abs(box['x'] + box['width']/2 - 720) < 2
