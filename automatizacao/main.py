context = {'version': '0', 'id': '80e0c19d-f26d-3d9c-1776-605cc242b38e',
           'detail-type': 'EC2 Instance State-change Notification', 'source': 'aws.ec2', 'account': '596490595119',
           'time': '2022-02-09T17:50:37Z', 'region': 'us-east-1',
           'resources': ['arn:aws:ec2:us-east-1:596490595119:instance/i-0e3844befff9de3ba'],
           'detail': {'instance-id': 'i-09b4d1b885d6441e4', 'state': 'unning'}}

from aws import tags
from aws import route53
from aws import ip

instance_id = context['detail']['instance-id']
status = (context['detail']['state'])
tag = tags.get_tags(instance_id)
public_ip = ip.get_ip(instance_id)

if status == 'running':
    route53.insert('camila.myfisrtzone.com.', public_ip)
    print('inserido')
else:
     route53.delete('camila.myfisrtzone.com.', public_ip)
     print('deletado')



# def handler(id):
#     id = context['detail']['instance-id']
#     status = (context['detail']['state'])
#     tag = tags.get_tags(id)
#     if status == 'running':
#         route53.insert(ip.get_ip(ip), tag)
#         print('deu certo')
#     else:
#         route53.delete(ip.get_ip(ip), tag)
#         print('deu errado')
#
# handler(id)

# if __name__ == "__main__":
