#!/usr/bin/env python

import os

# first import the lybraries

""" open the IP list """

""" parse trough the list """

""" ping the IPs 
"""
print("#" * 60)
print("-" * 60)
ip_to_check = input("Pls enter IP...")
print("-" * 60)
os.system("ping -c 4 {}".format(ip_to_check))
print("*" * 60)

input("Press ENTER to exit.")
