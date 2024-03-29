
from scrapli.driver.core import IOSXEDriver
from rich import print as pr

devices = [
    {"host": "192.168.111.1", "auth_username": "admin", "auth_password": "Cisco123", "ssh_config_file": True, "auth_strict_key": False},
    {"host": "192.168.111.100", "auth_username": "admin", "auth_password": "Cisco123", "ssh_config_file": True, "auth_strict_key": False}
]

for device in devices:
    with IOSXEDriver(**device) as connection:
        response = connection.send_command("show cdp neighbor detail")
        structured_response = response.genie_parse_output()
        cdp_index = structured_response['index']
        pr(f"*** Sending Config to {device['host']} ***")
        for item in cdp_index:
            remote_device = cdp_index[item]['device_id'].split('.')[0]
            remote_port = cdp_index[item]['port_id']
            local_port = cdp_index[item]['local_interface']
            config_commands = [f"interface {local_port}", f"description Connected to {remote_device}'s {remote_port}"]
            results = connection.send_configs(config_commands)
            pr(results.result)
        pr("*** Config Sent ***\n")
