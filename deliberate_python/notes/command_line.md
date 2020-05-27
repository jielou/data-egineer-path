# command line in pyton

## intro

reference: [command line arguements](https://realpython.com/python-command-line-arguments/)

[make python as comand line tool](https://dbader.org/blog/how-to-make-command-line-commands-with-python)

[argparse](https://realpython.com/command-line-interfaces-python-argparse/)
## what is command line interface

CLI provides a way for a user to interact with a program running in a text-based shell interpreter

## tricks

On Linux, whitespaces can be escaped by doing one of the following:
- Surrounding the arguments with single quotes (')
- Surrounding the arguments with double quotes (")
- Prefixing each space with a backslash (\)

## terminology
**Options** modify the behavior of a particular command or program.
- Short options can be stacked, meaning that -abc is equivalent to -a -b -c.
- Long options can have arguments specified after a space or the equals sign (=). The long option --input=ARG is equivalent to --input ARG.

## parse arguments

1. using list comprehensions
2. argparse
3. getopt
4. click

**Arguments** represent the source or destination to be processed.

**Subcommands** allow a program to define more than one command with the respective set of options and arguments.