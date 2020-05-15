---
noteId: "7fc2b860914511eab318d55bc3e6e734"
tags: []

---

# documentation guide

5.8

[reference](https://realpython.com/documenting-python-code/)

## Intro

As a Data Engineer, I wrote a lot of code to develop a tool. Documenting is very import 

## why code is important

> code is more often read than written

## code comments

> Code tells you how; Comments tell you why

- comment as planning and reviewing code segment; code description; algorithmic description; Tag for action like todo, fix it, etc.

- comment rule:
1. keep comments as close as possible to the code
2. design your code to comment itself
3. don't include redundant information
4. type hinting

## docstrings

- docstrings provide a brief overview of the object.

- multi-lined docstrings elaborate more on the object

```python
func/class.__doc__

# you can set the __doc__ attribute
func.__doc__="This is a func"

# or just use """

def func():
    """This is a func"""

```
### class docstrings
- place immediately following the class or class method indented by one level

### module/package docstrings
- placed at the top of the file, above even imports
- include description of the module and its purpose
### script docstrings
- scripts are considered single file executables
- explain how to use the script

## docstrings formatting

- Commonly have arguments, returns, attributes
- Options: Google docstrings, reStructured Text, NumPy/SciPy, Epytext