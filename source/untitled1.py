# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:21:42 2025

@author: jc16287
"""

import config_builder
import gather_input




channel_test = gather_input.get_requirements()

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
        
'''
name = channel_test[config_builder.config_v2_inst.req_name_index]
limit = channel_test[config_builder.config_v2_inst.req_limit_index]
compare = channel_test[config_builder.config_v2_inst.req_compare_index]
metadata_type = channel_test[config_builder.config_v2_inst.req_metadata_type_index]
formula = channel_test[config_builder.config_v2_inst.req_formula_index]

trial_req = Requirement(name, limit, compare, metadata_type, formula)
trial_req.set_channels(channel_test[config_builder.config_v2_inst.req_channels_index:])              
'''         
