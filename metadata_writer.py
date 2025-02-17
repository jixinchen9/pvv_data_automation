# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:13:59 2025

@author: jc16287
"""
import regex as re
import csv
import os

import file_finder
import def_output
import ncode_metadata
import run_ncode
'''
++++++++++++++++++++++++O+++++++++++++++++++++++O++++++++++++++++++++++++++++++
'''

siefile_folder = "D:\\086 local test ncode\\"
#metadata_filename = "3_Mercury_WT_13.6_LPB_FT4_YINLUN_PP_405kw_29C_meta_raw"

fields_to_collect = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
                   "\"Min\"",
                   "SDev"
    ]

fields_to_output = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
                   "\"Min\"",
                   "SDev"
    ]

filter_folder = "D:\\086 local test ncode\\"
filter_filename = "Channel_list_example.csv"

batfile_folder = "D:\\086 local test ncode\\"
batfile_filename = "metadata_export_01.bat"
batscript_filename = "metadata_export_01.script"

output_name = "metadata_all_output.csv"

'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

#find all the sie files in the folder
sie_files = file_finder.find_sie(siefile_folder)

#make changes to the batch script file to include all sie files
#hit the batch file to create metadata files

#run_ncode.edit_script(batfile_folder, batscript_filename, batfile_filename, sie_files)

#find all the generated metadata files in the folder
metadata_files = file_finder.find_metadata_files(siefile_folder)

#run regex search on metadata files for collected attributes and place into appropriate data structure
full_list_tall = ncode_metadata.read_metadata(siefile_folder, metadata_files, fields_to_collect)

#optionally filter the full list or lists wrt channels
#short_list = ncode_metadata.filter_metadata(full_list_tall, filter_folder, filter_filename)

#pivot the full list or filtered wrt to channels list to a 'wide' table, flattened
#based on filename
pivoted_list = def_output.wide_table(full_list_tall, sie_files, fields_to_output)

#write the csv
def_output.write_csv(pivoted_list,output_name)