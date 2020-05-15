---
noteId: "b8fdc570937f11eab318d55bc3e6e734"
tags: []

---

# read file

5.11

## Intro

I deal with file reading a lot in the work. Therefore, I would like to understand it better.

## quick facts

1. file is a contiguous set of bytes used to store data.
2. in file path, double-dot (..) moves one directory up.
3. Line endings in Windows and Unix are different: Window uses CR+LF charatecters (\r+\n) while Unix uses LF character (\n)
4. ASCII and UNICODE are two common encodings formats. ASCII stores 128 characters while Unicode stores 1,114,112 characters. Choosing a right format is important.

## Implementation in Python

```python
file = open(file_path) # return a file object

# a btter way to close the file
with open(file_path) as file:
    # process
```

#### tips 

1. use reading mode: *r* for reading, *w* for writing, *rb/wb* for reading/writing using byte data.

## processing file in python

```python
file.read(size=-1) # reads from the file based on the number fo size

file.readline(size==-1) # read at most size number of characters from the line

file.readlines() # reads the remaining lines from the file object returning as a list

## more pythonic way
with open(file_path, 'r') as file:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')

# write files
file.write(string)
file.writelines(seq)
```