import requests

def test_req():
    resp = requests.get('https://www.naver.com/')
    print(resp)
    print(resp.status_code)
    print(resp.text[:100])
    return resp
    
    
a = test_req()

print(len(a.text))