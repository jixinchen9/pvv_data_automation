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
metadata_filename = "3_Mercury_WT_13.6_LPB_FT4_YINLUN_PP_405kw_29C_meta_raw"

fields_to_collect = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
                   "\"Min\"",
                   "SDev"
    ]

fields_to_output = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
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
full_list = ncode_metadata.read_metadata(siefile_folder, metadata_files, fields_to_collect)

#optionally filter the full list or lists wrt channels
#short_list = ncode_metadata.filter_metadata(full_list, filter_folder, filter_filename)

#write the csv, optionally choose what attributes to output
'''
for index, summary in enumerate(full_list):
    def_output.write_csv(siefile_folder+metadata_files[index], fields_to_output, summary)
'''

'''
with open(siefile_folder+output_name,'w', newline = '') as f:
    f_writer = csv.writer(f)
    for i in range(len(full_list[0])):
        f_writer.writerow([""])
    f.close()

fields = fields_to_output
'''
with open(siefile_folder+metadata_files[0]+".csv",'r') as f:
    read_thing = csv.reader(f)
    list_of_rows=[]
    for j in read_thing:
        list_of_rows.append(j)
    f.close()

    
    