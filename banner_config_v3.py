import paramiko
from netmiko import ConnectHandler

#Note: ExOS specifies a limit on the size of the banner to be not more than 79 columns wide and 24 rows long
#The docs for vyos do not specify a limit, it is likely close to the standard 80x24 terminal size though
#The banner included here is the maximum width allowed
BANNER=[
    "##############################################################################", 
    "  NOTICE: This network device is only to be accessed by authorized personnel  ", 
    "   of the district. Unauthorized connections will be logged and acted upon.   ", 
    "##############################################################################"
]

exos_cmdlist=["configure banner", chr(10), BANNER, chr(10), chr(10)]

vyos_cmdlist="set system login banner pre-login " + '"' + BANNER + '"'

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

#this is exos cli script language, building a script with the banner and saving it
f = open("banner.xsf", "w")
f.writelines(exos_cmdlist)
f.close()

for device in (MLS1, MLS2, MLS3, R1, R2):
    netcon = ConnectHandler(**device)
    print(netcon.find_prompt())
    if device["device_type"] == "extreme_exos":
        #long long story short, exos sucks and needs this long distance runaround to set a banner
        output = netcon.send_command(exos_cmdlist)
        output += netcon.send_command("show banner")
        output += netcon.send_command("save configuration")
        print(output)
    if device["device_type"] == "vyos_ssh":
        #enter config mode, set the banner, commit and save
        output = netcon.config_mode()
        output += netcon.send_command(vyos_cmdlist)
        output += netcon.commit()
        output += netcon.save_config()
        print(output)
    netcon.disconnect()

print("script finished, exiting")