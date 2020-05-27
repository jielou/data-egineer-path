# import 


## import search order
- sys.modules: everything that has already been imported
- Python Standard Library
- sys.path: list of directories, usually includes current directory 

## import pep8

### order of import
- standard library imports
- third party imports
- local application imports

Each group of imports should be separated by a blank space

### style
- Imports should always be written at the top of the file, after any module comments and docstrings


## absolute imports (PEP recommended)
a detailed path for each package or file, from the top-level package folder
- pros:
    - based on project root directory, doesn't change with directory structure
    - readable - clearly idenfities resource location
    - preferred per pep8
- cons:
    - can be verbose and repetitive

## relative improts
specifies the resource to be imported relative to the current location—that is, the location where the import statement is
- pros:
    - concise
    - advantage depends on directory structure
- cons:
    - not as readable
    - project changes can break imports
    - advantage depends on directory structure

