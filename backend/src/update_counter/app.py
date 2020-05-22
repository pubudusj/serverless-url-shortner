import json
import boto3
import os
import decimal

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
    data = json.loads(event['Records'][0]['Sns']['Message'])

    input = {
        'pk': 'counter#' + data['id'],
        'timestamp': data['timestamp'],
        'type': 'stat',
        'resource_value': data['id']
    }
    result = table.update_item(
        Key={
            'pk': 'counter#' + data['id'],
            'timestamp': 1234
        },
        UpdateExpression="set visit_count = if_not_exists(visit_count, :start) + :inc, resource_value = :resource_value, #resource_type = :type",
        ExpressionAttributeValues={
            ':inc': decimal.Decimal(1),
            ':type': 'counter',
            ':start': 0,
            ':resource_value': data['id']
        },
        ExpressionAttributeNames={
            '#resource_type': 'type'
        }
    )
