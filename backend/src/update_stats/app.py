import json

def index(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Update URL access stats",
        }),
    }
