# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 10:45:26 2025

@author: jc16287
"""

import regex as re
import pandas as pd
import csv
# import os
# import json

import file_finder
import def_output
import ncode_metadata
import run_ncode
import gather_input
import log_writer
'''
reconfigure original metadata writer to be easy input, and work in a remote folder

'''
#this is the only way to write inputs, by reading the config file
config_filename = "../config/config.json"
#start log
mw_log = log_writer.create_log()

siefile_folder_dep, filter_folder, filter_filename, batfile_folder, batfile_filename, batscript_filename, output_name, fields_to_collect, output_folder, ncode_app_path = gather_input.read_config_metadata(config_filename)

#temporary magic path take note
data_input = "../input/metadata_writer/Data_Automation_Benchmark_Data.csv"

files, folders = gather_input.gather_group(data_input)

sie_files, files_not_found = file_finder.get_full_paths(files, folders)

#write the file search log entries

#make changes to the batch script file to include all sie files
#hit the batch file to create metadata files

run_ncode.edit_script(batfile_folder, batscript_filename, batfile_filename, sie_files)

#find all the generated metadata files in the folder abs paths
metadata_files = file_finder.find_meta_files_multifolder(folders)

#run regex search on metadata files for collected attributes and place into appropriate data structure
full_df_tall = ncode_metadata.read_metadata_df(metadata_files, fields_to_collect)

#optionally filter the full list wrt channels
short_df = ncode_metadata.filter_metadata_df(full_df_tall, filter_folder, filter_filename)

#pivot the full list or filtered wrt to channels list to a 'wide' table, flattened
#based on filename
wide_df = pd.pivot(short_df, index='ChanTitle', columns = ['Filename','Attribute'], values = 'value')

#write the csv
wide_df.to_csv(path_or_buf = output_folder + "/" + output_name+".csv")