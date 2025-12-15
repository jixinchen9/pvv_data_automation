# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 10:45:26 2025

@author: jc16287
"""

import regex as re
import pandas as pd
#import csv
import os
# import json

import file_finder
import def_output
#import ncode_metadata
import gather_input
import log_writer
import run_libsie
import config_builder
import time_slice_define
import operate_exports
import scrape_export
import operate_devx
'''
reconfigure original metadata writer to be easy input, and work in a remote folder

and now w time slicing!

'''
os.chdir(config_builder.config_v2_inst.source_cwd)
print(os.getcwd())

files, folders = gather_input.file_folder_helper()

sie_files, devx_files, files_not_found = file_finder.get_full_paths(files, folders)

#run the libsie exe to generate temp files
run_libsie.clear_temps()
run_libsie.write_temps(sie_files)

time_slice_df = time_slice_define.get_all_timeslice()

#export_objs = operate_exports.create_export_objs()
export_objs = operate_exports.create_data_objs(operate_exports.make_sie_exp_list()) + operate_exports.create_data_objs(devx_files)

chan_list = gather_input.get_filter_channels()

tall_result = def_output.make_empty_result_df()

for export in export_objs:
    
    if config_builder.config_v2_inst.timeslice_selection:
        export.time_slice_start , export.time_slice_end = operate_exports.get_slice_ends(export.file_name , time_slice_df)
    else:
        talk4 = "time slicing optioned off, see config\n"
        print(talk4)
        log_writer.create_log_entry(talk4, log_writer.metadata_v01_log.content)
        
    
    if file_finder.is_sie(export.file_path):
        
        export.set_ts_data(scrape_export.add_timeseries_df(export, chan_list))
        print(f"{export.file_path} is an sie export.\n") 
    
    elif file_finder.is_devx(export.file_path):
        
        all_devx_ts_df  =   operate_devx.make_df_all(export.file_path)
        devx_desired_df = all_devx_ts_df[all_devx_ts_df['measure_name'].isin(chan_list)].reset_index(drop=True)
        
        export.set_ts_data(devx_desired_df)
        print(f"{export.file_path} is an devx file.\n")
   
    else:
        print(f"{export.file_path} is neither devx file nor sie export, no operations possible.\n")

    tall_result = pd.merge(tall_result , def_output.calc_aggs(export), how='outer')

#write the csv
tall_result.to_csv(path_or_buf = config_builder.config_v2_inst.output_path + "/" + config_builder.config_v2_inst.output_name+".csv")

#save logging file
log_writer.save_log_clean()
