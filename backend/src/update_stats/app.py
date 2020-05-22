import json
import boto3
import os

client = boto3.resource('dynamodb')
table = client.Table(os.getenv('DYNAMODB_TABLE'))

def index(event, context):
    data = json.loads(event['Records'][0]['Sns']['Message'])

    input = {
        'pk': 'stat#' + data['id'],
        'timestamp': data['timestamp'],
        'type': 'stat',
        'resource_value': data['id']
    }
    result = table.put_item(Item=input)
