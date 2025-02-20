# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:13:59 2025

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

#this is the only way to write inputs, by reading the config file
config_filename = "config.json"
   
siefile_folder, filter_folder, filter_filename, batfile_folder, batfile_filename, batscript_filename, output_name, fields_to_collect, output_folder = gather_input.read_config_metadata(config_filename)
#find all the sie files in the folder
sie_files = file_finder.find_sie(siefile_folder)

#make changes to the batch script file to include all sie files
#hit the batch file to create metadata files

run_ncode.edit_script(batfile_folder, batscript_filename, batfile_filename, sie_files, siefile_folder)

#find all the generated metadata files in the folder
metadata_files = file_finder.find_metadata_files(siefile_folder)

#run regex search on metadata files for collected attributes and place into appropriate data structure
full_df_tall = ncode_metadata.read_metadata_df(siefile_folder, metadata_files, fields_to_collect)

#optionally filter the full list or lists wrt channels
short_df = ncode_metadata.filter_metadata_df(full_df_tall, filter_folder, filter_filename)

#pivot the full list or filtered wrt to channels list to a 'wide' table, flattened
#based on filename
wide_df = pd.pivot(full_df_tall, index='ChanTitle', columns = ['Filename','Attribute'], values = 'value')

#write the csv
wide_df.to_csv(path_or_buf = output_folder+output_name+".csv")