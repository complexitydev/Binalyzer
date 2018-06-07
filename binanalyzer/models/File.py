# -*- coding: utf-8 -*-
import boto3
import json

class File:
    file = None
    s3 = None
    aws_lambda = None

    def __init__(self, req):
        self.file = req
        self.s3 = boto3.client("s3")
        self.aws_lambda = boto3.client("lambda")

    def upload(self):
        try:
            self.s3.upload_fileobj(self.file, 'my-file-samples', self.file.filename)

        except Exception as e:
            print("Error uploading to s3 ", e)
            return False
        data = json.loads(self.process_file())
        ordered_data = self.get_ordered_data(data)
        return ordered_data

    def process_file(self):
        args = {'service': 'analysis', 'file': self.file.filename}
        response = self.aws_lambda.invoke(
            FunctionName='arn:aws:lambda:us-east-2:332807454899:function:malware_analysis',
            InvocationType='RequestResponse',
            LogType='None',
            Payload=json.dumps(args)
        )
        data = response['Payload'].read().decode()
        return data

    def get_ordered_data(self, data):
        info = {}
        index = 0;
        for item in reversed(sorted(data['message'], key=len)):
            if index > 200:
                continue
            info[item] = "".join([" %02x" % ord(c) for c in item])
            index += 1
        return info