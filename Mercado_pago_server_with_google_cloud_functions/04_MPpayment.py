import requests
import sys

ENTRY_POINT = "https://api.mercadopago.com/v1/payments?access_token="

CUSTOMER_ID = 'customerId'
CUSTOMER_EMAIL = 'email'
CARD_TOKEN = 'cardToken'
MOUNT = 'mount'
PAYMENT_METHOD = 'method'
DESCRIPTION = 'description'
INSTALLMENTS = 'installments'

SUCCESS_STATUS_CODE = 201


def MPpayment(request):
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
            email = request_args[CUSTOMER_EMAIL]
            cardToken = request_args[CARD_TOKEN]
            mount = round(request_args[MOUNT],2)
            paymentMethod = request_args[PAYMENT_METHOD]
            description = 'Mercado Pago payment'
            installments = 1
            if DESCRIPTION in request_args:
                description = request_args[DESCRIPTION]
            if INSTALLMENTS in request_args:
                installments = request_args[INSTALLMENTS]
            url = ENTRY_POINT + os.environ.get('ACCESS_TOKEN', 'Invalid Token')
            postData = {
                'token': cardToken,
                'transaction_amount': mount,
                'description': description,
                'installments': installments,
                'payment_method_id': paymentMethod,
                'binary_mode': True,
                'payer': {
                    'id': customerId,
                    'email': email,
                },
            }
            response = requests.post(url, json=postData)
            
            if response.status_code != SUCCESS_STATUS_CODE:

                # Here you can add the logic of an error in the payments

                return ("Error", response.status_code, headers)

            # Here you can add the login of a success payment
            

            return (response.text, 200, headers)
            
        else:
            return ("Malformed JSON", 401, headers)
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        return ("Error", 400, headers)

def verifyJson(request_args):
    if request_args and CUSTOMER_ID in request_args and CARD_TOKEN in request_args \
        and MOUNT in request_args and PAYMENT_METHOD in request_args \
        and CUSTOMER_EMAIL in request_args:
        return True
    return False
