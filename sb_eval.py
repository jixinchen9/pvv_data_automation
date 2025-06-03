# -*- coding: utf-8 -*-
"""
Created on Fri May 16 12:10:49 2025

@author: jc16287
"""

import numpy as np
import pandas as pd

eval_test_df = pd.DataFrame(columns=['formula', 'arg1', 'arg2', 'arg3', 'arg4'])

new_row = {'formula': "arg1*arg2", 'arg1': 'pressure', 'arg2': 'temp', 'arg3': np.nan, 'arg4': np.nan  }

eval_test_df.loc[len(eval_test_df)] = new_row


temp =5

var1 = eval_test_df.at[0,'arg1']

exec(var1+ "= 10")

