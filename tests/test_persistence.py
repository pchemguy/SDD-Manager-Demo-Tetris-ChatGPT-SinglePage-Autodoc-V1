

def test_complete_setting_domains(js):
    assert js("typeof normaliseSettings==='undefined'?null:Object.keys(normaliseSettings({...DEFAULTS})).length") == 6
    assert js("typeof normaliseSettings==='undefined'?null:(()=>{try{normaliseSettings({...DEFAULTS,hold:'on'});return false}catch{return true}})()") is True
    assert js("typeof DEFAULTS==='undefined'?null:[DEFAULTS.ghost,DEFAULTS.hardDrop,DEFAULTS.lockPolicy]") == ['show',True,'interval']
