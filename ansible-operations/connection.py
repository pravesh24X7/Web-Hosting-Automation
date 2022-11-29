#!/usr/bin/env python3

import subprocess
import paramiko
import sys



def is_alive(host):

	cmd = 'ping -c 1 ' + host
	result = subprocess.run(cmd, shell=True)
	
	return (result.returncode == 0)



def get_connection(host, user, passwd):

	if not is_alive(host):
		print('[+] Server Down')
		sys.exit(1)


	client = paramiko.client.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect(host, username=user, password=passwd)
	_stdin, _stdout, _stderr = client.exec_command('df -Th')

	print(_stdout.read().decode())
	client.close()




def main():

	host = '13.233.254.153'
	user = 'ec2-user'
	passwd = 'ec2-user123'

	get_connection(host, user, passwd)



main()
