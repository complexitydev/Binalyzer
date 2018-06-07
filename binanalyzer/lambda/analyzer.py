import boto3
import string


def get_file_from_s3(file_name):
    bucket = 'my-file-samples'
    key = file_name

    s3 = boto3.resource("s3")
    try:
        s3.Bucket('my-file-samples').download_file(file_name, "/tmp/{}".format(file_name))
    except Exception as e:
        print("Something went from getting the file")
        return False
    return "/tmp/{}".format(file_name)


def extract_strings(file_name):
    with open(file_name, errors="ignore") as f:
        result = ''
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) > 5:
                yield result
            result = ''
        if len(result) > 5:
            yield result


def get_ascii_strings(file_name):
    return list(extract_strings(file_name))


def lambda_handler(event, context):
    if event['service'] == 'analysis':
        file_path = get_file_from_s3(event['file'])
        if not file_path:
            return {
                'message': 'fileerror'
            }
        ascii_data = get_ascii_strings(file_path)
        if not ascii_data:
            return {
                'message': 'stringserror'
            }
        return {
            'message': ascii_data
        }
