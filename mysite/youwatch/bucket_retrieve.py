import os
import boto3

# Initialize a Boto3 S3 client
s3 = boto3.client('s3')

# Specify the bucket name and object key
bucket_name = 'youwatch-aws-bucket'
object_key = 'Videos/youwatchtest.mp4'
local_path = 'mysite/youwatch/videos/'  # Replace with your local folder path

# Ensure the local directory exists, or create it if it doesn't
if not os.path.exists(local_path):
    os.makedirs(local_path)

# Retrieve the object data
try:
    # Download the video file from S3 to your local folder
    s3.download_file(bucket_name, object_key, local_path + 'video.mp4')
    print("Video downloaded successfully!")
except Exception as e:
    print(f"Error: {e}")