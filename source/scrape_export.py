# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:50:37 2025

@author: jc16287
"""
import gather_input
import pandas as pd
import regex as re

'''
for a single export obj:
    first find all indices of channel name matches
    create x number of channel data lists using general scrape for each index
    change lines in the list to numbers and add into dataframe
    create 1 dataframe per export obj by combining all dfs for each channel specified
    
'''
def make_channel_df(ts_list, channel_name, file_name):
    #should be able to fully nest
    new_df = pd.DataFrame(columns=['time_stamp' , 'measure_value', 'measure_name' , 'file_name'])

    for datapoint in ts_list:
        #i think it's ok to put extremely specific and non configurable string searches here, the temp files are made by a computer
        
        timestamp_pattern = r":\s*(\d+),"
        meas_value_pattern = r"(?<=,)\s*(.*)"
        
        timestamp_match = re.search(timestamp_pattern , datapoint)
        meas_value_match = re.search(meas_value_pattern , datapoint)

        if timestamp_match and meas_value_match:
            timestamp = float(re.findall(timestamp_pattern , datapoint)[0])
            meas_value = float(re.search(meas_value_pattern , datapoint).group().strip())
            
            new_row = {'time_stamp' : timestamp,
                                 'measure_value' : meas_value,
                                 'measure_name' : channel_name,
                                 'file_name' : file_name}
            
            new_df.loc[len(new_df)] = new_row
            
    return new_df
  
def add_timeseries_df(exp_obj, channel_list):
    
    with open(exp_obj.file_path) as f:
        all_lines = f.readlines()
        
        f.close()

    time_series_df = pd.DataFrame(columns=['time_stamp' , 'measure_value', 'measure_name' , 'file_name'])

    for index, line in enumerate(all_lines):
        for channel in channel_list:
            #i think it's ok to put extremely specific and non configurable string searches here, the temp files are made by a computer
            if (channel in line) and ("somat:input_channel" in line):

                ts_list = gather_input.general_scrape(all_lines[index:], "Data block 0", "Channel id")
                time_series_df = pd.merge(time_series_df, make_channel_df(ts_list, channel, exp_obj.file_name), how='outer' )
    
    return time_series_df
    print()