import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key, Attr

client = boto3.resource('dynamodb')
table = client.Table(os.getenv('DYNAMODB_TABLE'))

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def index(event, context):
    response = table.scan(
        FilterExpression=Key('type').eq('short-url'),
        )

    data = []
    for item in response['Items']:        data.append({
            'url': item.get('url'),
            'short_code': item.get('pk')
        })

    return {
        "statusCode": 200,
        "body": json.dumps(data),
    }
