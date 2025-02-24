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
    - Script can discover all input files in a folder
    - Script can run ncode to generate metadata files for each test file
    - Script can search metadata file for desired channel data or all channel data
    - Script can output compiled metadata as csv
- Feature 2
- Feature 3

## Setup

- make sure you have the correct python modules, as of this writing you may need to install regex and pandas. i recommend: opening a command prompt in folder with python.exe of the python intallation you intend to use; type 'python.exe pip -m install regex', repeat as needed.
- edit the path of python install in the main_metadata_writer.bat, should be the same one you updated modules in.
- edit the paths in the config.json file, these paths are inputs to the script itself; you need to edit the input, filter file, ncode batch file, and output folder.
- edit the path of the ncode install location, flo file, ncode script file, and log file in the ncode batch file
- alternatively, it may be faster just to re-make the batch file, simply open flo file in ncode and 'save for batch file'
- now you can simply run the batch file for the ptyhon script from command prompt.