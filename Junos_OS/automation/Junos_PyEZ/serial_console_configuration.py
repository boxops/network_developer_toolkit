'''
Purpose
Connect to a device running Junos OS using a serial console connection and also load and commit a configuration on the device in a Junos PyEZ application using Python 3.

Reference
https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-connection-methods.html#id-connecting-to-a-device-using-a-serial-console-connection
'''

import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")
mode = 'serial'
port = "/dev/ttyUSB0"
config_path = '/tmp/config_mx.conf'

try:
    with Device(mode=mode, port=port, user=junos_username, passwd=junos_password) as dev:
        print (dev.facts)
        cu = Config(dev)
        cu.lock()
        cu.load(path=config_path)
        cu.commit()
        cu.unlock()

except Exception as err:
    print (err)
    sys.exit(1)
