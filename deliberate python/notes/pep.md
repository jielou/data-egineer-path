---
noteId: "d7d8c0b0914c11eab318d55bc3e6e734"
tags: []

---

# pep8

5/8

## Introduction

All my goal is about writing more pythonic code!

[reference](https://realpython.com/python-pep8/)

## what is pep8
PEP(Python Enhancement Proposal) 8 is a document that provides guidelines and best practices on how to write Python code.The primary focus of PEP 8 is to improve the readability and consistency of Python code.

## Naming

1. function, variable, method， module: lowercase word or words separated by underscores.
2. Class: camel case
3. constant: uppercase word or words separated by underscores

## Code Layout

- surround top-level functions and classes with two blank lines
- use blank lines sparingly inside functions to show clear steps
- lines should be limited to 79 characters
- If line breaking needs to occur around binary operators, like + and *, it should occur before the operator

## indention

- Use 4 consecutive spaces to indicate indentation
- Prefer spaces over tabs
- Python 3 does not allow mixing of tabs and spaces
- Add a comment after the final condition. Due to syntax highlighting in most editors, this will separate the conditions from the nested code

## comments

- Limit the line length of comments and docstrings to 72 characters
- Use complete sentences, starting with a capital letter
- Make sure to update comments if you change your code

## documentation strings
- Surround docstrings with three double quotes on either side, as in """This is a docstring"""
- Write them for all public modules, functions, classes, and methods
- Put the """ that ends a multiline docstring on a line by itself
- For one-line docstrings, keep the """ on the same line

## whitespaces
- Surround the following binary operators with a single space on either side: assignment operators, comparisons, and booleans; but not when assigning a default value to a function argument
- in multiple operator and multiple conditions, no whitespace around higher priority oeprtator
- avoid adding whitespace is at the end of a line

## Programming Recommendations

- Don’t compare boolean values to True or False using the equivalence operator
- Use the fact that empty sequences are falsy in if statements
- Use is not rather than not ... is in if statements
- Don’t use if x: when you mean if x is not None:
- Use .startswith() and .endswith() instead of slicing

## Some helpful tool

- linters
- pycodestyle
- flake8
- pip install black
