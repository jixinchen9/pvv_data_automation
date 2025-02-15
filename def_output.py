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
#writes a csv with a filename matching original metadata file
#based on filename matching original metadata file (not neccesarily), fields to output or attributes to write, and a list of dicts either filters or not
'''

def write_csv(file_name, attributes_to_write, channels_to_write):
    with open (file_name + ".csv",mode = 'w', newline = '') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(attributes_to_write)
        
        for index, row in enumerate(channels_to_write):
            f_writer.writerow(row_for_csv(row, attributes_to_write))
    f.close()

