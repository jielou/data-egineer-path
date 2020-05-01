# pip
5.1

this note is taken for the tutorial from Real Python

## Intro

I have used pip a lot...but not really understand what pip is and how it works. I planned to go deep into its core.

## basic concepts

1. what is pip

pip is a package manager for python, allowing installation and management of python packages. 

2. what is Conda, Pipenv and Poetry?

They are all great alternatives to pip.

- conda is a package, dependency, and environment manager for many languages, including Python.
- pipenv is a package management tool. It merges virtual environment and package management.
- Poetry simplifies package version management and separates development vs production dependencies.



## quick facts

1. packages are published to the Python Package Index, aka PyPI

2. requirements.txt allows to specify dependcy versions using logical operators

## Useful command

```sh
pip --version
pip help
pip install package_name # install
python -m pip install --upgrade pip # upgrade by running pip as an executable module
pip list # see the packages installed
pip show package_name # package metadata
pip freeze > requirements.txt # outputs the installed packages in requirements format
pip install -r requirements.txt # specifying the requirements file
pip install --upgrade -r requirements.txt # upgrade the packages in requirements file
pip help search # get help info for search command
pip search package_name # search the package to be installed
pip uninstall package_name -y # uninstall a package, -y flag to suppress the confirmation and file list
```
## tips

1. Before uninstalling a package, check the dependency by show command. 

## Useful resources

1. [pip doc](https://pip.pypa.io/en/stable/)
2. [install pip](https://pip.pypa.io/en/stable/installing/)
3. [PYPI](https://pypi.org/)
4. [requirements file format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)
5. [conda](https://conda.io/en/latest/)
6. [pipenv](https://pipenv.pypa.io/en/latest/)
7.[poetry](https://python-poetry.org/)