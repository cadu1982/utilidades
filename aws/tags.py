import boto3
# id = 'i-04703ade5adfe0ad9'
    
def get_tags():
    boto3.setup_default_session(profile_name='ragazzi')
    client = boto3.client('ec2', region_name='us-east-1')
    return client.describe_tags(
        Filters=[
            {
                'Name': 'resource-id',
                'Values': [
                    'i-04703ade5adfe0ad9',
                ],
            },
        ],
    )


