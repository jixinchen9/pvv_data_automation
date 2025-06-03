#PVV Data Automation

##Introduction
This document presents very granular tasks that a human developer or an AI assisted developer can complete in order to complete the automation project

##nCode Metadata Collector

###Completed function; retroactively fill in 

##EAR Evaluation Feature
###Completed some operations; retroactively fill in

###Evaluate the expression in 'Requirement_Equation' column for each file/run in 'lv_result_df'

-pivot lv_result_df so rows are 'Filename' and columns become 'Measure_name'
-dynamically assign the value for each Measure_name i in each Filename to a variable actually named Measure_name
-evaluate a result using the entry in the 'Requirement_Equation' column of 'requirement_input_df'
-output a new df named 'lv_result_evaluated' which stores the evaluation result for each 'Filename'

###Find the relevant evaluation result for a given requirement in the 'lv_result_evaluated'