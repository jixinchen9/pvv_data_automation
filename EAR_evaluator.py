# -*- coding: utf-8 -*-
"""

Created on Tue Apr  1 13:56:07 2025

@author: jc16287

EAR_evaluation, it's time to figure out if we meet requirements

"""
import gather_input
import Scrape_EAR

import regex as re
import pandas as pd
import os
import math
import numpy as np
'''
input file is in 2 parts, data has all folder paths and file names, with optional group number 
that can be used in conjunction with requirement sheet input field
requirement sheet is just that, requirements, relevant channels, how to evaluate requirement, and group number
which is not yet generalized
 
'''

config_file = "config_EAR_eval.json"

requirement_input, data_input = gather_input.read_config_EAR_eval(config_file)

"""
find the files listed in input file in the possible folder locations, store full paths in
'found all files'
"""


files, folders = gather_input.gather_group(data_input)

found_all_files = gather_input.get_full_paths(files, folders)

'''
There is always a labview
'''

master_sheet_path = [i for i in found_all_files if "Labview" in i and "Master" in i]

general_labview_paths = [i for i in found_all_files if "Labview" in i]

#'3' is the magic number of rows to skip ;)

lv_summary_df = pd.read_excel(master_sheet_path[0], "Master Summary", skiprows=3)
lv_summary_df = lv_summary_df.fillna('')

#print(lv_summary_df.loc[lv_summary_df['CAC'] == 'Compressor Inlet Temp', file].values[0])

"""
read the EAR input document into structure
"""
requirement_input_df =  pd.read_csv(requirement_input).fillna('')

'''
find the channels of interest time series data agnostic of file type and place into large df
'''

search_channel=[]

scrape_res_df = pd.DataFrame(columns=['Filename', 'Measure_name', 'Measure_Value', 'data_type', 'timestamp'])


for idx, row in requirement_input_df.iterrows():

    #search_channel=[]
    
    for i in [col for col in requirement_input_df.columns if 'Lab_Channel_' in col]:

        if row[i] != '':
            search_channel.append(row[i])
        
    if row['hint'] == "Labview":
        lv_result_df = Scrape_EAR.scrape_labview_master(search_channel, files, scrape_res_df, lv_summary_df)
  
'''
evaluate EAR
evalate calculation
'''

'''
for lv master evaluation

isolate evaluation equation
isolate relevant channels and group by file name

evaluate per equation and then compile results
 
'''