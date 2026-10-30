def test_legal_geometry_and_collision(js):
    assert js("valid(emptyBoard(),'T',0,3,0)") is True
    assert js("cells('I',0,3,0)") == [[3,1],[4,1],[5,1],[6,1]]
    assert js("valid(emptyBoard(),'I',0,8,0)") is False
    assert js("(()=>{const b=emptyBoard();b[1][4]='J';return valid(b,'T',0,3,0)})()") is False
    assert js("(()=>{const p={type:'T',rot:0,x:0,y:0};return transform(emptyBoard(),p,-1,0,0).x})()") == 0

def test_gravity_lock_clear_and_scoring(js):
    assert js("typeof Game==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.lines=6;g.p={type:'I',rot:1,x:3,y:16};for(let y=16;y<20;y++)g.board[y]=Array.from({length:10},(_,x)=>x===5?0:'J');g.lock();return [g.score,g.lines,g.level,g.board.flat().filter(Boolean).length]})()") == [800,10,2,0]
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:18};g.tick(999);const a=g.board.flat().filter(Boolean).length;g.tick(1);return [a,g.board.flat().filter(Boolean).length,g.status]})()") == [0,4,'running']
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.board[0][4]='I';g.spawn('O');g.finish();return [g.status,g.events.length]})()") == ['over',1]
