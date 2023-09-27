import paramiko
from netmiko import ConnectHandler

ntp_addr="205.169.134.6"

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
        output = netcon.send_command(f"configure ntp server add {ntp_addr}")
        output += netcon.save_config()
        print(output)
    if device["device_type"] == "vyos_ssh":
        output = netcon.config_mode()
        output += netcon.send_command(f"set system ntp server {ntp_addr} prefer")
        output += netcon.commit()
        output += netcon.save_config()
        print(output)
    netcon.disconnect()

print("script finished, exiting")