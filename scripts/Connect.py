#/usr/bin/env python3


import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/prince/auth_keys/Universal.pem')
clnt = paramiko.SSHClient()


clnt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('[+] Connecting ...')

clnt.connect(hostname='13.234.75.237', username='ec2-user', pkey=key)
print('[+] Connected')

commands = [
       'echo "Updating System ..."', 'sudo yum update -y', '$'
        ]

for command in commands:

    if command == '$':
        break

    print('[+] Executing {a},'.format(a=command))
    _stdin, _stdout, _stderr = clnt.exec_command(command)

    print('\tOutput:\n')
    print(_stdout.read())

    print('\tErrors\n')
    print(_stderr.read())


clnt.close()
