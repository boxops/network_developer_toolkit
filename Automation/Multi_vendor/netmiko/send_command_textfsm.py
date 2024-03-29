#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.111.1",
    "username": "admin",
    "password": getpass(),
}

command = "show ip int brief"
with ConnectHandler(**cisco1) as net_connect:
    # Use TextFSM to retrieve structured data
    output = net_connect.send_command(command, use_textfsm=True)

print()
pprint(output)
print()
