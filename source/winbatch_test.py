# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:21:39 2025

@author: jc16287
"""
import os

config_file = "../config/config.json"
real_path = os.path.abspath(config_file)
'''


'''
with open(real_path) as f:
    lies = f.readlines()
    for line in lies:
        print(line)
print("batch test success!")
