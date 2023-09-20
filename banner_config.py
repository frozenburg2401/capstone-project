import paramiko
from netmiko import ConnectHandler
import time

MLS1 = {
    "device_type": "extreme_exos"
    "host": "205.169.134.1"
    "username": "admin"
    "password": ""
}

MLS2 = {
    "device_type": "extreme_exos"
    "host": "205.169.130.1"
    "username": "admin"
    "password": ""
}

MLS3 = {
    "device_type": "extreme_exos"
    "host": "205.169.132.1"
    "username": "admin"
    "password": ""
}

R1 = {
    "device_type": "extreme_exos"
    "host": "205.169.64.5"
    "username": "vyos"
    "password": "vyos"
}

R2 = {
    "device_type": "extreme_exos"
    "host": "205.169.64.9"
    "username": "vyos"
    "password": "vyos"
}

netcon = ConnectHandler(**MLS1)
print(netcon.find_prompt())
netcon.disconnect()