# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:14:16 2025

@author: jc16287
"""
import csv
import regex as re
import pandas as pd
'''
takes in name and path string of metadata file, and attributes named in fields to collect 
outputs a list of dicts containing the attributes in fields to collect
dicts correspond to individual channels
'''
def read_metadata_df(files ,desired_columns):
    
    start_search = False
    metadata_df = pd.DataFrame(columns=['Filename','ChanTitle','Attribute','value'])
    
    quote_searcher = r'\"(.*?)\"'
    
    for file in files:
        print(f"Scraping all metadata channels from: {file}")
        
        
        with open(file) as f:
            for line in f:
                #the code tries to guard against picking up stat field that actually
                #belong to another channel
                #the latching variable indicates when it's valid to search vs when it is not
                
                if "Attributes" in line:
                    start_search = True
                    channel_title = "unknown"
                    
                if start_search == True:
    
                    if "ChanTitle" in line:
                        value_index = line.index("value")
                        channel_title = re.search(quote_searcher, line[value_index:] ).group()[1:-1]
                        # this is not quite right, if you try to catch attributes alphabetically before chantitle
                        # the row may not write the channel correctly
                    
                    for column_name in desired_columns:
                        if column_name in line and column_name != "ChanTitle":
    
                            value_index = line.index("value")
                            channel_attribute_value = re.search(quote_searcher, line[value_index:] ).group()[1:-1]
    
                            new_row = {'value' : channel_attribute_value,
                                                 'Attribute' : column_name,
                                                 'ChanTitle' : channel_title,
                                                 'Filename' : file.replace("_meta_raw","")}
                            metadata_df.loc[len(metadata_df)] = new_row
        
                if "</Set>" in line:
                    start_search = False
                    
            f.close()
    return metadata_df


'''
reads filter spreadsheet and filters the tall df
'''
def filter_metadata_df(metadata_list, folder, filename):
    filtered_channels=[]
    with open(folder + "/" + filename, newline = '') as f:
        f_reader = csv.reader(f)
        
        for row in f_reader:
            filtered_channels.append(row[0])
        
        pattern = '|'.join(filtered_channels)
        filtered_df = metadata_list[metadata_list['ChanTitle'].str.contains(pattern)]
    
        f.close()
    
    return filtered_df

'''
obsoleted by df adoption
'''

def filter_metadata(metadata_list, folder, filename):
    filtered_list=[]
    with open(folder + filename, newline = '') as f:
        f_reader = csv.reader(f)
        
        for row in f_reader:
        
            for i in metadata_list:
                if row[0] in i.get("ChanTitle"):
                    filtered_list.append(i)
        
        f.close()
        
        sorted_filtered_list = sorted(filtered_list, key=lambda x: x['File_name'])

    return sorted_filtered_list

'''
takes in name and path string of metadata file, and attributes named in fields to collect 
outputs a list of dicts containing the attributes in fields to collect
dicts correspond to individual channels
'''


def read_metadata(folder, files ,desired_columns):
    
    start_search = False
    channel_dict = {}
    channel_dict_list = [] 
    
    quote_searcher = r'\"(.*?)\"'
    
    for file in files:
        print(file)
        
        
        with open(folder + file) as f:
            for line in f:
                #the code tries to guard against picking up stat field that actually
                #belong to another channel
                #the latching variable indicates when it's valid to search vs when it is not
                
                if "Attributes" in line:
                    start_search = True
                    
                if start_search == True:
                    for column_name in desired_columns:
                        if column_name in line:
                            value_index = line.index("value")
                            
                            try:
                                channel_dict.update({column_name : re.search(quote_searcher, line[value_index:] ).group()[1:-1]})
                            except: 
                                pass
        
                if "</Set>" in line:
                    start_search = False
                    
                    if len(channel_dict) != 0:
                        channel_dict.update({'File_name':file.replace("_meta_raw","")})
                        channel_dict_list.append(channel_dict)
                        channel_dict = {}
            f.close()
        
        
    return channel_dict_list

