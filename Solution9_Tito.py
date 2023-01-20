#!/usr/bin/python3

import re

ip_pattern = re.compile(
    r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

ip_address = input("For example: 192.168.0.1  -")

match = ip_pattern.match(ip_address)

if match:
    print("Valid IP address.")
else:
    print("Invalid IP address.")
