import os
import boto3

def retrieve():

    # Initialize a Boto3 S3 client
    s3 = boto3.client("s3")

    i = 1
    # Specify the bucket name and object key
    bucket_name = "youwatch-aws-bucket"
    object_key = "Videos/youwatchtest.mp4"
    local_path = "mysite/youwatch/media/"  # Replace with your local folder path
    file_name = f"video{i}.mp4"

    # Ensure the local directory exists, or create it if it doesn't
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    if os.path.isfile(file_name):
        print("Error: this file already exists on the local host")
        exit(1)
    else:
        # Retrieve the object data
        try:
            # Download the video file from S3 to your local folder
            s3.download_file(bucket_name, object_key, local_path + "video.mp4")
            print("Video downloaded successfully!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    retrieve()