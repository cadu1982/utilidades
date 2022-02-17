from multiprocessing.sharedctypes import Value
import boto3

boto3.setup_default_session(profile_name='ragazzi')
client = boto3.client('ec2', region_name='us-east-1')
tags = client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [
                'i-04703ade5adfe0ad9',
            ],
        },
    ],
)
print(tags['Tags'][0]['Value'])
# print(tags['Tags']['Value'][1])
    

# for tag in tags['Tags']:
#     if tag['Key'] == "mongodb":
#        tag = tag['Value']
#        print(tag)
#     else:
#         tag = False
