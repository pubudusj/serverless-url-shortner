import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb')
table = client.Table(os.getenv('DYNAMODB_TABLE'))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def index(event, context):
    print(event)
    pathData = event['path'];
    short_code = pathData.split('/')[-1]

    print(event['pathParameters']['code'])

    response = table.scan(
        FilterExpression=Key('pk').begins_with('stat#' + short_code) | Key('pk').begins_with('counter#' + short_code),
        ProjectionExpression='#resource_type, #created_timestamp, visit_count',
        ExpressionAttributeNames={
            '#created_timestamp': 'timestamp',
            '#resource_type': 'type'
        }
    )

    stats = []
    total_count = 0
    for item in response['Items']:
        if (item.get('type') === 'counter'):
            totalCount = item.get('visit_count')
        else:
            stats.append({
                'type': item.get('type'),
                'timestamp': item.get('timestamp'),
            })

    return {
        "statusCode": 200,
        "body": json.dumps({ 'stats': stats, 'total_count': total_count }, cls=DecimalEncoder),
        "headers": {
            'Content-Type': 'application/json', 
            'Access-Control-Allow-Origin': '*'
        }
    }
