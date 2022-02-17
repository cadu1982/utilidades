import boto3
# id = 'i-09b4d1b885d6441e4'
    
def get_tags(id):
    boto3.setup_default_session(profile_name='ragazzi')
    client = boto3.client('ec2', region_name='us-east-1')
    tag = client.describe_tags(
        Filters=[
            {
                'Name': 'resource-id',
                'Values': [
                    id,
                ],
            },
        ],
    )
    # print(tag['Tags'][0]['Value'])
    return tag
            

