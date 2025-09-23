# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:12:18 2025

@author: jc16287
"""

import pandas as pd

ts_df_column_name = ['time','value','measure_name']

class sie_export:
    
    def __init__(self, file_path, file_name, ts_data = pd.DataFrame(columns=ts_df_column_name), time_slice_start = -1, time_slice_end= -1):
        self.file_path = file_path
        self.file_name = file_name
        self.ts_data = ts_data
        self.time_slice_start = time_slice_start
        self.time_slice_end = time_slice_end
        
