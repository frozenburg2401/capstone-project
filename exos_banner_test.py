import paramiko
from netmiko import ConnectHandler

BANNER="This is a test for the banner script"

exos_cmdlist="configure banner\n" + BANNER

device = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

netcon = ConnectHandler(**device)
output = netcon.send_command(exos_cmdlist)
output += netcon.send_command("show banner")
output += netcon.send_command("save configuration")
print(output)
netcon.disconnect()