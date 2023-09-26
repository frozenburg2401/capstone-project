import paramiko
from netmiko import ConnectHandler

#Note: ExOS specifies a limit on the size of the banner to be not more than 79 columns wide and 24 rows long
BANNER="This is a test for the banner script"

exos_cmdlist=[
    ["configure banner", r"[\n]"],
    [BANNER, BANNER],
    ["\n"]
]

vyos_cmd="show config"

MLS1 = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

MLS2 = {
    "device_type": "extreme_exos",
    "host": "205.169.130.1",
    "username": "admin",
    "password": "",
}

MLS3 = {
    "device_type": "extreme_exos",
    "host": "205.169.132.1",
    "username": "admin",
    "password": "",
}

R1 = {
    "device_type": "vyos_ssh",
    "host": "205.169.64.5",
    "username": "vyos",
    "password": "vyos",
}

R2 = {
    "device_type": "vyos_ssh",
    "host": "205.169.64.9",
    "username": "vyos",
    "password": "vyos",
}

for device in (MLS1, MLS2, MLS3, R1, R2):
    netcon = ConnectHandler(**device)
    print(netcon.find_prompt())
    if device["device_type"] == "extreme_exos":
        output = netcon.send_multiline_timing(exos_cmdlist)
        output += netcon.send_command("show banner")
        output += netcon.send_command("save configuration")
        print(output)
    if device["device_type"] == "vyos_ssh":
#        print(netcon.send_command(vyos_cmd))
        pass
    netcon.disconnect()

print("script finished, exiting")