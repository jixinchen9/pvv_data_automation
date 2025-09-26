# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 10:33:28 2025

@author: jc16287
"""
import ncode_metadata
import re
import os
import subprocess
import config_builder
import operate_exports
import log_writer

def clear_temps():
    temp_list = os.listdir(config_builder.config_v2_inst.temp_path)
    
    for file in temp_list:
        full_path = config_builder.config_v2_inst.temp_path + "/" + file
        
        if os.path.exists(full_path):
            os.remove(full_path)
            
            talk1 = f"{file} was deleted !!\n"
            print(talk1)
            log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
            
        else:
            print(f"{file} not found ??")

def write_temps(input_file_list):
    
    batfile_abs = os.path.abspath(config_builder.config_v2_inst.libsie_path + "/" + config_builder.config_v2_inst.libsie_bat)
    source_abs = config_builder.config_v2_inst.source_cwd
    
    for file in input_file_list:
        edit_script(file)
        os.chdir(os.path.abspath(config_builder.config_v2_inst.libsie_path))
        os.system(batfile_abs)
        os.chdir(source_abs)
        
        

    
def edit_script(input_file_name):
    
    batch_file_abs_path = os.path.abspath(config_builder.config_v2_inst.libsie_path + "/" + config_builder.config_v2_inst.libsie_bat)
    
    with open(batch_file_abs_path) as f:
        batch_content = f.readline()
        f.close()
    '''
    just look for quote marks that signify the input and output
    '''
    filename_match = re.finditer(r"\"",batch_content)

    if filename_match: 
        input_file_start_idx = next(filename_match).end()
        input_file_end_idx = next(filename_match).start()
        
        output_file_start_idx = next(filename_match).end()
        output_file_end_idx = next(filename_match).start()
    
    else:
        error1 = "problem defining input of libsie batch script, check libsie batch script"
        print(error1)
        log_writer.create_log_entry(error1, log_writer.metadata_v01_log.content)
    
    
    temp_output_name =config_builder.config_v2_inst.temp_path  + "/" + ncode_metadata.extract_file_name(repr(input_file_name)) +"export.csv"
    
    talk1 = f"writing temp file: {temp_output_name}\n"
    print(talk1)
    log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
    
    with open(batch_file_abs_path, "w") as f:
        
        f.write(
            batch_content.replace(
            batch_content[input_file_start_idx:input_file_end_idx], input_file_name).replace(
                batch_content[output_file_start_idx:output_file_end_idx],os.path.abspath(temp_output_name))
                )
        
        f.close()
        
