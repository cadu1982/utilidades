import boto3


def insert(name, ip):
    
    
    boto3.setup_default_session(profile_name='ragazzi')

    client = boto3.client('route53')

    response = client.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': name,
                        'ResourceRecords': [
                            {
                                'Value': ip,
                            },
                        ],
                        'TTL': 60,
                        'Type': 'A',
                    },
                },
            ],
            'Comment': 'Web server for myfisrtzone',
        },
        HostedZoneId='Z07613381BFGTQENZMGEW',   
    )

    print(response)
    return insert


def delete(name, ip):

    boto3.setup_default_session(profile_name='ragazzi')

    client = boto3.client('route53')

    response = client.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'DELETE',
                    'ResourceRecordSet': {
                        'Name': name,
                        'ResourceRecords': [
                            {
                                'Value': ip,
                            },
                        ],
                        'TTL': 60,
                        'Type': 'A',
                    },
                },
            ],
            'Comment': 'Web server for myfisrtzone',
        },
        HostedZoneId='Z07613381BFGTQENZMGEW',
    )

    print(response)
    return delete