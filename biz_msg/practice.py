import requests
import base64
import ssl
# Create your views here.
ssl._create_default_https_context = ssl._create_unverified_context

def test_req():
    resp = requests.get('https://www.naver.com/')
    print(resp)
    print(resp.status_code)
    print(resp.text[:100])
    return resp

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
    
a = test_req()

print(len(a.text))



a = get_token()
print(a)
print(a.request.headers)
print(a.text)