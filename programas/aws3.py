import boto3

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
