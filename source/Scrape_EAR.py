# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:30:28 2025

@author: jc16287
"""
import pandas as pd
import numpy as np

'''
scrape the labview master or other doc for channel results in search_channel

    searches entire df of labview master for cell corresponding to correct file name and channel name
    adds it to the scrape_res_df which rn is agnostic and will contain all results
'''

def scrape_labview_master(channel_list, file_list, result_df, lv_master_df):
        
    for channel in channel_list:
            
            for file in file_list:
                try:
                    lv_result = lv_master_df.loc[lv_master_df['CAC'].str.contains(channel), file].values[0]
                    print(channel, "::" , lv_result)
                    
                    scrape_row = [file, channel, lv_result, "lv_agg", np.nan]
                    result_df = pd.concat([pd.DataFrame([scrape_row], columns= result_df.columns), result_df], ignore_index=True)
                
                except IndexError:
                    print(channel, " not found.")
                except KeyError:
                    print(file, " not found")
    
    return result_df
