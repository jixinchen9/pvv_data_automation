# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 10:45:26 2025

@author: jc16287
"""

import regex as re
import pandas as pd
import csv
import os
# import json

import file_finder
import def_output
import ncode_metadata
import gather_input
import log_writer
import run_libsie
import config_builder
import time_slice_define
import operate_exports
import scrape_export
'''
reconfigure original metadata writer to be easy input, and work in a remote folder

'''
os.chdir(config_builder.config_v2_inst.source_cwd)
print(os.getcwd())

files, folders = gather_input.gather_group_clean()

sie_files, files_not_found = file_finder.get_full_paths(files, folders)

run_libsie.clear_temps()
run_libsie.write_temps(sie_files)

time_slice_df = time_slice_define.get_all_timeslice()

export_objs = operate_exports.create_export_objs()

chan_list = gather_input.get_filter_channels()

for export in export_objs:
    export.time_slice_start , export.time_slice_end = operate_exports.get_slice_ends(export.file_name , time_slice_df)
    export.ts_data = scrape_export.add_timeseries_df(export, chan_list)
'''

#find all the generated metadata files in the folder abs paths
metadata_paths, metadata_files = file_finder.find_meta_files_multifolder(folders)

#run regex search on metadata files for collected attributes and place into appropriate data structure
full_df_tall = ncode_metadata.read_metadata_df(metadata_paths, fields_to_collect)

#optionally filter the full list wrt channels
short_df = ncode_metadata.filter_metadata_df(full_df_tall, filter_folder, filter_filename)

#pivot the full list or filtered wrt to channels list to a 'wide' table, flattened
#based on filename
wide_df = pd.pivot(short_df, index='ChanTitle', columns = ['Filename','Attribute'], values = 'value')

#write the csv
wide_df.to_csv(path_or_buf = output_folder + "/" + output_name+".csv")

#save logging file
log_writer.save_log(log_writer.metadata_v01_log.content, output_folder)
'''