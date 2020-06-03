# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:43:18 2020

@author: Whiterabbit2015
"""

import getpass
import sys
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print (tn.read_all)