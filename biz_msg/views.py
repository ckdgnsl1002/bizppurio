from django.shortcuts import render
import base64
import requests
# Create your views here.


def get_token():
    dev_id_pw = 'lookin4u_dev:wearelk4u!'
    encoded_id_pw = base64.b64encode(dev_id_pw.encode('utf-8'))
    
    headers = {
        'Authorization' : 'Basic' + ' ' + str(encoded_id_pw),
        'Content-type' : 'application/json; charset=utf-8',
    }
    
    url = 'https://dev-api.bizppurio.com/v1/token'
    session = requests.Session()
    
    return session.post(url, headers=headers)


def request_token(request):
    response = get_token()
    print(response)
    context = {
        'response' : response,
        'status_code' : response.status_code,
        'response_json' : response.json()
    }
    
    return render(request, 'biz_msg/response.html', context)
    # except:
    #     error_message = 'Error occured'
    #     return render(request, 'biz_msg/response.html', context={'error' : error_message})
    