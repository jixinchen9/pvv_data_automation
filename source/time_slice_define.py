# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:22:20 2025

@author: jc16287
"""

import config_builder
import pandas as pd
import gather_input
import regex as re
import os 


def get_all_timeslice():
    slice_files = gather_input.get_timeslice_file_path()
    all_slices = pd.DataFrame(columns=['run_string', 'slice'])
    
    for file in slice_files:
        if os.path.exists(file):
            print(f"slice inputs found in {file}")
            new_slice_df = get_timeslice_df(file)
            all_slices = pd.concat([all_slices , new_slice_df])
            
        else:
            config_builder.config_v2_inst.timeslice_selection = 0
            print("slice input not found, time series data will not slice")
    
    all_slices['time_slice_start'] = all_slices['slice'].apply(get_timeslice_start)
    all_slices['time_slice_end'] = all_slices['slice'].apply(get_timeslice_end)
    
    all_slices.index = range(len(all_slices))
    
    return all_slices
'''
helper functions to turn scraped string type times slice into integer 
'''
def get_timeslice_start(slice_str):
    dash = re.search(r"-" , slice_str)
    
    if dash:
        return int(slice_str[:dash.start()])
    
    else:
        return -1
    
def get_timeslice_end(slice_str):
    dash = re.search(r"-" , slice_str)
    
    if dash:
        return int(slice_str[dash.end():])
    
    else:
        return -1
'''
the heavy lifting of the time slice scrape

makes use of hint strings that can be defined in the config, currently you have to add the 
word 'time_slice' into the row that the slices are in in the labview xls
the test labels happen to be in the row 'CAC', these are configurable in the json file


'''
def get_timeslice_df(slice_file_path):
    
    summary_df = pd.read_excel(slice_file_path, sheet_name='Master Summary')

    file_xls_row = config_builder.config_v2_inst.timeslice_file_hint
    slice_xls_row = config_builder.config_v2_inst.timeslice_time_hint
    col_to_keep = [file_xls_row,slice_xls_row]

    summary_df['file_srch'] = summary_df['Project'].str.find(file_xls_row)
    summary_df['slice_srch'] = summary_df['Project'].str.find(slice_xls_row)
    
    #if there are nothing except -1 in the new slice srch column, then this funciton should terminate, time slice option should set to zero
             
    timeslice_df = (summary_df.loc[(summary_df['file_srch'] == 0)|(summary_df['slice_srch'] == 0)]).transpose()

    timeslice_df.columns = timeslice_df.iloc[0]

    timeslice_df['valid_slice'] = timeslice_df[slice_xls_row].str.find("-")
    timeslice_df = timeslice_df.loc[timeslice_df['valid_slice']>0].dropna(axis=1)

    timeslice_df = timeslice_df[col_to_keep]
    timeslice_df.columns = ['run_string', 'slice']
    
    return timeslice_df

