#!/usr/bin/python3

import os

mine = os.listdir('/home/grant/Projects/amari/tortuga/recipes')
theirs = os.listdir('/home/grant/Projects/amari/tortuga/dump/upneat')

for me in mine:
    if me in theirs:
        print(me)
