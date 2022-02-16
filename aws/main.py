import boto3
from route53 import insert, delete
from ec2 import get_tags


X = get_tags()
print(X)



# def handler(event, contenxt):
#     print("Iniciando")
#     print(event)
#     pass



# if __name__ == "__main__":
#     handler(subindo, [])
#     up = (subindo['detail']['state'])
#     up == 'running'
#     insere_dns()