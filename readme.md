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
- v2 metadata writer: script creates tall table summarzing channels of user selection in a list of input files, the files will be trimmed according to steady state time start and ends in another specified input file
    - Script reads input of file names and folder lists, file names can be partially matched, case insensitive
    - Script runs libsie api demo .exe from hbm to convert sie files to csv 
    - script collects time series data for specified channels from the csv export
    - Script scrapes labview summaries for time slice start time and end time from a specified labview summary
    - script matches the runs in the labview summary with the input files based on set overlap of words in the name
    - script checks each time series for each channel to see if the specified steady state time can be applied
    - the time limits or slices are applied to time series for each file or test run and metadata (min max mean) is calculated
    - metadata output as tall table
    - outputs a log of each run reporting on execution status of above functions
- v1 metatdata writer: Script can create wide table summarizing multiple wind tunnel .sie files
    - Script reads input of file names and folder lists, file names can be partially matched, case insensitive
    - Script can run ncode to generate metadata files for each test file
    - Script can search metadata file for desired channel data or all channel data
    - Script can output compiled metadata as csv
- Feature 2
- Feature 3

## Setup

- edit the path of python install in the main_metadata_writer.bat, should be the same one you updated modules in.
    alternatively, add the path of both the python bundled with windows and a full featured python install to the PATH variable in 'edit environment variables', making sure the full featured python precedes the windows one in the path variable list. 
- adding the install of python to PATH variable will allow you to install any packages that are missing from you python install: "python -m pip install \<module name\>". 'xlrd' may a module you install in this manner.
- relevant only to v1: it is easiest to just regenerate the ncode batch file and script by opening the flo file and adding a file to the input, this will update the install location of ncode so the ncode batch script can run
    simply open flo file in ncode and 'save for batch file'
- The process is developed inside a python virtual environment, but relies on only a few libraries, regex, pandas, and xlrd at time of this writing; a requirements document is provided to generate venv should dependency issues arise in the future; for most purposes it will be ok to run script with generic python 3.12 interpreter, which you will have mapped to.
- now you can simply run the batch file for the python script from command prompt or by double clicking.
    

## Running the script
- Currently 2 processes are provided, one runs metadata generation with requirement evaluation, the other just runs metadata generation; note that the input form must be completed to run the script with requirement evaluation.
- Use the input form, here named "Data_Automation_Benchmark_Data_w_timeslice.csv", to specify what files will be input into the process. there are four main inputs on this page:
    - the file names 
    - the folder path where the files are, 
    - and the full path of the timeslice data source, usually a labview summary. 
    - note that all inputs must be written between the guard strings: they look like 'group_1_path_start', 'group_1_path_end' and so on, the text scraping for inputs depends on these guard strings and will only pick up inputs written between the guards.
    - Define what channels should be included
- Add/verify hintwords in time slice information file i.e. labview summary. the process uses hint words to find the row with run name and the row with time slice start and end. usually the time slice hint word will not be in a labview summary by default. if you don't write the hint word the process will still run but it will not slice the data, metadata will be calculated that may not be steady state. the hint words the process uses can be edited in the config file. 
- Use the requirement input form to add requirements you wish to evaluate:
    - all requirements to be evaluated are entered between guard strings "Requirement_start" and "Requirement_end" much as in the data file input 
    - the requirement name will be used as a column to indicate pass/fail in the summary output
    - the requirement value and requirement operator are used to evaluate the requirement, for example if the value is '200' and the operator is '<=', the the requirement will be evaluated to 'pass' if the measure value is less than or equal to '200'
    - the data measure entry tells script which aggregate value to look at, min, max, or avg
    - channels are input starting in column K, the script will look for any many channels as are input past channel K
    - the "OR" in requirement formula means that all channels are evaluated using the same criteria
- Make selections in config, usually not needed, but see next section 

## The config file explained
- both processes use config_v2.
- input
    * path: folder where input forms are
    * data: the name of input form for config writer v2, you can copy the form, rename it, and update it here and the script will use it to run the process
    * requirement: carry over from earlier development, this input form would hold specific EAR requirements
- Filter
    * path: folder where channel name list input form is 
    * filename: name of channel name list input form 
- timeslice
    * option: you can opt out of applying steady state time slices to time series data altogether by entering '0' here, any non-zero entry enables time slice processing
    * helper_test: this helps the script scrape the labview summary for time slices, this is the entry in the excel sheet in the first column of the row holding all the test run names, happens to be "CAC" in most labview summaries. This can be thought of as a 'magic' parameter.
    * helper_slice: same idea as above, except this time it's to help find the row with time slice start and end, as mentioned previously, this one should be added to the labview summary.
    * minimum_match: test names in the labview summary and test names in the input files are not always identical, they are matched to each other based on how many words appear in both strings, script selects the maximum match for each input file from the time slice scrape, minimum match is to prevent the script from assigning matches from a completely unrelated summary sheet if the user has made an input error: if match number is less than the number here, time slice will not be updated with data from lv summary.
- ncode
    * path: v1 config field to point to where the ncode batch and script files for metadata export were stored
    * batfile: name of batch file for ncode based automation
    * batch_script: batch script for  ncode based automation
- libsie
    * path: path to where batchfile that calls libsie demo exe is, this is how sie is converted to csv for python to process
    * batfile: name of batch file 
    * path_hint: this helps the script distinguish devx files from sie files or sie exports, because file paths for sie files always have the work 'Edaq' in them, it's for this same reason 'edaq_export' is suffixed to the temp file outputs.
-temp
    * path: folder where the csv exports made by libsie are stored
- ncode_app
    * path: streamline setup for v1, not implemented
- output
    * path: folder where output files like the summary tables of the entire process are stored
    * filename: you can specify a name for your output here
- log
    * path: folder where logs will be output
    * filename: you can specify a name for the log files
- helper
    * path: folder where helper files are stored, like a planned channel lister, not yet inplemented
- Devx
    * trim_hint: this helps the script find the first line of dex data, devx writes a wide table of data organized into columns by channel after varying lines of machine information, the hint string is the first channel name ("Time") in the channel row. like the earlier time slice hints, this can be thought of as another 'magic' parameter.
    * path_hint: this helps the script distinguish devx files from sie files or sie exports, devx file network file paths always have the word 'devx' in the file path
- Attributes
    * name: metadatawriter v1 used this to scrape the ncode generated metadata exports, you basically used this to choose what stats to export, not used any more
- requirement
    * path: folder where requirement input files are
    * filename: input file name
    * the rest: to build the requirement objects, the script relies on the indexing of the input spreadsheet, this means users are strongly discouraged from changing the order of the columns in the input, unless corresponding changes are made in the config