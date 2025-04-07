# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 10:25:44 2025

@author: jc16287

how does pivot work? i mean how does it REALLY work
"""

import pandas as pd
import numpy as np

data_1 = np.array([
    ['test_a','engine_speed', 1000],
    ['test_a','coolant_temp', 80],
    ['test_a','fuel_level', 80],
    ['test_b','engine_speed', 1100],
    ['test_b','coolant_temp', 90],
    ['test_b','percent_load', 95],
    ['test_b','scr_temp', 500]
    ])

df_1 = pd.DataFrame(data_1, columns = ['file', 'channel', 'value'])

df_1_wide = pd.pivot(df_1, index='channel', columns = ['file'], values = 'value')

lab_channel_1 = 1
lab_channel_2 = 2

expression = "abs(lab_channel_1-lab_channel_2)"

result = eval(expression)


