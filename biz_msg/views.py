from django.shortcuts import render
import base64
import requests
import ssl
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


def request_token(request):
    response = get_token()
    print(response)
    context = {
        'response' : response,
        'status_code' : response.status_code,
        'text' : response.text,
        'headers' : response.request.headers,
        'response_json' : response.json()
    }
    
    return render(request, 'biz_msg/response.html', context)
    # except:
    #     error_message = 'Error occured'
    #     return render(request, 'biz_msg/response.html', context={'error' : error_message})
    