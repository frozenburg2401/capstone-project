import paramiko
from netmiko import ConnectHandler

#Note: ExOS specifies a limit on the size of the banner to be not more than 79 columns wide and 24 rows long
BANNER="This is a test for the banner script"

exos_cmdlist="configure banner\n" + BANNER

vyos_cmd="set system login banner pre-login " + BANNER

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
        #commenting out for now, cant figure out why this wont work
        '''
        output = netcon.send_command(exos_cmdlist)
        output += netcon.send_command("show banner")
        output += netcon.send_command("save configuration")
        print(output)
        '''
        pass
    if device["device_type"] == "vyos_ssh":
        output = netcon.send_command_set(vyos_cmd)
        output += netcon.commit()
        print(output)
    netcon.disconnect()

print("script finished, exiting")