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

def edit_script(folder, script, bat, sie_list, sie_folder):
    sie_entry_searcher = r'\"(.*?)\;'
    
    with open(folder + script, 'r') as f:
        script_contents = f.readlines()
        f.close()
    
    i=0    
    while i != len(script_contents):
        
        if "AddFiles" in script_contents[i]:
            
            template_line = script_contents[i]
            script_contents.pop(i)
            
        else:
            i+=1
    
    addfiles_index = template_line.index("AddFiles")
    replaced = re.search(sie_entry_searcher, template_line[addfiles_index:] ).group()[1:-1]
        
    for j in sie_list:
        
        script_contents.pop(1)
        script_contents.insert(1, template_line.replace(replaced, sie_folder + j)+"\n")
        #script_contents.insert(2,"\n")

        with open(folder + script, 'w') as f:
            for k in script_contents:
                f.writelines(k)
            f.close()
            
        os.system(bat)