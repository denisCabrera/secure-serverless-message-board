import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Messages')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body.get('message')
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'message': message,
        'timestamp': int(time.time())
    })
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'Message stored'})
    }
