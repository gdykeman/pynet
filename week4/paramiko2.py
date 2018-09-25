#!/usr/bin/env python
import paramiko
import time

MAX_BUFFER = 65535

def clear_buffer(remote_conn):
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')


def disable_paging(remote_conn, cmd='terminal length 0'):
    #Disable Paging
    cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    clear_buffer(remote_conn)

def send_command(remote_conn, cmd='', delay=1):
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')
    else:
        return ''

def main():
    #Use Paramiko to retrieve the entire 'show version' output
    # try:
    #     ip_addr = raw_input("Enter IP Address: ")
    # except NameError:
    #     ip_addr = input("Enter IP Address: ")

    username = 'pyclass'
    password = '88newclass'
    port = 22
    ip_addr = 'cisco2.twb-tech.com'

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()

    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn)

    send_command(remote_conn, cmd='conf t')
    send_command(remote_conn, cmd='logging buffered 20000')
    send_command(remote_conn, cmd='end')

    output = send_command(remote_conn, cmd='show run | i logging', delay=2)

    print('\n>>>>')
    print(output)
    print('\n>>>>')

if __name__ == '__main__':
    main()
