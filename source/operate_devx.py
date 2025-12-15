# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 10:21:06 2025

@author: jc16287
"""

import config_builder
import log_writer
import pandas as pd
import os
import gather_input

with open('test_path.txt') as f:
     content = f.readlines()


def find_devx_file_data_start (devx_file):
    '''
    
    Parameters
    ----------
    devx_file : this is the full path of the devx data

    Returns index of the start of data, which is the row with channel names
    -------


    '''
    with open(devx_file) as f:
        devx_csv = f.readlines()

    
    found_start = False
    
    for index, line in enumerate(devx_csv):
        
        if line.startswith(config_builder.config_v2_inst.devx_trim_hint):
            
            #print(line,"is on this line", index)
            return index
            found_start = True
            
    if (found_start == False):
        
        return -1

def make_df_all (devx_file):
    '''
  
    Parameters
    ----------
    devx_file : full path of devx data, extracted from input file

    Returns a tall dataframe of all time series data in the same schema as export obj time series
    -------
    None.

    '''
    common_df_order = ['time_stamp' , 'measure_value', 'measure_name' , 'file_name']
    devx_folder , devx_filename = os.path.split(devx_file)
    
    trim_index = find_devx_file_data_start(devx_file)
    
    if (trim_index == -1):
        talk1 = f"hint string {config_builder.config_v2_inst.devx_trim_hint} not found in {content[0]}, check file and config, devx scrape not possible"
        print(talk1)
        log_writer.create_log_entry(talk1 , log_writer.metadata_v01_log.content)
        
        return pd.DataFrame(columns = common_df_order)      
        #return empties if first row identification did not work
        
    devx_df = pd.read_csv(devx_file , skiprows = trim_index)

    df_columns_all = devx_df.columns.tolist()

    column_to_remove = [config_builder.config_v2_inst.devx_trim_hint] #remove the time column from column list of channels so df can un-pivot

    channels_list = [channel for channel in df_columns_all if channel not in column_to_remove]

    devx_df_tall = pd.melt(devx_df , id_vars = config_builder.config_v2_inst.devx_trim_hint, value_vars = channels_list, var_name='measure_name' , value_name = 'measure_value')
    devx_df_tall.rename(columns={'Time':'time_stamp'},inplace=True)

    devx_df_tall['file_name'] = devx_filename

    talk2 = f"\n Devx data collected from: *{devx_filename}*\n"
    print(talk2)
    log_writer.create_log_entry(talk2 , log_writer.metadata_v01_log.content)
    
    return devx_df_tall[common_df_order]

'''
local test
'''
'''    
all_devx_ts_df  =   make_df_all(content[0])

channel_desired = gather_input.get_filter_channels()

devx_desired_df = all_devx_ts_df[all_devx_ts_df['measure_name'].isin(channel_desired)]
'''