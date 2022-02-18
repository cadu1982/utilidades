import boto3


def insert(name, ip):
    print("Tentando criar {} - {}".format(name, ip))
    boto3.setup_default_session(profile_name='ragazzi')
    client = boto3.client('route53')
    cria = client.change_resource_record_sets(
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
        },
        HostedZoneId='Z043404112J4ILIAMZASV',
    )
    return cria


def delete(name, ip):
    print("Tentando deletar {} - {}".format(name, ip))
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
        },
        HostedZoneId='Z043404112J4ILIAMZASV',
    )
    return response