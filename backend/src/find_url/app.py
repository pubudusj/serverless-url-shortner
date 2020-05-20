import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb')
table = client.Table(os.getenv('DYNAMODB_TABLE'))

def index(event, context):
    pathData = event['path'];
    short_code = pathData.split('/')[-1]
    
    response = table.query(
        Select='SPECIFIC_ATTRIBUTES',
        KeyConditionExpression=Key('pk').eq(short_code),
        ProjectionExpression='link',
        )
    if (response['Items']):        
        return {
            "statusCode": 301,
            "headers": {
                "Location": response['Items'][0]['link']
            }
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({
                'message': 'Short url not found',
            }),
        }
