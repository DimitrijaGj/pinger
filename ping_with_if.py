#!/usr/bin/env python

import os

""" Taking IP from list pings it and returns if it is down"""
ip_list = ["1.1.1.1", "172.21.118.152", "172.21.116.58", "192.1.0.2"]

for ip in ip_list:
    response = os.popen("ping -c 4 " + ip).read()
    if "100.0% packet loss" in response:

        print(ip, "is unresponcive ")


#    else:
# print(ip, "is up")
