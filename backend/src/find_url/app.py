import json

def index(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Find URL by short id",
        }),
    }
