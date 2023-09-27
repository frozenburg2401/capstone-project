import paramiko
from netmiko import ConnectHandler

BANNER="This is a test for the banner script"

exos_banner=chr(10) + BANNER + chr(10) + chr(10)

device = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

netcon = ConnectHandler(**device)
output = netcon.send_command("configure banner" + exos_banner)
output += netcon.send_command("show banner")
output += netcon.send_command("save configuration")
print(output)
netcon.disconnect()