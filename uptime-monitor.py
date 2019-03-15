import json
import requests

def check(event, context):
    website = event['queryStringParameters']['website']
    res = requests.get(website)

    response = {
        "statusCode": 200,
        "body": json.dumps({ 
            "status_code": res.status_code, 
            "elapsed_time": res.elapsed.total_seconds() 
        })
    }

    return response

