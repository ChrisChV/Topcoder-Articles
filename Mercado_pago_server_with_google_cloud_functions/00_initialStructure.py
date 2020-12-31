import json
import sys

def nameOfFunction(request):
    # Part 1
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
        # Part 2
        request_args = request.get_json(silent = True)
        if verifyJson(request_args):
            pass
            # Part 3
            # The logic of the function here
        else:
            return ("Malformed JSON", 400, headers)
    except:
        # Part 4
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        return ("Error", 400, headers)

def verifyJson(request_args):
    # Part 5
    # Function to verify the arguments of the function    
    return True
