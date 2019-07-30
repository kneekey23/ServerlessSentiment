import json
import urllib.parse as urlparse
import boto3

def lambda_handler(event, context):
    body = event["body"]
    print(body)
    parsed = urlparse.parse_qs(body)
    text = parsed["Body"][0]
    print(text)

    client = boto3.client('comprehend')
    response = client.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    sentiment = response['Sentiment']



    return {
        "statusCode": 200,
        "body": '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>' + 'Hello World' + '</Body></Message></Response>',
        "headers": {"Content-Type": "application/xml"}
    }
