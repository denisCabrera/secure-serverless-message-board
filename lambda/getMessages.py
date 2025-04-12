import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Messages')

def lambda_handler(event, context):
    response = table.scan(Limit=10)
    messages = response.get('Items', [])
    return {
        'statusCode': 200,
        'body': json.dumps(messages)
    }
