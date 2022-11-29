#!/usr/bin/env python3



from random import randint
import boto3



def generate_key_pair():
    AWS_REGION = 'ap-south-1'
    ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

    KEY_NAME = 'KeyPair-' + str(randint(1,9999999))

    key_pair = ec2_resource.create_key_pair(
		    KeyName=KEY_NAME,
		    TagSpecifications=[{
			    'ResourceType':'key-pair',
			    'Tags':[{
				    'Key':'Name',
				    'Value': KEY_NAME
			    },]
		    },])

    print('[+] SSH Key Fingerprint :{a}'.format(a=key_pair.key_fingerprint))
    fqn_ = '/home/prince/auth_keys/' + str(KEY_NAME) + '.pem'
    with open(fqn_, 'w') as f:
        f.write(key_pair.key_material)

    return KEY_NAME




def list_key_pair():

    key_list = {}

    ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
    key_pairs = ec2_resource.key_pairs.all()

    for key in key_pairs:
        key_list[key.key_name] = key.key_fingerprint
    return key_list




def search_key_by_name(keyname):

    ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
    key_pairs = ec2_resource.key_pairs.filter(
                KeyNames=[
                    keyname,
                ],)
    for key in key_pairs:
        print(f'[+] SSH Key "{key.key_name}"\tKeyFingerprint "{key.key_fingerprint}"')



def delete_key_pair(keyname):

    ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
    key_pair = ec2_resource.KeyPair(keyname)

    key_pair.delete()
    print(f'[+] SSH Key :\t{key_pair.key_name} successfully deleted')



#generate_key_pair()
res = list_key_pair()


'''
for idx in res:
    search_key_by_name(idx)
'''


