#!/usr/bin/env python3

from collections import defaultdict
import boto3
import subprocess
import os,sys


def fetch_details():

    ec2 = boto3.resource('ec2')

    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}])

    ec2info = defaultdict()
    for instance in running_instances:
        for tag in instance.tags:
            if 'Name'in tag['Key']:
                name = tag['Value']
        ec2info[instance.id] = {
            'Name': name,
            'Type': instance.instance_type,
            'State': instance.state['Name'],
            'Private IP': instance.private_ip_address,
            'Public IP': instance.public_ip_address,
            'Launch Time': instance.launch_time
            }

    attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
    for instance_id, instance in ec2info.items():
        for key in attributes:
            print("{0}: {1}".format(key, instance[key]))
        print("------")


def up():

	if os.getcwd() != '/home/prince/ansible-operations':
		os.chdir('/home/prince/ansible-operations')

	result = subprocess.run("ansible -m ping servers -i inventory", shell=True)
	return (result.returncode == 0)


def do_operations():

	if not up():
		print('[+] Server Down')
		sys.exit(1)

	subprocess.run("ansible-playbook -i inventory web-hosting.yml -l servers -K ", shell=True)


def main():

	do_operations()



main()
