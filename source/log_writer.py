# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:43:33 2025

@author: jc16287
"""
from datetime import datetime

def create_log():
    log_content = []
    current_time = datetime.now()
    log_content.append(f"{current_time}: Begin execution of ncode based script")
    
    return log_content

def log_entry(input_item, created_log):
    
    current_time = datetime.now()
    created_log.append(f"{current_time}: Begin execution of ncode based script")
    
    if isinstance(input_item, list):
        for i in input_item:
            created_log.append(i)
    
    else:
        created_log.append(input_item)