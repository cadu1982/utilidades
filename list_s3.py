import boto3
# Retrieve the list of existing buckets
boto3.setup_default_session(profile_name='ragazzid')
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')