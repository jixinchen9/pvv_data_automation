# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:13:59 2025

@author: jc16287
"""
# import regex as re
# import csv
# import os
# import json

import file_finder
import def_output
import ncode_metadata
import run_ncode
import gather_input

#this is the only way to write inputs, by reading the config file
config_filename = "config.json"
   
siefile_folder, filter_folder, filter_filename, batfile_folder, batfile_filename, batscript_filename, output_name, fields_to_collect = gather_input.read_config_metadata(config_filename)

#find all the sie files in the folder
sie_files = file_finder.find_sie(siefile_folder)

#make changes to the batch script file to include all sie files
#hit the batch file to create metadata files

run_ncode.edit_script(batfile_folder, batscript_filename, batfile_filename, sie_files, siefile_folder)

#find all the generated metadata files in the folder
metadata_files = file_finder.find_metadata_files(siefile_folder)

#run regex search on metadata files for collected attributes and place into appropriate data structure
full_list_tall = ncode_metadata.read_metadata(siefile_folder, metadata_files, fields_to_collect)

#optionally filter the full list or lists wrt channels
short_list = ncode_metadata.filter_metadata(full_list_tall, filter_folder, filter_filename)

#pivot the full list or filtered wrt to channels list to a 'wide' table, flattened
#based on filename
pivoted_list = def_output.wide_table(short_list, sie_files, fields_to_collect)

#write the csv
def_output.write_csv(pivoted_list,output_name)