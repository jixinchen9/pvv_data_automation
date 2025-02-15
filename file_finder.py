# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:45:13 2025

@author: jc16287
"""

'''
gives list of .sie files given a folder path string
'''
import os

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