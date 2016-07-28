#!/usr/bin/env python3

import ipaddress

# construct an CIDR network
net = ipaddress.ip_network('123.45.67.64/27')
for ip in net:
    print(ip)

# check ip in network
a = ipaddress.ip_address('123.45.67.69')
print(a in net)
b = ipaddress.ip_address('123.45.67.123')
print(b in net)

# ip address and network address with ip interface
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)
