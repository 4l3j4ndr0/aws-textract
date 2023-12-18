import json
import boto3
import base64
textract_client = boto3.client('textract')
s3_client = boto3.client('s3')

def proccess_textract_information(data):
    response = []
    for field in data:
        response.append({
            'label' : field.get('LabelDetection', {}).get('Text') if field.get('Type', {}).get('Text') == 'OTHER' else field.get('Type', {}).get('Text'),
            'value' : field.get('ValueDetection', {}).get('Text')
        })
    return response

def lambda_handler(event, context):
    try:
        # Parse the input JSON from the API Gateway
        body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        base64_image = body.get("base64_image", None)
        base64_image = base64_image.split(",")[1]
        decoded_bytes = base64.b64decode(base64_image)
        if not base64_image:
            return {
            'statusCode': 400,
            'body': json.dumps({'message': "The body param base64_image is required."}),
        }
            

        textract_response = textract_client.analyze_expense(
            Document = {
                'Bytes': decoded_bytes
            }
        )

        if 'ExpenseDocuments' in textract_response:
            data_proccesed = proccess_textract_information(textract_response['ExpenseDocuments'][0]['SummaryFields'])

        # Return a success response
        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(data_proccesed),
        }

    except Exception as e:
        # Return an error response
        print("EXCEPTION::::", e)
        response = {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': str(e)}),
        }

    return response
