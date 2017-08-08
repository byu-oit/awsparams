import boto3
import sure
from moto import mock_ssm, mock_ec2


@mock_ec2
@mock_ssm
def moto_test_describe_parameters():
    client = boto3.client('ssm', region_name='us-east-1')

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
    print('Starting test')
    moto_test_describe_parameters()
    print('finished')


if __name__ == '__main__':
    moto_test_describe_parameters()
