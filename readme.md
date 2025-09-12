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
- this wont be a problem if you have a full feaured install: make sure you have the correct python modules, as of this writing you may need to install regex and pandas. 
    i recommend: opening a command prompt in folder with python.exe of the python intallation you intend to use; type 'python.exe pip -m install regex', repeat as needed.
- look through the config json file, no edits are needed here anymore because it is mostly set up with relative paths, things you may want to change?:
    the parameters that get pulled from metadata, max, mean etc
    the name of the output
- it is easiest to just regenerate the ncode batch file and script by opening the flo file and adding a file to the input, this will update the install location of ncode so the ncode batch script can run
    simply open flo file in ncode and 'save for batch file'
- now you can simply run the batch file for the ptyhon script from command prompt.
    batch file is currently in the source file folder, i wish it werent, it runs into errors though if it is not in the same folder, need to fix this.