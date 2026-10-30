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

def test_pause_freezes_clock_and_restart_replaces_game(js):
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.tick(500);g.pause?.();g.tick(5000);return [g.status,g.elapsed,g.p.y]})()") == ['paused',500,0]
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.tick(500);g.pause();g.tick(9000);g.pause();g.tick(500);const y=g.p.y;g.score=100;g.start();return [y,g.score,g.lines,g.level,g.p.y,g.status]})()") == [1,0,0,1,0,'running']


def test_seven_bag_and_preview_order(js):
    assert js("(()=>{const g=new Game(()=>0.5);const a=Array.from({length:14},()=>g.draw());return [new Set(a.slice(0,7)).size,new Set(a.slice(7)).size]})()") == [7,7]
    assert js("typeof Game.prototype.next==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();const next=g.queue[0];g.p.y=16;g.lock();return [g.p.type===next,g.queue.length]})()") == [True,1]


def test_hold_swap_and_turn_limit(js):
    assert js("typeof Game.prototype.holdPiece==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();const a=g.p.type,b=g.queue[0];g.holdPiece();const first=[g.held===a,g.p.type===b];g.holdPiece();const limited=g.held===a;g.p.y=16;g.lock();const q=g.queue[0];g.holdPiece();return [...first,limited,g.p.type===a,g.queue[0]===q]})()") == [True,True,True,True,True]


def test_wall_and_floor_kicks(js):
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'T',rot:1,x:-1,y:4};g.act(0,0,-1);return [g.p.rot,g.p.x]})()") == [0,0]
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'I',rot:1,x:-2,y:4};g.act(0,0,-1);return [g.p.rot,g.p.x]})()") == [0,0]
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'T',rot:0,x:3,y:18};g.act(0,0,1);return [g.p.rot,g.p.x,g.p.y]})()") == [1,2,17]


def test_shared_normal_landing(js):
    assert js("typeof findLanding==='undefined'?null:(()=>{const b=emptyBoard();b[10][3]='J';return findLanding(b,{type:'I',rot:0,x:3,y:0}).y})()") == 8
    assert js("typeof findLanding==='undefined'?null:findLanding(emptyBoard(),{type:'O',rot:0,x:4,y:0}).y") == 18


def test_hard_drop_lands_and_scores(js):
    assert js("typeof Game.prototype.hardDrop==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.config={lockPolicy:'failed',hardDropLock:'general'};g.p={type:'O',rot:0,x:4,y:0};const p=g.landing();g.hardDrop();return [g.score,cells('O',0,p.x,p.y).every(([x,y])=>g.board[y][x]==='O')]})()") == [36,True]


def test_interval_grounding_and_immediate_drop(js):
    assert js("(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:18};g.tick(300);g.act(-1);g.tick(699);const before=g.board.flat().filter(Boolean).length;g.tick(1);return [before,g.board.flat().filter(Boolean).length]})()") == [0,4]
    assert js("typeof Game.prototype.syncGround==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:17};g.board[19][4]='J';g.syncGround();g.tick(400);g.act(1);const lifted=g.deadline===null;g.tick(100);g.act(-1);return [lifted,g.deadline]})()") == [True,1500]
    assert js("typeof Game.prototype.syncGround==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:0};g.hardDrop();g.tick(400);const a=g.score;g.hardDrop();const deadline=g.deadline;g.tick(600);return [a,g.score,deadline,g.board.flat().filter(Boolean).length]})()") == [36,36,1000,4]
