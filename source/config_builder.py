# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 10:12:06 2025

clean up config processing, to dict is a deprecated method, will create a singleton class object to serve as global 
varible for configurations

@author: jc16287
"""

import json
import os

class script_config:
    
    def __init__(self, name,  **config_field):
        
        self.name = name
        for key, value in config_field.items():
            setattr(self, key, value)
          
with open("../config/V02/config_v2.json") as f:
    config = json.load(f)
    f.close()

config_v2_inst = script_config("v2",
                               input_path = config['Input']['path'],
                               input_data = config['Input']['data'],
                               input_req = config['Input']['requirement'],
                               filter_folder = config['Filter']['path'],
                               filter_filename = config['Filter']['filename'],
                               ncode_bat_folder = config['ncode']['path'],
                               ncode_bat = config['ncode']['batfile'],
                               ncode_script = config['ncode']['batch_script'],
                               output_name = config['Output']['filename'],
                               output_path = config['Output']['path'],
                               ncode_app_path = config['ncode_app']['path'],
                               #timeslice_path = config['timeslice']['path'],
                               #timeslice_file = config['timeslice']['filename'],
                               libsie_path = config['libsie']['path'],
                               libsie_bat = config['libsie']['batfile'],
                               libsie_path_hint = config['libsie']['path_hint'],
                               temp_path = config['temp']['path'],
                               log_path = config['log']['path'],
                               log_name = config['log']['filename'],
                               source_cwd = os.getcwd(),
                               timeslice_selection = config['timeslice']['option'],
                               timeslice_file_hint = config['timeslice']['helper_test'],
                               timeslice_time_hint = config['timeslice']['helper_slice'],
                               timeslice_min_match = config['timeslice']['minimum_match'],
                               req_path = config['requirement']['path'],
                               req_file = config['requirement']['filename'],
                               req_name_index = config['requirement']['name_idx'],
                               req_limit_index = config['requirement']['limit_idx'],
                               req_compare_index = config['requirement']['compare_idx'],
                               req_metadata_type_index = config['requirement']['metadata_type_idx'],
                               req_formula_index = config['requirement']['formula_idx'],
                               req_channels_index = config['requirement']['channels_idx'],
                               devx_trim_hint = config['devx']['trim_hint'],
                               devx_path_hint = config['devx']['path_hint']
                               #source_cwd = config['start']['path']
)

def read_config_to_dict(filename):
    e_config = {}
    abs_filename = os.path.abspath(filename) 
    with open(abs_filename) as f:
        config = json.load(f)
        
        e_config.update({"input_path":config['Input']['path']})
        e_config.update({"input_data":config['Input']['data']})
        e_config.update({"input_req":config['Input']['requirement']})
        
        e_config.update({"filter_folder" : config['Filter']['path']})
        e_config.update({"filter_filename" : config['Filter']['filename']})
        
        e_config.update({"ncode_bat_folder" : config['ncode']['path']})
        e_config.update({"ncode_bat" : config['ncode']['batfile']})
        e_config.update({"ncode_script" : config['ncode']['batch_script']})
        
        e_config.update({"output_name" : config['Output']['filename']})
        e_config.update({"output_path" : config['Output']['path']})
        
        e_config.update({"ncode_app_path" : config['ncode_app']['path']})
        
        e_config.update({"timeslice_path" : config['timeslice']['path']})
        e_config.update({"timeslice_file" : config['timeslice']['filename']})
        
        e_config.update({"libsie_path" : config['libsie']['path']})
        e_config.update({"libsie_bat" : config['libsie']['batfile']})
        
        e_config.update({"temp_path" : config['temp']['path']})
        
        e_config.update({"log_path" : config['log']['path']})
        e_config.update({"log_name" : config['log']['filename']})
        
        f.close()
    
    return e_config