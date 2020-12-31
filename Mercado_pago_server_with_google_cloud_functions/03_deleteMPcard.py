import requests
import os
import sys

BASE_ENTRY_POINT = 'https://api.mercadopago.com/v1/customers/'
CARD_ENTRY_POINT = '/cards/'
AC_ENTRY_POINT = '?access_token='
CUSTOMER_ID = 'customerId'
CARD_ID = 'cardId'

SUCCESS_STATUS_CODE = 201
SECOND_SUCCES_STATUS_CODE = 200

def deleteMPcard(request):
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
            cardId = request_args[CARD_ID]
            accessToken = os.environ.get('ACCESS_TOKEN', 'Invalid Token')
            url = BASE_ENTRY_POINT + customerId + CARD_ENTRY_POINT + cardId + AC_ENTRY_POINT + accessToken
            response = requests.delete(url)
            if response.status_code == SUCCESS_STATUS_CODE \
                or response.status_code == SECOND_SUCCES_STATUS_CODE:
                return ("", 200, headers)
            return ("Error", response.status_code, headers)
        else:
            return ("Malformed JSON", 400, headers)
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        return ("Error", 400, headers)


def verifyJson(request_args):
    if request_args and CUSTOMER_ID in request_args \
        and CARD_ID in request_args:
        return True
    return False