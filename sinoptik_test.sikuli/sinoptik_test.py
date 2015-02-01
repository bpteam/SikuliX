try:
    firefox = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    url = 'https://sinoptik.ua'
    openApp(firefox)
    if bool(exists("1422816842381.png",4)) != True:
        raise Exception('Can`t run browser')
    click("1422818832742.png")
    type(url + Key.ENTER)
    if bool(exists(Pattern("1422821974735.png").similar(0.95),50)) != True:
        raise Exception('Can`t load page ' + url)
    click('1422822266010.png')
    type('Kie')
    if bool(exists(Pattern("search.png").similar(0.90),50)):
        popup('WORK')
    else:
        popup('ERROR!!!')
except Exception, e:
    popup(e)
