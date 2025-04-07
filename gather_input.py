# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:11:30 2025

@author: jc16287
"""
import json
import regex as re
import pandas as pd
import os

def read_config_metadata(filename):
     
    with open(filename) as f:
        config = json.load(f)
        
        e_siefile_folder = config['Input']['path']
        
        efilter_folder = config['Filter']['path']
        efilter_filename = config['Filter']['filename']
        
        ebatfile_folder = config['ncode']['path']
        ebatfile_filename = config['ncode']['batfile']
        ebatscript_filename = config['ncode']['batch_script']
        
        eoutput_name = config['Output']['filename']
        eoutput_path = config['Output']['path']
        
        efields_to_collect =[]
        for i in config['Attributes']:
            efields_to_collect.append(i.get('name'))
        f.close()
    
    return e_siefile_folder, efilter_folder, efilter_filename, ebatfile_folder, ebatfile_filename, ebatscript_filename, eoutput_name, efields_to_collect, eoutput_path

def read_config_EAR_eval(filename):
    
    with open(filename) as f:
        config = json.load(f)
        
        req_path = config['Requirement']['path']
        data_path = config['Data']['path']
        f.close()
    
    return req_path, data_path

def gather_group(input_file):
    
    collect_line = False
    search_result = []

    with open(input_file) as f:
        data_contents = f.readlines()
        
        for line in data_contents:
            if "file_start" in line:
                collect_line = True
                group_number = re.search("[0-99]",line).group()
                row_type = "file"
                continue
            
            if "file_end" in line:
                group_number = None
                row_type = None
                collect_line = False
                
            if "path_start" in line:
                collect_line = True
                group_number = re.search("[0-99]",line).group()
                row_type = "path"
                continue
                
            if "path_end" in line:
                collect_line = False
                group_number = None
                row_type = None
                
                
            if collect_line:
                #print(line)
                search_result.append([row_type, group_number, line.rstrip('\n')])
        
        f.close()
        
    inputs_df = pd.DataFrame(search_result, columns = ['Type', 'group', 'name'])
    
    # The following is not quite right, it ignores groups, correct soon
    files = inputs_df.loc[inputs_df['Type']=='file']['name'].tolist()
    folders = inputs_df.loc[inputs_df['Type']=='path']['name'].tolist()
        
    return files, folders

def get_full_paths(file_list, folder_list):
    # list comprehension ya dig
    full_path_list = []
    
    for row in folder_list:
        files_found = os.listdir(row)
        matched_files = [item for item in files_found if any(substring in item for substring in file_list)]
        
        for i in matched_files:
            full_path_list.append(row + "\\" + i )
    
    return full_path_list