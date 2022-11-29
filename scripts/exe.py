#!/usr/bin/env python3


import boto3


def create_vm():

    instance_name = 'Red Hat Server'
    ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
    instances = ec2_resource.create_instances(
            ImageId='ami-069d9fecd19e7ed40',
            MinCount=1, MaxCount=1,
            InstanceType='t2.micro',
            KeyName='Universal',
            TagSpecifications=[
                {
                    'ResourceType':'instance',
                    'Tags':[
                        {
                            'Key':'Name',
                            'Value':instance_name
                            },
                        ]
                    },]
                )

    for instance in instances:
        print(f'[+] EC2 instance {instance.id} of type {instance.instance_type} has been launched')

        instance.wait_until_running()


create_vm()

