import json
from libs.dynamodb_lib import insert_data

def addition(event, context):
    body = json.loads(event.get('body'))
    operation = "addition"
    print(f'**Inputs > {operation}  event body : {body}')
    
    a = body['a']
    b = body['b']
    result = a+b
    body = {
        "a":a,
        "b":b,
        "resultat": result
    }
    print(f"**Result > {operation} return : {body}")
    insert_data(a, b, operation, result)
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
