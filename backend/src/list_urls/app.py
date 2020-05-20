import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb')
table = client.Table(os.getenv('DYNAMODB_TABLE'))

def index(event, context):
    response = table.scan(
        FilterExpression=Key('type').eq('short-url'),
        ProjectionExpression='link, pk',
        )

    data = []
    for item in response['Items']:
        data.append({
            'url': item.get('link'),
            'short_code': item.get('pk')
        })

    return {
        "statusCode": 200,
        "body": json.dumps(data),
    }
