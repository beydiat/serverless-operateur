import json
from libs.dynamodb_lib import get_list


def list_table(event, context):
    result = get_list()
    print(f"**Result > list_table return : {result}")
    response = {
        "statusCode": 200,
        "body": str(result)
    }
    return response