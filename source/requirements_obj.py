# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:21:42 2025

@author: jc16287
"""

class Requirement:
    def __init__(self, name, limit = -1, compare = "", metadata_type = "", formula = "", channels= []):
        self.name = name
        self.limit = limit
        self.compare = compare
        self.metadata_type = metadata_type
        self.formula = formula
        self._channels = channels
        
    def get_channels (self):
        return self._channels
    
    def set_channels (self, input_list):
        
        for entry in list(input_list):
            if not entry or entry.isspace():
                input_list.remove(entry)
            else:
                continue
            
        self._channels = input_list
        
