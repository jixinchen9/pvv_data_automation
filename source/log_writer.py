# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:43:33 2025

@author: jc16287
"""
from datetime import datetime
import config_builder
import os

class run_log:
    def __init__(self,content):
      self.content = content
  
    def display_content(self):
        for i in self.content:
            print(i)
'''
create module level instance, which is effectively a singleton instance
'''

current_time = datetime.now()
metadata_v01_log = run_log([f"{current_time}: executing...\n"])

def create_log():
    log_content = []
    current_time = datetime.now()
    log_content.append(f"{current_time}: Begin execution of ncode based script")
    
    return log_content

def create_log_entry(input_item, created_log):
    
    current_time = datetime.now()
    created_log.append(f"\n{current_time}::\n")
    
    if isinstance(input_item, list):
        for i in input_item:
            created_log.append(i)
    
    else:
        created_log.append(input_item)

def save_log_clean():
    
    output_file = config_builder.config_v2_inst.log_name
    folder = config_builder.config_v2_inst.log_path
    
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    
    os.chdir(config_builder.config_v2_inst.source_cwd)
    print(os.getcwd())
    
    with open(folder + "/" + output_file + formatted_time + ".txt", 'w') as f:
        
        for k in metadata_v01_log.content:
            f.write(f"{k}\n")
        f.close()
        
def save_log(log_contents,folder):
    
    output_file = "run log of deprecated script"

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    
    with open(folder + "/" + output_file + formatted_time + ".txt", 'w') as f:
        for k in log_contents:
            f.write(f"{k}\n")
        f.close()
        