# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 12:21:11 2025

@author: jc16287
"""
import gather_input
import config_builder
import requirements_obj
import pandas as pd
import log_writer
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
        
        try:
            limit = float(limit)
        except:
            talk1 = (f"unable to intake limit value input {limit} as a number!\n")
            print(talk1)
            log_writer.create_log_entry(talk1, log_writer.metadata_v01_log.content)
            
        req_inst = requirements_obj.Requirement(name, limit, compare, metadata_type, formula)
        req_inst.set_channels(req_wordlist[ config_builder.config_v2_inst.req_channels_index :])
    
        obj_list.append(req_inst)

    return obj_list
        


# if req formula is OR, then cycle through all collected channels
def set_req_result (row, requirement ):
    if requirement.formula == "OR":
        
        for data_channel in requirement.get_channels():
            pass_fail = set_channel_result(row , data_channel, requirement)
            
            if pass_fail:
                return "pass"
            elif pass_fail == False:
                return "fail"

    else:
        talk2 = ("requirement evaluation method not supported, check formula box")
        print(talk2)
        log_writer.create_log_entry(talk2, log_writer.metadata_v01_log.content)
        
def set_channel_result (row , channel_name , requirement ):
    if row['measure_name'] == channel_name and row['agg_type'] == requirement.metadata_type:
        
        comparison_string = f"{row['measure_value']}{requirement.compare}{requirement.limit}"
        
        result = eval(comparison_string)
        
        talk3 = (f"Result of {channel_name}'{comparison_string}': {result}")
        print(talk3)
        log_writer.create_log_entry(talk3, log_writer.metadata_v01_log.content)
        
        return result
"""
#local testing

req_obj_list = create_req_objs()

test_df = pd.read_csv(config_builder.config_v2_inst.output_path + "/" + config_builder.config_v2_inst.output_name + ".csv")

channels_test = req_obj_list[0].get_channels()

test_df[f"{req_obj_list[0].name}"] = test_df.apply(set_req_result , 
                                                   axis = 1,  
                                                   requirement=req_obj_list[0])

"""       

