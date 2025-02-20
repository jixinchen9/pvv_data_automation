# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:58:13 2025

@author: jc16287
"""

import csv

'''
#takes in a dict which is one entry in list of dicts, and a list which indicates what to output
#outputs list which will become a row of output csv
'''

def row_for_csv(metadata_dict, fields):
    ordered_row = []
    for attribute in fields:
        ordered_row.append(metadata_dict.get(attribute))
    return ordered_row

'''
more generic csv writer, takes in a already comsposed list, could be memory
intensive, but honestly probably doesnt matter for the small inputs
'''
    
def write_csv(input_list,file_name):
    with open (file_name + ".csv", mode = 'w', newline = '') as f:
        f_writer = csv.writer(f)

        for row in input_list:
            f_writer.writerow(row)
    f.close()

'''
naive function written which basically does a df.pivot, will replace with the actual pandas 
method, secondarily it has some stuff in there to clean up the tables, it inserts column titles for attributes 
and file name, and also removes columns with repeat chan names
'''

def wide_table(input_list_metadata, input_files, output_columns):
    all_output_row=[]
    
    for i in input_list_metadata:
        if i.get("File_name") != input_files[0].replace(".sie",""):
            break
        
        output_row = row_for_csv(i, output_columns)
        
        for j in input_list_metadata:
            if i.get("ChanTitle") == j.get("ChanTitle") and i.get("File_name") != j.get("File_name"):
                output_row.extend(row_for_csv(j, output_columns))
         
        all_output_row.append(output_row)
    
    column_name_row = []
    
    for i in range(len(input_files)):
        for name in output_columns:
            column_name_row.append(name)
    
    file_name_row = []
    
    for file in input_files:
        file_name_row.append(" ")
        file_name_row.append(file)
        for i in range(len(output_columns)-2):
            file_name_row.append(" ")
    
    all_output_row.insert(0,column_name_row)
    all_output_row.insert(0,file_name_row)
    
    for row in all_output_row:
        column = 0
        for i in range(len(input_files)-1):
            column += len(output_columns)
            row.pop(column)
            column = column - 1
    
    return all_output_row
'''
#writes a csv with a filename matching original metadata file
#based on filename matching original metadata file (not neccesarily), fields to output or attributes to write, and a list of dicts either filters or not
keep around for now...
'''

def write_csv_deprecated(file_name, attributes_to_write, channels_to_write):
    with open (file_name + ".csv",mode = 'w', newline = '') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(attributes_to_write)
        
        for index, row in enumerate(channels_to_write):
            f_writer.writerow(row_for_csv(row, attributes_to_write))
    f.close()