# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 11:57:57 2025

@author: jc16287
"""
import sie_obj
import ncode_metadata
import config_builder
import time_slice_define
import gather_input
import scrape_export
import log_writer

import os
import regex as re

def create_export_objs():

    export_obj_list = []
    
    temp_file_list = os.listdir(config_builder.config_v2_inst.temp_path)
    
    for file in temp_file_list:
        file_path = config_builder.config_v2_inst.temp_path + "/" + file
        export_obj_list.append(sie_obj.sie_export(file_path, ncode_metadata.extract_file_name(file_path)))
        
    return export_obj_list

def make_set(input_str):
    
    word_list = re.split(r"[;,_\\ ]+" , input_str)
    lowercase_list = [item.lower() for item in word_list]
    word_set = set(lowercase_list)
    
    return word_set

def get_match_metric(export_name , slice_name):
    
    match_metric = len(make_set(export_name) & make_set(slice_name))
    
    return match_metric

def get_slice_ends(obj_file_name, time_slice_df):
    #compare word sets for each entry in time slice 
    if time_slice_df.empty:
        error2 = "empty timeslice search result, check file path input or hint strings.\n"
        print(error2)
        log_writer.create_log_entry(error2, log_writer.metadata_v01_log.content)
        
        return -1,-1
    
    find_slice_match_df = time_slice_df.copy(deep = True)
    find_slice_match_df['match_metric'] = find_slice_match_df['run_string'].apply(get_match_metric, args =(obj_file_name,))
    #store a match quantity for each entry
    #find the max match quantity entry

    slice_match = find_slice_match_df['match_metric'].idxmax()
    highest_metric = find_slice_match_df['match_metric'].max()
    
    if highest_metric >= config_builder.config_v2_inst.timeslice_min_match:
        
        match_name = find_slice_match_df.loc[slice_match, 'run_string']
        match_slice_start = find_slice_match_df.loc[slice_match, 'time_slice_start']
        match_slice_end = find_slice_match_df.loc[slice_match, 'time_slice_end']
        
        talk1 = f"\n matched '{obj_file_name}' temp file with '{match_name}' in labview summary with {highest_metric} words \n"
        print(talk1)
        log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
    
    else:
        match_slice_start = -1
        match_slice_end = -1
        
        error1 = r"could not match enough words, edit config if you think it's a good idea \n"
        print(error1)
        log_writer.create_log_entry(error1, log_writer.metadata_v01_log.content)
        
    return match_slice_start, match_slice_end
    # finally fill in the time slice attributes in the object from the df highest match entry
'''
local test


time_slice_df = time_slice_define.get_all_timeslice()

export_objs = create_export_objs()

chan_list = gather_input.get_filter_channels()

for export in export_objs:
    export.time_slice_start , export.time_slice_end = get_slice_ends(export.file_name , time_slice_df)
    export.ts_data = scrape_export.add_timeseries_df(export, chan_list)

obj_file_name = create_export_objs()[0].file_name


time_slice_str = time_slice_df.loc[17,'run_string']

slice_name_set = make_set(time_slice_str)
exp_name_set = make_set(obj_file_name)
'''