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
import log_writer

def get_all_timeslice():
    slice_files = gather_input.get_timeslice_file_path()
    all_slices = pd.DataFrame(columns=['run_string', 'slice'])
    
    for file in slice_files:
        if os.path.exists(file):
            
            talk1 = f"slice inputs file found here: {file}\n"
            print(talk1)
            log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
            
            new_slice_df = get_timeslice_df(file)
            all_slices = pd.concat([all_slices , new_slice_df])
            
            
        else:
            config_builder.config_v2_inst.timeslice_selection = 0
            
            talk2 = "slice input file not found, time series data will not slice\n"
            print(talk2)
            log_writer.create_log_entry(talk2, log_writer.metadata_v01_log.content)
    
    all_slices['time_slice_start'] = all_slices['slice'].apply(get_timeslice_start)
    all_slices['time_slice_end'] = all_slices['slice'].apply(get_timeslice_end)
    
    all_slices.index = range(len(all_slices))
    
    log_list = all_slices.to_numpy().flatten()
    talk3 = "time slice scrape complete:\n"
    print(talk3)
    log_writer.create_log_entry(talk3, log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(log_list, log_writer.metadata_v01_log.content)
    
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
    found_file_hint = (summary_df['file_srch'] == 0).any()
    found_slice_hint = (summary_df['slice_srch'] == 0 ).any()
    
    if found_slice_hint and found_file_hint:
        
        timeslice_df = (summary_df.loc[(summary_df['file_srch'] == 0)|(summary_df['slice_srch'] == 0)]).transpose()

        timeslice_df.columns = timeslice_df.iloc[0]

        timeslice_df['valid_slice'] = timeslice_df[slice_xls_row].str.find("-")
        timeslice_df = timeslice_df.loc[timeslice_df['valid_slice']>0].dropna(axis=1)

        timeslice_df = timeslice_df[col_to_keep]
        timeslice_df.columns = ['run_string', 'slice']
        
        talk1 = f"Found time slice and file name hints in {slice_file_path}\n"
        print(talk1)
        log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
        
        return timeslice_df
    
    else:
        config_builder.config_v2_inst.timeslice_selection = 0
        
        error1 = f"problem in {slice_file_path}\n One or both Hint String do not match, check summary file and script config\n"
        print(error1)
        log_writer.create_log_entry(error1, log_writer.metadata_v01_log.content)
        
        return pd.DataFrame(columns=['run_string', 'slice'])


'''
# a brief demonstration:
    
b_slice_file = r"\\fhxnas02\pdcteams\combine\Power Module\PV&V\Lab\Windtunnel\Tier 4 Final\Mercury_13.6L-S750 & 9.0L\04 Labview\Mercury 13.6L Application Approval\LPB FT4 Yinlun\LPB_FT4_Yinlun_Master.xls"
g_slice_file = r"\\fhxnas02\pdcteams\combine\Power Module\PV&V\Lab\Windtunnel\Tier 4 Final\Mercury_13.6L-S750 & 9.0L\04 Labview\Mercury 13.6L Application Approval\LPB FT4 Yinlun\A-108308_A-154687\WabcoProductionExhaust Tube.xls"
test_timeslice = get_timeslice_df(g_slice_file)
print(config_builder.config_v2_inst.timeslice_selection)
'''