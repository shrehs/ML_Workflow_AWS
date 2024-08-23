""" Lambda function 1: Preprocessing """
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key =event["s3_key"] ## TODO: fill in
    bucket = event["s3_bucket"]## TODO: fill in

    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    boto3.resource('s3').Bucket(bucket).download_file(key, "/tmp/image.png")

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
}






""" Lambda function 2- inference """
import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-endpoint-new"

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])

    # Create a SageMaker runtime client
    runtime = boto3.client('sagemaker-runtime')

    # Make a prediction
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='application/x-image',  
        Body=image
    )

    # Decode the inferences to get the list not the string of list
    
    inferences = json.loads(response['Body'].read().decode('utf-8'))

    # We return the data back to the Step Function    
    event["inferences"] = inferences
    return {
        'statusCode': 200,
        'body': {
            "image_data": event["body"]['image_data'],
            "s3_bucket": event["body"]['s3_bucket'],
            "s3_key": event["body"]['s3_key'],
            "inferences": event['inferences'],
       }
    }






""" Lambda function 3: Threshold check """
import json

THRESHOLD = 0.9

def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event["body"]['inferences']## TODO: fill in

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(list(inferences))>THRESHOLD## TODO: fill in

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event
    }