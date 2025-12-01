# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:21:11 2025

@author: jc16287
"""
import gather_input
import config_builder
import requirements_obj

'''
              
'''         
def create_req_objs():
    
    req_lists = gather_input.get_requirements()
    obj_list = []
    
    for req_wordlist in req_lists:
        
        name = req_wordlist[ config_builder.config_v2_inst.req_name_index ]
        limit = req_wordlist[ config_builder.config_v2_inst.req_limit_index ]
        compare = req_wordlist[ config_builder.config_v2_inst.req_compare_index ]
        metadata_type = req_wordlist[ config_builder.config_v2_inst.req_metadata_type_index ]
        formula = req_wordlist[ config_builder.config_v2_inst.req_formula_index ]

        req_inst = requirements_obj.Requirement(name, limit, compare, metadata_type, formula)
        req_inst.set_channels(req_wordlist[ config_builder.config_v2_inst.req_channels_index :])
    
        obj_list.append(req_inst)
        
    return obj_list
        
req_obj_list = create_req_objs()