# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:11:30 2025

@author: jc16287
"""
import json

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
        
        efields_to_collect =[]
        for i in config['Attributes']:
            efields_to_collect.append(i.get('name'))
        f.close()
    
    return e_siefile_folder, efilter_folder, efilter_filename, ebatfile_folder, ebatfile_filename, ebatscript_filename, eoutput_name, efields_to_collect