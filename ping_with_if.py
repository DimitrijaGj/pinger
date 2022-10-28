#!/usr/bin/env python

import os

""" Taking IP from list pings it and returns if it is down"""
with open("list.txt") as ip_list:

    for ip in ip_list:
        # response = os.popen("ping -c 4 " + ip).read()
        response = os.popen("ping -c 2 " + ip).read()
        if "100.0% packet loss" in response:
            print(ip, "is unresponcive  👎  ")


#    else:
# print(ip, "is up")
# with 4 pings ended in 1min 50 sec
# with 1 ping endet in 13 sec
# with 2 pings ended in 30 sec
