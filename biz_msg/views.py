from django.shortcuts import render
import base64
import requests
# Create your views here.


def get_token():
    dev_id_pw = 'lookin4u_dev:wearelk4u!'
    encoded_id_pw = base64.b64encode(dev_id_pw.encode('utf-8'))
    
    headers = {
        'Authorization' : 'Basic' + ' ' + str(encoded_id_pw),
        'Content-Type' : 'application/json; charset=utf8'
    }
    
    url = 'https://api.bizppurio.com/v1/token'
    
    return requests.post(url, headers=headers, timeout=10)


def request_token(request):
    try:
        response = get_token()
        context = {
            'response' : response,
            'status_code' : response.status_code,
            'response_json' : response.json()
        }
        
        return render(request, 'biz_msg/response.html', context)
    except:
        error_message = 'Error occured'
        return render(request, 'biz_msg/response.html', context={'error' : error_message})
    