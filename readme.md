# Project Title

A brief description of your project and what it does.

## Table of Contents

- [Features](#features)
- [Setup](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- List of features in your project
- Script can create wide table summarizing multiple wind tunnel .sie files
    - Script reads input of file names and folder lists, file names can be partially matched, case insensitive
    - Script can run ncode to generate metadata files for each test file
    - Script can search metadata file for desired channel data or all channel data
    - Script can output compiled metadata as csv
- Feature 2
- Feature 3

## Setup

- edit the path of python install in the main_metadata_writer.bat, should be the same one you updated modules in.
    alternatively, add the path of both the python bundled with windows and a full featured python install to the path variable in 'edit environment variables', making sure the full featured python precedes the windows one in the path variable list. 
- this shouldn't be a problem if you have a full feaured install: make sure you have the correct python modules, as of this writing you may need to install regex and pandas. 
    i recommend: opening a command prompt in folder with python.exe of the python intallation you intend to use; type 'python -m pip install regex', repeat as needed.
    will look into deployment using a venv.
- relevant to v1: it is easiest to just regenerate the ncode batch file and script by opening the flo file and adding a file to the input, this will update the install location of ncode so the ncode batch script can run
    simply open flo file in ncode and 'save for batch file'
- now you can simply run the batch file for the python script from command prompt or by double clicking.
    

## Running the v2 script

- Use the input form, here named "Data_Automation_Benchmark_Data_w_timeslice.csv", to specify what files will be input into the process. there are three main inputs on this page, the file names, the folder path where the files are, and the full path of the timeslice data source, usually a labview summary. note that all inputs must be written between the guard strings: they look like 'group_1_path_start', 'group_1_path_end' and so on, the text scraping for inputs depends on these guard strings and will only pick up inputs written between the guards.
- Add/verify hintwords in time slice information file or labview summary. the process uses hint words to find the row with run name and the row with time slice start and end. usually the time slice hint word will not be in a labview summary by default. if you don't write the hint word the process will still run but it will not slice the data, metadata will be calculated that may not be steady state. the hint words the process uses can be edited in the config file. 
- Define what channels should be included in another file in the input folder "Channel_list_v02.csv", same guard string logic applies here. there will be a tool which will generate channels common to a batch of files as well as list of all possible channels in a batch.
- Make selections in config, usually not needed, but see next section 

## The config fie explained