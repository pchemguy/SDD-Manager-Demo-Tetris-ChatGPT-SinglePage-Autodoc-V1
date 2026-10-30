

def test_complete_setting_domains(js):
    assert js("typeof normaliseSettings==='undefined'?null:Object.keys(normaliseSettings({...DEFAULTS})).length") == 6
    assert js("typeof normaliseSettings==='undefined'?null:(()=>{try{normaliseSettings({...DEFAULTS,hold:'on'});return false}catch{return true}})()") is True
    assert js("typeof DEFAULTS==='undefined'?null:[DEFAULTS.ghost,DEFAULTS.hardDrop,DEFAULTS.lockPolicy]") == ['show',True,'interval']


def test_live_settings_preserve_and_replace_deadlines(js):
    assert js("typeof Game.prototype.applySettings==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:18};g.tick(200);g.applySettings({...DEFAULTS,hardDrop:false});const kept=g.deadline;g.applySettings({...DEFAULTS,lockPolicy:'failed'});const cleared=g.deadline;g.applySettings({...DEFAULTS});return [kept,cleared,g.deadline]})()") == [1000,None,1200]
    assert js("typeof Game.prototype.applySettings==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.applySettings({...DEFAULTS,hardDrop:false,hold:false});const p=JSON.stringify(g.p);g.hardDrop();g.holdPiece();return JSON.stringify(g.p)===p})()") is True
