import json

def index(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Update URL access stats",
        }),
    }
