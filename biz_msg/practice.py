import requests
import base64
import ssl
import json
# Create your views here.
ssl._create_default_https_context = ssl._create_unverified_context

def get_token():
    dev_id = 'lookin4u_dev'
    dev_pw = 'wearelk4u!'
    # encoded_id_pw = base64.b64encode(dev_id_pw.encode('utf-8')).decode('ascii')
    encoded_id_pw = base64.b64encode("{}:{}".format(dev_id, dev_pw).encode('utf-8')).decode('ascii')
    headers = {
        'Authorization' : 'Basic {}'.format(encoded_id_pw),
        'Content-type' : 'application/json; charset=utf-8',
    }
    
    url = 'https://api.bizppurio.com/v1/token'
    session = requests.Session()
    # session.verify=False
    # return requests.post(url, headers=headers)
    return session.post(url, headers=headers)


def send_FT():
    token_request = get_token()
    
    print(token_request)
    print(token_request.text)
    
    access_token = json.loads(token_request.text)['accesstoken']
    token_type = json.loads(token_request.text)['type']
    
    sender_key = '6124f5ac566eab918092388e75a4ef89e78a9515'
    
    headers = {
        'Authorization' : '{} {}'.format(token_type, access_token),
        'Content-type' : 'application/json; charset=utf-8',
    }
    
    body_sms={
        "account" : 'lookin4u_dev',
        "refkey" : 'BJUom4GftTE4',
        'type' : 'sms',
        'from' : '01095106419',
        'to' : '01095106419',
        'content' : {
            'sms':{
                "message" : '안녕 원명아! 지금 내 핸드폰번호로 발신하게 설정해보았어. 이 메세지가 너에게 닿길 바래.'
            }
        }
    }
    
    body_ft={
        "account" : 'lookin4u_dev',
        "refkey" : 'BJUom4GftTE4',
        'type' : 'ft',
        'from' : '01095106419',
        'to' : '01095106419',
        'content' : {
            'ft':{
                'senderkey' : sender_key,
                "message" : '안녕 원명아! 지금 내 핸드폰번호로 발신하게 설정해보았어. 이 메세지가 너에게 닿길 바래.',
                'image':{
                    'img_url' : 'http://street-together.kro.kr/media/blog/images/2021/10/06/53DF48C5-BCC0-4D66-8AC6-5BC147094A57.jpeg',
                    'img_link' : 'http://street-together.kro.kr/'
                },
                'button':[{
                    'name' : '테스트!!',
                    'type' : "WL",
                    'url_mobile' : 'http://street-together.kro.kr/',
                    'url_pc' : 'https://www.naver.com/'
                }]
            }
        }
    }
    
    url = 'https://api.bizppurio.com/v3/message'
    session = requests.Session()
    # session.verify=False
    # return requests.post(url, headers=headers)
    return session.post(url, headers=headers, data=json.dumps(body_ft))


send_complete = send_FT()

print(send_complete)
print(send_complete.text)