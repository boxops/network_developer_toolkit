#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

# Logging section ##############
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
# Logging section ##############

cisco1 = {
    "device_type": "juniper_junos",
    "host": "192.168.111.123",
    "username": "admin",
    "password": getpass(),
}

net_connect = ConnectHandler(**cisco1)
print(net_connect.find_prompt())
net_connect.disconnect()
