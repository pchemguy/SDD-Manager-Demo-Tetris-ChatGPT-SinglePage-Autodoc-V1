"""Acceptance checks against the actual single-file application and isolated runtimes."""


def test_complete_setting_domains(js):
    assert js("typeof normaliseSettings==='undefined'?null:Object.keys(normaliseSettings({...DEFAULTS})).length") == 6
    assert js("typeof normaliseSettings==='undefined'?null:(()=>{try{normaliseSettings({...DEFAULTS,hold:'on'});return false}catch{return true}})()") is True
    assert js("typeof DEFAULTS==='undefined'?null:[DEFAULTS.ghost,DEFAULTS.hardDrop,DEFAULTS.lockPolicy]") == ['show',True,'interval']


def test_live_settings_preserve_and_replace_deadlines(js):
    assert js("typeof Game.prototype.applySettings==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.p={type:'O',rot:0,x:4,y:18};g.tick(200);g.applySettings({...DEFAULTS,hardDrop:false});const kept=g.deadline;g.applySettings({...DEFAULTS,lockPolicy:'failed'});const cleared=g.deadline;g.applySettings({...DEFAULTS});return [kept,cleared,g.deadline]})()") == [1000,None,1200]
    assert js("typeof Game.prototype.applySettings==='undefined'?null:(()=>{const g=new Game(()=>0.5);g.start();g.applySettings({...DEFAULTS,hardDrop:false,hold:false});const p=JSON.stringify(g.p);g.hardDrop();g.holdPiece();return JSON.stringify(g.p)===p})()") is True


def test_independent_configuration_sources(js):
    assert js("typeof resolveSettings==='undefined'?null:(()=>{const r=resolveSettings('https://local.test/?ghost=show&nextPreview=off&hold=INVALID&hold=on','tetris_ghost=hide; tetris_hardDrop=off; tetris_hold=off');return [r.settings.ghost,r.settings.hardDrop,r.settings.nextPreview,r.settings.hold,r.explicit.ghost]})()") == ['show',False,False,False,'show']
    assert js("typeof resolveSettings==='undefined'?null:resolveSettings('https://local.test/','tetris_ghost=dynamic').settings.ghost") == 'dynamic'


def test_configuration_spellings(js):
    assert js("SETTING_DEFS.map(d=>serializeSetting(d.key,DEFAULTS[d.key]))") == ['show','on','on','general','interval','on']
    assert js("SETTING_DEFS.map(d=>parseSetting(d.key,serializeSetting(d.key,DEFAULTS[d.key])))") == ['show',True,True,'general','interval',True]


def test_query_update_preserves_unrelated_values(js):
    assert js("typeof updatedURL==='undefined'?null:(()=>{const u=new URL(updatedURL('https://local.test/?keep=1#frag',{...DEFAULTS,hardDrop:false},['hardDrop']));return [u.searchParams.get('keep'),u.searchParams.get('hardDrop'),u.hash]})()") == ['1','off','#frag']


def test_session_ranking_and_stable_completion(js):
    assert js("typeof SessionResults==='undefined'?null:(()=>{const s=new SessionResults(()=> 'stable',()=> '2026-10-30T00:00:00.000Z');s.complete({generation:1,score:0});s.complete({generation:1,score:999});s.complete({generation:2,score:500});return [s.records.length,s.records[0].score,s.records[1].id]})()") == [2,500,'stable']
    assert js("typeof rankResults==='undefined'?null:rankResults(Array.from({length:12},(_,i)=>({id:'g'+i,score:i,timestamp:'2026-10-30T00:00:00.000Z'}))).map(r=>r.score)") == [11,10,9,8,7,6,5,4,3,2]


def test_complete_export_validation(js):
    assert js("typeof validateExport==='undefined'?null:(()=>{const v=validateExport(({formatVersion:1,results:[{id:'a',score:0,timestamp:'2026-10-30T00:00:00.000Z'}],settings:{...DEFAULTS}}));return [v.formatVersion,v.results[0].score,Object.keys(v.settings).length]})()") == [1,0,6]


def test_export_rejects_complete_invalid_candidates(js):
    assert js("(()=>{const good=()=>({formatVersion:1,results:[{id:'a',score:0,timestamp:'2026-10-30T00:00:00.000Z'}],settings:{...DEFAULTS}});return [v=>v.formatVersion=2,v=>v.extra=1,v=>v.results[0].score=-1,v=>v.results[0].score=1.5,v=>v.results[0].score=9007199254740992,v=>v.results[0].timestamp='2025-02-29T00:00:00.000Z',v=>v.results[0].timestamp='2026-10-30T00:00:00Z',v=>v.results.push({...v.results[0]}),v=>delete v.settings.hold,v=>v.settings.hold='on',v=>v.settings.unknown=true].every(change=>{const v=good();change(v);try{validateExport(v);return false}catch{return true}})})()") is True


def test_duplicate_members_and_exact_json_numbers(js):
    assert js('(()=>{const base=JSON.stringify({formatVersion:1,results:[{id:\'a\',score:0,timestamp:\'2026-10-30T00:00:00.000Z\'}],settings:{...DEFAULTS}});const bad=[base.replace(\'\\"formatVersion\\":1\',\'\\"formatVersion\\":1,\\"formatVersion\\":1\'),base.replace(\'\\"score\\":0\',\'\\"score\\":9007199254740991.1\'),base.replace(\'\\"score\\":0\',\'\\"score\\":1e-400\')];return bad.every(text=>{try{parseExportJSON(text);return false}catch{return true}})})()') is True
