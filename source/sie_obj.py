# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:12:18 2025

@author: jc16287
"""

import pandas as pd

ts_df_column_name = ['time_stamp' , 'measure_value', 'measure_name' , 'file_name']

class sie_export:
    
    def __init__(self, file_path, file_name, ts_data = pd.DataFrame(columns=ts_df_column_name), time_slice_start = -1, time_slice_end= -1):
        self.file_path = file_path
        self.file_name = file_name
        self._ts_data = ts_data
        self.time_slice_start = time_slice_start
        self.time_slice_end = time_slice_end
        
    def get_ts_data(self):
        return self._ts_data
    
    def set_ts_data(self, input_df):
        sliced_df = pd.DataFrame(columns=['time_stamp' , 'measure_value', 'measure_name' , 'file_name'])
        test_channels = input_df['measure_name'].unique()
        
        slice_start = self.time_slice_start
        slice_end = self.time_slice_end
        
        if not input_df.empty:
            current_file = input_df.loc[0]['file_name']
        
        for channel in test_channels:
            
            current_channel_df = input_df[input_df['measure_name'] == channel ]
            
            current_ts_min = current_channel_df['time_stamp'].min()
            current_ts_max = current_channel_df['time_stamp'].max()
            
            if slice_start >= current_ts_min and slice_start <= current_ts_max:
                current_channel_df = current_channel_df[current_channel_df['time_stamp'] >= slice_start]
                
            else:
                error2 = f"timeslice start outside of possible range in {current_file}, data not sliced\n"
                print(error2)
                
            if slice_end <= current_ts_max and slice_end >= current_ts_min:
                current_channel_df = current_channel_df[current_channel_df['time_stamp'] <= slice_end]

            else: 
                error4 = f"timeslice start outside of possible range in {current_file} , data not sliced\n"
                print(error4)
                
            sliced_df = pd.merge(sliced_df, current_channel_df, how='outer') 
        
        self._ts_data = sliced_df
        


 
#define getter setter for only the ts_data attribute, can play with slices