import requests, re

def GenerateToken(cookie:str, app:str):
    r    = requests.Session()
    req1 = r.get('https://graph.facebook.com/v16.0/device/login?method=POST&access_token={}'.format(app)).json()
    req2 = r.get('https://mbasic.facebook.com/device', cookies={'cookie':cookie}).text.replace('\\','')
    dat1 = {'fb_dtsg':re.search(r'name="fb_dtsg" value="(.*?)"',str(req2)).group(1), 'jazoest':re.search(r'name="jazoest" value="(.*?)"',str(req2)).group(1), 'qr':re.search(r'name="qr" value="(.*?)"',str(req2)).group(1), 'user_code':req1.get('user_code')}
    pos1 = r.post('https://mobile.facebook.com{}'.format(re.search(r'form method="post" action="(.*?)"',str(req2)).group(1)), data=dat1, cookies={'cookie':cookie}).text.replace('\\','')
    dat2 = {'fb_dtsg':re.search(r'name="fb_dtsg" value="(.*?)"',str(pos1)).group(1), 'jazoest':re.search(r'name="jazoest" value="(.*?)"',str(pos1)).group(1), 'scope':re.search(r'name="scope" value="(.*?)"',str(pos1)).group(1), 'display':re.search(r'name="display" value="(.*?)"',str(pos1)).group(1), 'sdk':'', 'sdk_version':'', 'domain':'', 'sso_device':'', 'state':'', 'user_code':re.search(r'name="user_code" value="(.*?)"',str(pos1)).group(1), 'logger_id':re.search(r'name="logger_id" value="(.*?)"',str(pos1)).group(1), 'auth_type':re.search(r'name="auth_type" value="(.*?)"',str(pos1)).group(1), 'auth_nonce':'', 'code_challenge"':'', 'code_challenge_method':'', 'encrypted_post_body':re.search(r'name="encrypted_post_body" value="(.*?)"',str(pos1)).group(1), 'return_format[]':re.search(r'name="return_format\[\]" value="(.*?)"',str(pos1)).group(1)}
    pos2 = r.post('https://mobile.facebook.com{}'.format(re.search(r'form method="post" action="(.*?)"',str(pos1)).group(1)), data=dat2, cookies={'cookie':cookie}).text.replace('\\','')
    tok  = r.get('https://graph.facebook.com/v16.0/device/login_status?method=post&code={}&access_token={}'.format(req1.get('code'), app), cookies={'cookie':cookie}).json().get('access_token')
    r.close()
    return(tok)

cookie    = 'Input Your Cookie Here'
TokenEAAT = GenerateToken(cookie=cookie, app='1348564698517390|007c0a9101b9e1c8ffab727666805038')
TokenEAAQ = GenerateToken(cookie=cookie, app='1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9')

print(TokenEAAT)
print(TokenEAAQ)

# 1348564698517390|007c0a9101b9e1c8ffab727666805038 - Meta Portal
# 1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9 - Messenger Kids for iOS

# Dump Name : https://graph.facebook.com/100000198243102?fields=friends.fields(id,name)&limit=5000&access_token=EAAT...