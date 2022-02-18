import boto3
def get_ip(instance_id):
    boto3.setup_default_session(profile_name='ragazzi')
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ip = ec2.describe_addresses(
        Filters=[
                {
                    'Name': 'instance-id',
                    'Values': [
                        instance_id,
                    ],
                },
            ],
    )
    ip = (ip['Addresses'][0]['PublicIp'])
    return ip
