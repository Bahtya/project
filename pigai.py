import requests

login_url='http://open.pigai.org/?c=api&a=sentbase&action=login&key=SE9mpdwTPxyKGUvJb9vrVfYlwX803YcH&type=json&pigaimobile=1&pigaiversion=1.4.4&uid=13312451&token=600f8005baa69bc14a1e80de1664093c'
headers = {
        'Content-Length': '326',
        'Accept': 'application/json',
        'Origin': 'file://',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
}

data = {'''
        'c':'api',
        'a':'sentbase',
        'action':'login',
        'key':'SE9mpdwTPxyKGUvJb9vrVfYlwX803YcH',
        'type':'json',
        'pigaimobile':'1',
        'pigaiversion':'1.4.4',
        'uid':'13312451',
        'token':'b6fd89abcda87dc77293e701bb69f27e',
        '''
        
        'name':'刘威',
        'email':'18699450605',
        'psw':'ailw1314.',
        'channel':'',
        'MB_time':'1551877327',
        'MB_version':'1.4.4',
        'MB_os[android]':'true',
        'MB_os[version]':'7.1.1',
        'MB_os[isBadAndroid]':'false',
        'MB_os[plus]':'true',
        'MB_uuid':'864166039376763,864166039376771',
        'MB_cid':'905ce29dbbc0ff14fab1ca7ea4469ab1',
        'MB_token':'905ce29dbbc0ff14fab1ca7ea4469ab1',
        'MB_wid':'org.pigai.allround'
}

urls = 'http://open.pigai.org/?c=api&a=essaylistbyuid'

def login():
    session=requests.session()
    r=session.post(login_url,headers=headers,data=data)
    result=r.json()
    if result['data'] !='':
        print('登陆成功')
        
    else:
        print('登陆失败')

if __name__ == '__main__' :
    login()
