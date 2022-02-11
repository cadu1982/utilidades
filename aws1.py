subindo = {'version': '0', 'id': '80e0c19d-f26d-3d9c-1776-605cc242b38e', 'detail-type': 'EC2 Instance State-change Notification', 'source': 'aws.ec2', 'account': '596490595119', 'time': '2022-02-09T17:50:37Z', 'region': 'us-east-1', 'resources': ['arn:aws:ec2:us-east-1:596490595119:instance/i-0e3844befff9de3ba'], 'detail': {'instance-id': 'i-0e3844befff9de3ba', 'state': 'running'}}
terminate = {'version': '0', 'id': '8428f347-88f6-a0cb-9d62-fe1b5efa39f1', 'detail-type': 'EC2 Instance State-change Notification', 'source': 'aws.ec2', 'account': '596490595119', 'time': '2022-02-09T17:52:54Z', 'region': 'us-east-1', 'resources': ['arn:aws:ec2:us-east-1:596490595119:instance/i-0e3844befff9de3ba'], 'detail': {'instance-id': 'i-0e3844befff9de3ba', 'state': 'terminated'}}
tags = {'Tags': [{'Key': 'DNS_NAME', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'cadu'}, {'Key': 'Name', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'web-1'}, {'Key': 'mongodb', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'true'}, {'Key': 'web', 'ResourceId': 'i-04703ade5adfe0ad9', 'ResourceType': 'instance', 'Value': 'true'}], 'ResponseMetadata': {'RequestId': 'dc5bae10-fba4-4448-8423-722873f87c00', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'dc5bae10-fba4-4448-8423-722873f87c00', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '822', 'date': 'Wed, 09 Feb 2022 18:03:22 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

def has_dns_tag(tags):
    for tag in tags['Tags']:
        if tag['Key'] == "DNS_NAME":
            return tag['Value'] 
    return False

def get_tags(instance_id):

def insere_dns(dns_name):
    # dns = instancia.id()
    print('Dns inserido com sucesso', dns_name)
  

def deleta_dns(dns_name):
    # dns = instancia.id()
    print('Dns deletado com sucesso', dns_name)
    

def handler(event, contenxt):
    if event['detail']['state'] == 'running':
        tag = has_dns_tag(tags)
        if tag:
            insere_dns(tag)
        else:
            print("Nao Achei")
    else:
        tag = has_dns_tag(tags)
        deleta_dns(tag)
        print('vamos deletar')
    
if __name__ == "__main__":
    handler(terminate, [])

    