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
        print("problem defining input of libsie batch script")
    
    
    temp_output_name =config_builder.config_v2_inst.temp_path  + "/" + ncode_metadata.extract_file_name(repr(input_file_name)) +"export.csv"
    print(f"writing temp file: {temp_output_name}\n")
    
    with open(batch_file_abs_path, "w") as f:
        
        f.write(
            batch_content.replace(
            batch_content[input_file_start_idx:input_file_end_idx], input_file_name).replace(
                batch_content[output_file_start_idx:output_file_end_idx],os.path.abspath(temp_output_name))
                )
        
        f.close()
        
'''
temp_output_folder = "../temp"
input_file_name =r"\\fhxnas02\pdcteams\combine\Power Module\PV&V\Lab\Windtunnel\Tier 4 Final\Mercury_13.6L-S750 & 9.0L\03 eDaq\Mercury 13.6L Application Approval\LPB FT4 Yinlun\1_Mercury_WT_13.6_LPB_FT4_YINLUN_InitialFill_Dearation_.sie"

libsie_batch = "output_temp.bat"
libsie_path = "./x64"

with open(libsie_path + "/" + libsie_batch) as f:
    batch_content = f.readline()
    f.close()

temp_output_name =temp_output_folder  + "/" + ncode_metadata.extract_file_name(repr(input_file_name)) +"export.csv"


filename_match = re.finditer(r"\"",batch_content)

if filename_match: 
    
    input_file_start_idx = next(filename_match).end()
    input_file_end_idx = next(filename_match).start()
    
    output_file_start_idx = next(filename_match).end()
    output_file_end_idx = next(filename_match).start()
    
    print(batch_content[input_file_start_idx:input_file_end_idx])
    print(batch_content[output_file_start_idx:output_file_end_idx])
    
    new_batch_content = batch_content.replace(
        batch_content[input_file_start_idx:input_file_end_idx],input_file_name).replace(
            batch_content[input_file_start_idx:input_file_end_idx],input_file_name)
else:
    print("problem defining input of libsie batch script")
    
with open("test_bat.txt", "w") as f:
    f.write(batch_content.replace(batch_content[input_file_start_idx:input_file_end_idx], input_file_name))
'''