# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:45:13 2025

@author: jc16287
"""

'''
gives list of .sie files given a folder path string
'''
import os
import log_writer

def find_sie(folder):
    
    files = os.listdir(folder)
    
    i=0
    while i != len(files):
        
        if ".sie" in files[i]:
            i+=1
        else:
            files.pop(i)
    return files

'''
gives list of metadata files given a folder path string
'''

def find_metadata_files(folder):
    metadata_filelist = os.listdir(folder)
    
    i=0
    while i != len(metadata_filelist):
        
        if "meta_raw" not in metadata_filelist[i] or ".csv" in metadata_filelist[i]:
            metadata_filelist.pop(i)
        
        else:
            i+=1
    
    return metadata_filelist

'''
find metadata files in multiple folders, writes abs paths, also returns all filenames alone
'''
def find_meta_files_multifolder(folder_list):
    
    all_metadata_paths = []
    all_metadata_files = []
    
    for folder in folder_list:
        
        metadata_files = find_metadata_files(folder)
        prefix = folder + "\\"
        metadata_paths = [prefix + item for item in metadata_files]
        
        all_metadata_paths += metadata_paths
        all_metadata_files += metadata_files
    
    log_writer.create_log_entry("the following metadata files were generated:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(all_metadata_files, log_writer.metadata_v01_log.content)
    
    return all_metadata_paths, all_metadata_files

'''
given a list of file name queries and list of files, searches all folder for all queries

'''
def get_full_paths(file_list, folder_list):
    # list comprehension ya dig
    full_path_list = []

    for row in folder_list:
        
        files_found = os.listdir(row)
        #matched_files = [item for item in files_found if any(substring in item for substring in file_list)]
        matched_files_os, matched_files_query = case_insensitive_search(file_list, files_found)
        
        for i in matched_files_os:
            full_path_list.append(row + "\\" + i )
        
        
    not_found_files = list(set(file_list) - set(matched_files_query))
    
    log_writer.create_log_entry("found these files", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(full_path_list, log_writer.metadata_v01_log.content)
    
    log_writer.create_log_entry("the following file names were not found:", log_writer.metadata_v01_log.content)
    log_writer.create_log_entry(not_found_files, log_writer.metadata_v01_log.content)

    return full_path_list, not_found_files, 

def case_insensitive_search(needle_list, haystack_list):
    result_list = []
    found_counter = []
    
    for i in needle_list:
        for j in haystack_list:
            
            if i.lower() in j.lower():
                result_list.append(j)
                found_counter.append(i)
                break
                
    return result_list, found_counter