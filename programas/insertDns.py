import boto3

boto3.setup_default_session(profile_name='ragazzi')

client = boto3.client('route53')

response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'myfisrtzone.com.',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
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





