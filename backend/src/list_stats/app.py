import json
import boto3
import os
import decimal
from boto3.dynamodb.conditions import Key
import datetime

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
    pathData = event['path'];
    short_code = event['pathParameters']['code']

    response = table.scan(
        FilterExpression=Key('pk').begins_with('stat#' + short_code) | Key('pk').begins_with('counter#' + short_code),
        ProjectionExpression='#resource_type, #created_timestamp, visit_count',
        ExpressionAttributeNames={
            '#created_timestamp': 'timestamp',
            '#resource_type': 'type'
        }
    )

    stats = {}
    total_count = 0
    for item in response['Items']:
        if item.get('type') == 'counter':
            total_count = item.get('visit_count')
        else:
            visited_date = datetime.datetime.fromtimestamp(item.get('timestamp')).strftime('%Y-%m-%d');
            if visited_date in stats:
                stats[visited_date] += 1
            else:
                stats[visited_date] = 1
    return {
        "statusCode": 200,
        "body": json.dumps({ 'stats': stats, 'total_count': total_count }, cls=DecimalEncoder),
        "headers": {
            'Content-Type': 'application/json', 
            'Access-Control-Allow-Origin': '*'
        }
    }
