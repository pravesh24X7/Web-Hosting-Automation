#/usr/bin/env python3 


import boto3
from random import randint

def create_ec2():


    client = boto3.client('ec2', region_name='ap-south-1')
    ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
    ec2_identity = 'Deployment-Server-' + str(randint(0, 9999999))
    response = ec2_resource.create_instances(
            ImageId='ami-069d9fecd19e7ed40',
            MinCount=1,
            MaxCount=1,
            KeyName='server-key',
            InstanceType='t2.micro',
            SecurityGroupIds = ['sg-0e1d28306f31842c6'],
            TagSpecifications=[
                {
                'ResourceType': 'instance',
                'Tags': [
                {
                    'Key': 'Name',
                    'Value': ec2_identity
                },
            ]},]
                )

    for instance in response: 
        print(f'EC2 instance "{instance.id}" of Type : "{instance.instance_type}" has been launched')
        instance.wait_until_running()
    



def list_running_ec2():

    region = 'ap-south-1'
    ec2_resource = boto3.resource('ec2', region_name=region)

    state = 'running'

    instances = ec2_resource.instances.filter(
        Filters=[
            {
            'Name': 'instance-state-name',
            'Values': [
                state
                ]
            }
        ]
    )

    print('List of Running Instances :')
    for instance in instances:
        print('\n')
        print(f'\tInstance ID: {instance.id}')
        print(f'\tInstance Public Ipv4: {instance.public_ip_address}\n\tInstance Type: {instance.instance_type}')



def id_assoc_ip():

    region = 'ap-south-1'
    ec2_resource = boto3.resource('ec2', region_name=region)

    info_dict = {}
    for instance in ec2_resource.instances.all():
        config_status = True
        if not instance.public_ip_address:
            config_status = False
        info_dict[instance.id]={
                'Config': config_status,
                'PublicIpv4': instance.public_ip_address,
                'PrivateIpv4': instance.private_ip_address
                }

    return info_dict



def list_all_ec2(show=False, get_ec2_id=False):

    region = 'ap-south-1'
    ec2_resource = boto3.resource('ec2', region_name=region)

    ec2_ids = []
    if not get_ec2_id:
        del ec2_ids

    if show:
        for instance in ec2_resource.instances.all():
            print("EC2 Id: {0}\nEC2 Type: {1}\nEC2 Public Ipv4: {2}\nEC2 Private Ipv4: {3}".format(instance.id, instance.instance_type, instance.public_ip_address, instance.private_ip_address))

            ec2_ids.append(instance.id)

    if get_ec2_id:
        return ec2_ids

    return None




def ops_ec2(ec2_id,flag=str('start')):


    region = 'ap-south-1'
    ec2_resource = boto3.resource('ec2', region_name=region)

    instance = ec2_resource.Instance(ec2_id)

    if flag == 'terminate':
        instance.terminate()

        print(f'Terminated EC2 instance : {instance.id}')
        instance.wait_until_terminated()

        print(f'EC2 instance "{ec2_id}" has been terminated')

    elif flag == 'reboot':
        instance.reboot()

        print(f'EC2 instance "{ec2_id}" has been rebooted')
        instance.wait_until_running()

        print(f'EC2 instance "{ec2_id}" has restarted')

    elif flag == 'start':
        instance.start()

        print(f'Starting EC2 instance : {ec2_id}"')
        instance.wait_until_running()

        print(f'EC2 Instance : "{ec2_id}" is ready to use')

    else:
        instance.stop()
        print(f'Shutting Down "{ec2_id}"')

        instance.wait_until_stopped()
        print(f'EC2 instance "{ec2_id}" is stopped')




"""
#ec2_ids = list_all_ec2(show=False, get_ec2_id=True)
#list_running_ec2()

#ops_ec2('i-047e7bf386e426e5d', flag='stop')
#list_running_ec2()

#res = id_assoc_ip()

#for K in res:

#    V = str(res[K])
#    print(K + " >>>> " + V)

ec2 = list_all_ec2(show=True, get_ec2_id=True)
print(ec2)

'''
for i in ec2:
    if i == 'i-00e7c4418b10dbf37':
        continue
    ops_ec2(i, flag='stop')
    '''
#for K in res:

#    if not res[K]['Config']:
#    print(res[K]['PublicIpv4'])


ops_ec2('i-047e7bf386e426e5d', flag='terminate'
        )
        """
create_ec2()
