
import boto3

dynamodb = boto3.resource('dynamodb')

def insert_data(a,b,op, c):
    table = dynamodb.Table('operation')
    table.put_item(Item={
                'variableA': str(a),
                'variableB': str(b),
                'operation': op,
                'result': str(c)
            })