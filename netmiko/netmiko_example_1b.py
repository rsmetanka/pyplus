######################################
# Rozsireny ping pomoci send_command()
#
#  ping
#  Protocol [ip]: 
#  Target IP address: 8.8.8.8
#  Repeat count [5]: 10
#  Datagram size [100]: 
#  Timeout in seconds [2]: 
#  Extended commands [n]: 
#  Sweep range of sizes [n]: 
#  Type escape sequence to abort.
#  Sending 10, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
#  !!!!!!!!!!
# Success rate is 100 percent (10/10), round-trip min/avg/max = 1/1/4 ms
#
#
######################################

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

output = net_connect.send_command(
    "ping", expect_string=r"Protocol", strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"#", strip_prompt=False, strip_command=False
)
net_connect.disconnect()

print()
print(output)
print()
