# Intro to bash scripts
from lecture on datacamp

04/26

## IF statements

**syntax**

```bash
if [ condition ]; then
    # some code
else
    # some other code
fi
```

**tips**
- spaces between square brackets and conditional elements inside
- don't forget semi-colon


**example**
```bash
x="ex"
if [ $x == "pre" ]; then
    echo "$x is a pre!"
else
    echo "$x is not a pre!"
fi
```
### Arithmetic IF statements

#### option 1

arithmetic statement can use the double-parenthesis structure

```bash
x=10
if (($x>5)); then
    echo "$x is more than 5!"
fi
```

#### option 2
square brackets + arithmetic flag:

- -eq
- ne
- lt
- le
- gt
- ge

```bash

x=10
if [ $x -gt 5 ]; then
    echo "$x is more than 5!"
fi
```

### other bash conditional flags

[link to the source](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)

- -e: if the file exists
- -s if the file exists and has size greater than zero

### and or or in bash

- &&: and
- ||: or

### multiple conditions
#### option 1
```bash
x=10
if [ $x -gt 5 ] && [ $x -lt 10 ]; then
    echo "$x is more than 5 and less thatn 11!"
fi
```
#### option 2
```bash
x=10
if [[ $x -gt 5 && $x -lt 10 ]]; then
    echo "$x is more than 5 and less thatn 11!"
fi
```
### IF and command-line programs
#### example
if the file words.txt has "Hello World!" inside

```bash
if grep -q 'Hello' words.txt; then
    echo "Hello is inside!"
fi
```
or 
```bash
if $(grep -q 'Hello' words.txt); then
    echo "Hello is inside!"
fi
```

## For loops & While statements

### basic structure

```bash
for x in 1 2 3
do
    echo $x
done
```
### number ranges

```bash
for x in {START..STOP..INCREMENT}
do
    echo $x
done
```
### three expression syntax

```bash
for ((x=START;CONDITION;X+=INCREMENTs))
do
    echo $x
done
```
### Glob expansions
```bash
for x in folder/*
do
    echo $x
done
```
### Glob expansions (advnaced)

add shell-within-a-call
```bash
for x in $(ls folder/ | grep -i 'air')
do
    echo $x
done
```
### While statement

example

```bash
x=1
while [ $x -le 3 ]:
do
    echo $x
    ((X+=1))
done
```

**beware the infinite loop!**

## Case Statement

optimal to complex conditions compared to if statement

### base structure

```bash
case ''
 in 
 PATTERN1)
 COMMAND1;;
 PATTERN2)
 COMMAND2;;
 *)
 DEFAULT COMMAND;; # if no patterns match
 esac #exit
 ```

## Basic functions
```bash
function func_name(){
    # func_code
    return # something
}
func_name # call the function
```
### arguments

- $1, $2 positional arguments
- $@, $* all the arguments in ARGV
- $#: number of arguments

### scope

- "Global": accessible anywhere in the program
- "local": only accessilbe in a certain part of the program. keyword `local`

**note**

All variables in Bash are global by defaul

### return

- reutn is only menat to determine if the function succeede or failed.

- echo the results back and capture using shell-within-a-shell

```bash
function error{
    eshf # error
}
error
echo $? # print the return value
```
## schduling your program

cron

- crontab -l: list schedules

- *****(minute, hour, day of the month, month, day of the week)

```bash
# run at 1:05 am every Saturday and Sunday
5 1 * * 6,7 bash myscript.sh
```
- crontab -d: edit your list of cronjobs