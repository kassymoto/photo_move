# -*- coding: utf-8 -*-
"""
Created on Mon May  7 23:29:31 2018

@author: vocal
"""

import os
import datetime
import shutil

path_from = r'J:\DCIM\100CANON'
path_to = r'F:\lightroom'

for x in os.listdir(path_from):
    direc = os.listdir(path_to)
    times = os.path.getctime(path_from + './' + x)
    date = datetime.date.fromtimestamp(times)

    if not str(date) in direc:
        os.mkdir(path_to + './' + str(date))
    shutil.move(path_from + './' + x , path_to + './' + str(date) +'/'+ x)