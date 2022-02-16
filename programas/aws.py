subindo = {'version': '0', 'id': '80e0c19d-f26d-3d9c-1776-605cc242b38e', 'detail-type': 'EC2 Instance State-change Notification', 'source': 'aws.ec2', 'account': '596490595119', 'time': '2022-02-09T17:50:37Z', 'region': 'us-east-1', 'resources': ['arn:aws:ec2:us-east-1:596490595119:instance/i-0e3844befff9de3ba'], 'detail': {'instance-id': 'i-0e3844befff9de3ba', 'state': 'running'}}
# terminate = {'version': '0', 'id': '8428f347-88f6-a0cb-9d62-fe1b5efa39f1', 'detail-type': 'EC2 Instance State-change Notification', 'source': 'aws.ec2', 'account': '596490595119', 'time': '2022-02-09T17:52:54Z', 'region': 'us-east-1', 'resources': ['arn:aws:ec2:us-east-1:596490595119:instance/i-0e3844befff9de3ba'], 'detail': {'instance-id': 'i-0e3844befff9de3ba', 'state': 'terminated'}}
tags = {'Tags': [{'Key': 'Name', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'web-1'}, {'Key': 'mongodb', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'true'}, {'Key': 'web', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'true'}], 'ResponseMetadata': {'RequestId': 'dc5bae10-fba4-4448-8423-722873f87c00', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'dc5bae10-fba4-4448-8423-722873f87c00', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '822', 'date': 'Wed, 09 Feb 2022 18:03:22 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

# print(subindo['detail']['state'])
# print(subindo['detail']['instance-id'])
# print(terminate['detail']['state'])
# print(terminate['detail']['instance-id'])

# for tag in tags['Tags']:
#     print(tag['Key'])
#     if tag['Key'] == "mongodb":
#         break


def estado_instancia ():
    
    estado_up = (subindo['detail']['state'])
        
    if estado_up == 'running':
        up = True
        print('inserir dns')
    elif estado_down == 'terminated':
        down = False
        print('deletar dns')
          


def tags_instancia ():
    pass

def insere_dns ():
    print('inserir dns')
    pass

def deleta_dns ():
    print()
    pass



def handler(event, contenxt):
    print("Iniciando")
    print(event)
    pass



if __name__ == "__main__":
    handler(subindo, [])
    up = (subindo['detail']['state'])
    up == 'running'
    insere_dns()


