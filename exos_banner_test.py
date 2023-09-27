import logging
import paramiko
from netmiko import ConnectHandler

logging.basicConfig(level=logging.DEBUG)

BANNER="This is a test for the banner script"

exos_banner=chr(10) + BANNER + chr(10) + chr(10)

device = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

netcon = ConnectHandler(**device)
#long story short, cli prompts get disabled on initialization of the connection
#this really messes with the banner commands, reenabling it might fix it?
output += netcon.send_command("enable cli paging")
output += netcon.send_command("configure banner" + exos_banner)
output += netcon.send_command("show banner")
output += netcon.send_command("save configuration")
print(output)
netcon.disconnect()