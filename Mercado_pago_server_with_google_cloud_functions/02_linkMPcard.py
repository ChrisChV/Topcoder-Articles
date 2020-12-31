import requests
import sys
import os

BASE_ENTRY_POINT = "https://api.mercadopago.com/v1/customers/"
CARD_ENTRY_POINT = "/cards?access_token="

CUSTOMER_ID = 'customerId'
CARD_TOKEN = 'cardToken'
MP_CARD_TOKEN = 'token'

SUCCESS_STATUS_CODE = 201
ALREADY_EXISTS_CODE = 200

def linkMPcard(request):
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
            customerId = request_args[CUSTOMER_ID]
            cardToken = request_args[CARD_TOKEN]
            accessToken = os.environ.get('ACCESS_TOKEN', 'Invalid Token')
            url = BASE_ENTRY_POINT + customerId + CARD_ENTRY_POINT + accessToken
            data = {
                MP_CARD_TOKEN: cardToken
            }
            response = requests.post(url, json=data)
            resData = response.json()
            if response.status_code == SUCCESS_STATUS_CODE or \
                response.status_code == ALREADY_EXISTS_CODE:
                return(response.text , 200, headers)
            return("Error", response.status_code, headers)
        else:
            return ("Malformed JSON", 401, headers)
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        return ("Error", 400, headers)


def verifyJson(request_args):
    if request_args and CUSTOMER_ID in request_args \
        and CARD_TOKEN in request_args:
        return True
    return False