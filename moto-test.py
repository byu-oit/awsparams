import boto3
import sure
from moto import mock_ssm, mock_ec2
import os


@mock_ec2
@mock_ssm
def moto_test_describe_parameters():
    client = boto3.client('ssm', aws_access_key_id="FakeKey", aws_secret_access_key='FakeSecretKey', aws_session_token='FakeSessionToken')

    client.put_parameter(
        Name='test',
        Description='A test parameter',
        Value='value',
        Type='String')

    response = client.describe_parameters()

    len(response['Parameters']).should.equal(1)
    response['Parameters'][0]['Name'].should.equal('test')
    response['Parameters'][0]['Type'].should.equal('String')


def main():
    print(os.environ)
    moto_test_describe_parameters()


if __name__ == '__main__':
    main()
