# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 10:45:25 2025

evaluate a formula which is a string with arbitrarily many inputs

@author: jc16287
"""
import pandas

test_formula = "var_0 * var_1"

enginespeed = 5
torque = 2

data = {
        "enginespeed":[3000,3300,2700,2200,3050],
        "torque":[100,104,99,87,101]
        }

df_data = pandas.DataFrame(data)

def calc_formulas ( formula, *args):
    
    for index, value in enumerate(args):
        var_name = f"var_{index}"
        locals()[var_name] = value
        
    print(locals())
    try:
        return eval(formula)
    
    except(NameError):
        print("not enough arguments")
        
print(calc_formulas(test_formula, enginespeed, torque))

df_data['power'] = df_data.apply(lambda x: calc_formulas(test_formula, x.enginespeed, x.torque), axis = 1)
print(df_data['power'])