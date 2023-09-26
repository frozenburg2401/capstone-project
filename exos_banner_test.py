import paramiko
from netmiko import ConnectHandler

BANNER="This is a test for the banner script"

exos_cmdlist="configure banner" + chr(10) + BANNER + chr(10) + chr(10)

device = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

netcon = ConnectHandler(**device)
output = netcon.send_command(
    command_string=exos_cmdlist,
    expect_string=r".MLS-1")
    strip_prompt=False,
    strip_command=False
)
output += netcon.send_command("show banner")
output += netcon.send_command("save configuration")
print(output)
netcon.disconnect()