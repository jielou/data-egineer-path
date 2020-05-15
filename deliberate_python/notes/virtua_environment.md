---
noteId: "cf2b395096a811ea9e7f53bbf66be716"
tags: []

---

# virtual environment

https://realpython.com/python-virtual-environments-a-primer/

## Intro
When I installed Python on my personal laptop, I never tried virtual environment, though I heard this term a lot. After working on industrial projects, I started using virtual environment, and found it really useful in the reality.

## Basic concepts

1. what is virtual environment?

virtual environment allows to create an isolated environment for Python projects. It is a big helpful when two projects depend on different version of packages. Each environment is independent of each other. 

## how to create VE

1. use virtualenv

```bash
pip install virtualenv #install the package
mkdir ve-example&&cd ve_example
python3 -m venv enc # create the ve
source env/bin/activate #activate virtual environment
which python # get path for the python executable
deactivate #deactivate

```

## under the hood

1. When Python is starting up, it looks at the path of its binary. In a virtual environment, it is actually just a copy of, or symlink to, your system’s Python binary. 