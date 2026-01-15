import boto3
import os
import io

s3_client = boto3.client('s3')


class S3Util:

    @staticmethod
    def put_file(bucket_name, file_path, file_binary):
        try:
            result = s3_client.put_object(
                Bucket=bucket_name, Key=file_path, Body=file_binary)
            return result
        except Exception as e:
            raise e

    @staticmethod
    def put_file_txt(bucket_name, file_path, file_txt, encoding):
        file = io.StringIO()
        file.write(file_txt)
        file_binary = file.getvalue().encode(encoding=encoding)

        return S3Util.put_file(bucket_name, file_path, file_binary)

    @staticmethod
    def upload(local_file, bucket, dir_path, file_name):
        s3 = boto3.client('s3')
        key = os.path.join(dir_path, file_name)
        s3.upload_file(local_file, bucket, key)

    @staticmethod
    def download(bucket, file_key):
        s3 = boto3.client('s3')
        file_path = f'/tmp/{file_key.split("/")[-1]}'
        s3.download_file(bucket, file_key, file_path)

        return file_path
