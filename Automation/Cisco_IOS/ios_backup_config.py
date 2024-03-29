#!/usr/bin/env python
# IOS running config backup

from netmiko import Netmiko
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d%m%Y_%H-%M-%S")

username = "admin"
password = "Cisco123"



Switch1 = {
    "host": "192.168.111.1",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch2 = {
    "host": "192.168.243.149",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch3 = {
    "host": "192.168.243.150",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch4 = {
    "host": "192.168.243.148",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch5 = {
    "host": "192.168.243.147",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

myswitches = [Switch1, Switch2, Switch3, Switch4, Switch5]

for x in myswitches:
    net_connect = Netmiko(**x)
    showver = net_connect.send_command("show version", use_textfsm=True)
    showrun = net_connect.send_command("show run")
    hostname = showver[0]['hostname']
    backupfilename = f"{hostname}_{dt_string}.txt"
    with open(backupfilename, "w") as file:
        file.write(showrun)
    print(f"{hostname} has been backed up" + "\n")
    net_connect.disconnect()
