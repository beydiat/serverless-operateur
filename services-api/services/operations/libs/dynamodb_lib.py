
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dev-OperationTableArn')

def insert_data(a,b,op, c):
    
    table.put_item(Item={
                'variableA': str(a),
                'variableB': str(b),
                'operation': op,
                'result': c
            })


def get_list():
    return table.scan()