def test_legal_geometry_and_collision(js):
    assert js("valid(emptyBoard(),'T',0,3,0)") is True
    assert js("cells('I',0,3,0)") == [[3,1],[4,1],[5,1],[6,1]]
    assert js("valid(emptyBoard(),'I',0,8,0)") is False
    assert js("(()=>{const b=emptyBoard();b[1][4]='J';return valid(b,'T',0,3,0)})()") is False
    assert js("(()=>{const p={type:'T',rot:0,x:0,y:0};return transform(emptyBoard(),p,-1,0,0).x})()") == 0
