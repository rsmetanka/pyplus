import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command("show version")

# Otevre soubor a zapise do neho
with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()

