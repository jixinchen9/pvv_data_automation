# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:22:20 2025

@author: jc16287
"""

import config_builder
import pandas as pd
import gather_input




def get_timeslice_df():
    summary_df = pd.read_excel(gather_input.get_timeslice_file_path()[0], sheet_name='Master Summary')

    file_xls_row = config_builder.config_v2_inst.timeslice_file_hint
    slice_xls_row = config_builder.config_v2_inst.timeslice_time_hint
    col_to_keep = [file_xls_row,slice_xls_row]

    summary_df['file_srch'] = summary_df['Project'].str.find(file_xls_row)
    summary_df['slice_srch'] = summary_df['Project'].str.find(slice_xls_row)
             
    timeslice_df = (summary_df.loc[(summary_df['file_srch'] == 0)|(summary_df['slice_srch'] == 0)]).transpose()

    timeslice_df.columns = timeslice_df.iloc[0]

    timeslice_df['valid_slice'] = timeslice_df[slice_xls_row].str.find("-")
    timeslice_df = timeslice_df.loc[timeslice_df['valid_slice']>0].dropna(axis=1)

    timeslice_df = timeslice_df[col_to_keep]
    timeslice_df.columns = ['run_string', 'slice']
    
    return timeslice_df

df = get_timeslice_df()