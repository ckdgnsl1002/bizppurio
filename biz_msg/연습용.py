import requests
import base64

def test_req():
    resp = requests.get('https://www.naver.com/')
    print(resp)
    print(resp.status_code)
    print(resp.text[:100])
    return resp
    
    
a = test_req()

print(len(a.text))

test_id = 'lookin4u_dev:wearelk4u!'

print(test_id.encode('utf-8f'))