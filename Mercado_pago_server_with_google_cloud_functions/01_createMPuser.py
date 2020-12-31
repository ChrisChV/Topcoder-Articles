import requests
import json
import sys
import os

ENTRY_POINT = "https://api.mercadopago.com/v1/customers?access_token="

EMAIL = 'email'
NAME = 'first_name'
MP_ID = 'id'

def createMPuser(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '36000'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    try:    
        request_args = request.get_json(silent = True)
        if verifyJson(request_args):
            email = request_args[EMAIL]
            name = request_args[NAME].split(' ')[0]

            url = ENTRY_POINT + os.environ.get('ACCESS_TOKEN', 'Invalid Token')
            postData = {
                'email': email,
                'firstName': name,
            }
            response = requests.post(url, json=postData)
            resData = json.loads(response.text)
            
            # Here you can save the mercado pago user id in your data base
            # write(resData[MP_ID])

            return (resData[MP_ID], 200, headers)
        else:
            return ("Malformed JSON", 400, headers)
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        return ("Error", 400, headers)


def verifyJson(request_args):
    if request_args and EMAIL in request_args \
        and NAME in request_args:
        return True
    return False
    




