# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:13:59 2025

@author: jc16287
"""
import regex as re
import csv
import os

metadata_folder = "D:\\086 local test ncode\\"
metadata_filename = "3_Mercury_WT_13.6_LPB_FT4_YINLUN_PP_405kw_29C_meta_raw"

fields_to_collect = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
                   "\"Min\"",
                   "SDev"
    ]

fields_to_output = ["ChanTitle",
                   "\"Max\"",
                   "Mean",
    ]

filter_folder = "D:\\086 local test ncode\\"
filter_filename = "Channel_list_example.csv"

def read_metadata(metadata_file,desired_columns):
    
    start_search = False
    channel_dict = {}
    channel_dict_list = [] 
    quote_searcher = r'\"(.*?)\"'
    
    with open(metadata_file) as f:
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
                    channel_dict_list.append(channel_dict)
                    channel_dict = {}
        f.close()
        return channel_dict_list

def row_for_csv(metadata_dict, fields):
    ordered_row = []
    for attribute in fields:
        ordered_row.append(metadata_dict.get(attribute))
    return ordered_row

def write_csv(file_name, attributes_to_write, channels_to_write):
    with open (file_name + ".csv",mode = 'w', newline = '') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(attributes_to_write)
        for row in channels_to_write:
            f_writer.writerow(row_for_csv(row, attributes_to_write))
    f.close()
    
full_list = read_metadata(metadata_folder + metadata_filename, fields_to_collect)

def filter_metadata(metadata_list, folder, filename):
    filtered_list=[]
    with open(folder + filename, newline = '') as f:
        f_reader = csv.reader(f)
        
        for row in f_reader:
        
            for i in full_list:
                if row[0] in i.get("ChanTitle"):
                    filtered_list.append(i)
    f.close()
    return filtered_list

short_list = filter_metadata(full_list, filter_folder, filter_filename)

def find_metadata_files(folder):
    metadata_filelist = os.listdir(folder)
    metadata_filelist.sort()
    
    i=0
    while i != len(metadata_filelist):
        
        if "meta_raw" not in metadata_filelist[i] or ".csv" in metadata_filelist[i]:
            metadata_filelist.pop(i)
        
        else:
            i+=1
    
    return metadata_filelist

files = find_metadata_files(metadata_folder)

#write_csv(metadata_filename, fields_to_output, short_list)