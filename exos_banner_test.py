import logging
import paramiko
from netmiko import ConnectHandler, file_transfer

logging.basicConfig(level=logging.DEBUG)

BANNER="This is a test for the banner script"

exos_banner=chr(10) + BANNER + chr(10) + chr(10)

device = {
    "device_type": "extreme_exos",
    "host": "205.169.134.1",
    "username": "admin",
    "password": "",
}

#this is exos cli script language, building a script with the banner and saving it
testfile = ["configure banner", BANNER, chr(10), chr(10)]
f = open("banner.xsf", "w")
f.writelines(testfile)
print(f.read())
f.close()

netcon = ConnectHandler(**device)
#long long story short, exos sucks and needs this long distance runaround to set a banner
output = file_transfer(
    netcon,
    source_file="banner.xsf",
    dest_file="banner.xsf",
    overwrite_file=True,
)
output += netcon.send_command("load script /usr/local/cfg/banner.xsf"
output += netcon.send_command("show banner")
output += netcon.send_command("save configuration")
print(output)
netcon.disconnect()