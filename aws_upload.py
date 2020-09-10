import logging
import boto3
import os


# we are creating a file that will store our logs
# we are setting the default logging level to debug (it is usually warning)
logging.basicConfig(filename='upload_s3.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def upload_to_aws():

    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]

    s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    s3_client.upload_file('Downloads/ItJobsWatchTop30.csv', 'andrew-mvc-with-itjobs', 'ItJobsWatchTop30.csv')
    logging.info("Your file has been successfully uploaded to an AWS bucket!")

