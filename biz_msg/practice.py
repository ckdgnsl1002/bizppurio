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
    
    url = 'https://dev-api.bizppurio.com/v1/token'
    session = requests.Session()
    session.verify=False
    # return requests.post(url, headers=headers)
    return session.post(url, headers=headers)


def send_FT():
    token_request = get_token()
    
    print(token_request)
    print(token_request.text)
    
    access_token = json.loads(token_request.text)['access_token']
    token_type = json.loads(token_request.text)['type']
    
    sender_key = '6124f5ac566eab918092388e75a4ef89e78a9515'
    
    headers = {
        'Authorization' : '{} {}'.format(token_type, access_token),
        'Content-type' : 'application/json; charset=utf-8',
    }
    
    body={
        "account" : 'lookin4u_dev',
        "refkey" : 'test1234',
        'type' : 'sms',
        'from' : '01095106419',
        'to' : '01064509159',
        'content' : {
            'sms':{
                "message" : '안녕 원명아! 지금 내 핸드폰번호로 발신하게 설정해보았어. 이 메세지가 너에게 닿길 바래.'
            }
        }
    }
    
    url = 'https://dev-api.bizppurio.com/v3/message'
    session = requests.Session()
    session.verify=False
    # return requests.post(url, headers=headers)
    return session.post(url, headers=headers, data=json.dumps(body))


send_complete = send_FT()

print(send_complete)
print(send_complete.text)