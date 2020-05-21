#############################################
# Rozsireny ping pomoci send_command_timing()
#
#  ping
#  Protocol [ip]: 
#  Target IP address: 8.8.8.8
#  Repeat count [5]: 10
#  Datagram size [100]: 
#   Timeout in seconds [2]: 
#  Extended commands [n]: 
#  Sweep range of sizes [n]: 
#  Type escape sequence to abort.
#  Sending 10, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
#  !!!!!!!!!!
#  Success rate is 100 percent (10/10), round-trip min/avg/max = 1/1/4 ms
############################################

import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("10\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(output)
print()
