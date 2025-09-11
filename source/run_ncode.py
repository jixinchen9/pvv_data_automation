# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:52:30 2025

@author: jc16287
"""
import regex as re
import os

'''
this function takes in the folder location and name of the batch script from ncode
currently it will take any lines that looks like it refers to a sie file, copy it to a template, and delete the original line that adds the sie file
then it replaces the sie file name in the template line and writes new lines based on the sie file search done earlier
finally it will rewrite the original batch script file
'''



def edit_script(folder, script, bat, sie_list):
    
    batchfile_path = os.path.abspath(folder + "/" + bat)
    
    sie_entry_searcher = r'\"(.*?)\;'
    
    with open(folder + "/" + script, 'r') as f:
        script_contents = f.readlines()
        f.close()
    
    i=0    
    while i != len(script_contents):
        
        if "AddFiles" in script_contents[i]:
            
            #template_line = script_contents[i]
            #script_contents.pop(i)
            template_line = script_contents.pop(i)
            
        else:
            i+=1
    
    addfiles_index = template_line.index("AddFiles")
    replaced = re.search(sie_entry_searcher, template_line[addfiles_index:] ).group()[1:-1]
       
    for j in sie_list:
        
        try_slash = repr(j)
        script_contents.pop(1)
        script_contents.insert(1, template_line.replace(replaced, j)+"\n")
        #script_contents.insert(2,"\n")

        with open(folder + "/" + script, 'w') as f:
            for k in script_contents:
                f.writelines(k)
            f.close()
            
        os.system(batchfile_path)

'''

#test inputs
batfile_folder = "./ncode_file"
batscript_filename = "metadata_export_02.script"
batfile_filename = "metadata_export_02.bat"
sie_files = ["\\fhxnas02\pdcteams\combine\Power Module\PV&V\Lab\Windtunnel\Tier 4 Final\Mercury_13.6L-S750 & 9.0L\03 eDaq\Mercury 13.6L Application Approval\LPB FT4 Yinlun\1_Mercury_WT_13.6_LPB_FT4_YINLUN_InitialFill_Dearation_.sie",
             "\\fhxnas02\pdcteams\combine\Power Module\PV&V\Lab\Windtunnel\Tier 4 Final\Mercury_13.6L-S750 & 9.0L\03 eDaq\Mercury 13.6L Application Approval\LPB FT4 Yinlun\1.1_Mercury_WT_13.6_LPB_FT4_YINLUN_InitialFill_Dearation.sie"]

#edit_script(batfile_folder,batscript_filename,batfile_filename,sie_files)
#print(r"\n")

'''