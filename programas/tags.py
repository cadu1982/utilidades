import boto3

boto3.setup_default_session(profile_name='ragazzi')
client = boto3.client('ec2', region_name='us-east-1')
response = client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [
                'i-04703ade5adfe0ad9',
            ],
        },
    ],
)

print(response)



