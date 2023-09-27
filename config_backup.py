import time
import paramiko
from netmiko import ConnectHandler

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

#this gets the current time and formatis it as follows:
#YYYYMMDD-HHMMSS
ct = time.strftime("%Y%m%d-%H%M%S")

tftp_addr = "205.169.134.6"

for device in (MLS1, MLS2, MLS3, R1, R2):
    netcon = ConnectHandler(**device)
    tftp_path = device + "_" + ct
    print(netcon.find_prompt())
    if device["device_type"] == "extreme_exos":
        #adding file ext for exos config files
        tftp_path += ".cfg"
        output = netcon.save_config()
        output += netcon.send_command(f"tftp put {tftp_addr} current.cfg {tftp_path}")
        print(output)
    if device["device_type"] == "vyos_ssh":
        #adding txt extension as there isnt a specified format for vyos config files
        tftp_path += ".txt"
        output = netcon.config_mode()
        output += netcon.send_command(f"save tftp://{tftp_addr}/{tftp_path}")
        print(output)
    netcon.disconnect()

print("script finished, exiting")