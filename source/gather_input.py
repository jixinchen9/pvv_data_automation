# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:11:30 2025

@author: jc16287
"""
import json
import regex as re
import pandas as pd
import os
import log_writer
import config_builder

def read_config_metadata(filename):
    
    abs_filename = os.path.abspath(filename) 
    with open(abs_filename) as f:
        config = json.load(f)
        
        e_siefile_folder = config['Input']['path']
        
        efilter_folder = config['Filter']['path']
        efilter_filename = config['Filter']['filename']
        
        ebatfile_folder = config['ncode']['path']
        ebatfile_filename = config['ncode']['batfile']
        ebatscript_filename = config['ncode']['batch_script']
        
        eoutput_name = config['Output']['filename']
        eoutput_path = config['Output']['path']
        
        encode_app_path = config['ncode_app']['path']
        
        efields_to_collect =[]
        for i in config['Attributes']:
            efields_to_collect.append(i.get('name'))
        f.close()
    
    return e_siefile_folder, efilter_folder, efilter_filename, ebatfile_folder, ebatfile_filename, ebatscript_filename, eoutput_name, efields_to_collect, eoutput_path, encode_app_path

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
    
    log_writer.create_log_entry("will look for these files:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(files, log_writer.metadata_v01_log.content)
    
    log_writer.create_log_entry("will look in these folders:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(folders, log_writer.metadata_v01_log.content)
    
    return files, folders

def get_full_paths(file_list, folder_list):
    # list comprehension ya dig
    full_path_list = []

    for row in folder_list:
        
        files_found = os.listdir(row)
        #matched_files = [item for item in files_found if any(substring in item for substring in file_list)]
        matched_files_os, matched_files_query = case_insensitive_search(file_list, files_found)
        
        for i in matched_files_os:
            full_path_list.append(row + "\\" + i )
        
        
    not_found_files = list(set(file_list) - set(matched_files_query))

    return full_path_list, not_found_files, 

def case_insensitive_search(needle_list, haystack_list):
    result_list = []
    found_counter = []
    
    for i in needle_list:
        for j in haystack_list:
            
            if i.lower() in j.lower():
                result_list.append(j)
                found_counter.append(i)
                break
                
    return result_list, found_counter

def gather_group_clean():
    
    collect_line = False
    search_result = []
    
    input_file = config_builder.config_v2_inst.input_path + "/" + config_builder.config_v2_inst.input_data
    
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
    
    log_writer.create_log_entry("will look for these files:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(files, log_writer.metadata_v01_log.content)
    
    log_writer.create_log_entry("will look in these folders:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(folders, log_writer.metadata_v01_log.content)
    
    return files, folders

def get_timeslice_file_path():
    
    input_file = config_builder.config_v2_inst.input_path + "/" + config_builder.config_v2_inst.input_data
    collect_line = False
    search_result = []
    
    with open(input_file) as f:
        data_contents = f.readlines()
        
        for line in data_contents:
            if "timeslice_full_path_start" in line:
                collect_line = True
                continue
            
            if "timeslice_full_path_end" in line:
                collect_line = False
            
            if collect_line:
                search_result.append(line.rstrip('\n'))
        
        f.close()
    
    return search_result
