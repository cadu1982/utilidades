import boto3


boto3.setup_default_session(profile_name='ragazzi')
ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_addresses(
    Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                   'i-09b4d1b885d6441e4' ,
                ],
            },
        ],
)
print(response['Addresses'][0]['PublicIp'])