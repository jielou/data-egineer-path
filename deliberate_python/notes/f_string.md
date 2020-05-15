---
noteId: "7ffccd70914011eab318d55bc3e6e734"
tags: []

---

# f string

5/8

## Intro

I used to use .format to format a string. Recently, I knew fstring expression in Python 3.6+, and found it really clear and helpful. I decided to change my formatted string to f-string. This tutorial walks through all the formatted string in Python and showcase how to use f-string to make your life easier! Let's get started. 

[Reference](https://realpython.com/python-f-strings/)

## Old-school format: %-formatting


```python
#example
name = "Jes"
age = 24
print("Hello. I am %s and %s years old" %(name, age))
```

    Hello. I am Jes and 24 years old


## str.format()

I used to use this option a lot and kinda liked it.


```python
# the same example
name = "Jes"
age = 24
print("Hello. I am {} and {} years old".format(name, age))

# a tricky one with dictionary
me = {"name":"Jes", "age":24}
print("Hello again. I am {name} and {age} years old".format(**me))
```

    Hello. I am Jes and 24 years old
    Hello again. I am Jes and 24 years old


### Why I don't like .format sometimes

It allows the item matched in the end of the sentence. I have to make sure I put the right variable in the right order. In a long string, I have to switch back and forth to make sure I do the right thing. It's a little annoying. And also .format just occupies some space.

Time for learning f-strings.

## f-strings

- AKA: formatted string literals
- definition: string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.


```python
# the same example
name = "Jes"
age = 24
print(f"Hello. I am {name} and {age} years old")
```

    Hello. I am Jes and 24 years old


See, you know exactly where to put name and age in the string.

### More examples


```python
# you can have more complex expression inside curly
print(f"Hello. I am {name.upper()} and {age+1} years old")

# multiline. It's useful when your string is long!
multiline = (f"Hello. "
             f"I am  {name.upper()}. "
             f"I am {age+1} years old. "
             f"How are you doing?")
print(multiline)
# multiline. If you want to have \n
multiline2 = (f"Hello. \n"
             f"I am  {name.upper()}. \n"
             f"I am {age+1} years old. \n"
             f"How are you doing?")

print(multiline2)

# multiline with tripple quotes
multiline3 = f"""Hello. 
I am  {name.upper()}.
I am {age+1} years old.
How are you doing?
"""
print(multiline3)
```

    Hello. I am JES and 25 years old
    Hello. I am  JES. I am 25 years old. How are you doing?
    Hello. 
    I am  JES. 
    I am 25 years old. 
    How are you doing?
    Hello. 
    I am  JES.
    I am 25 years old.
    How are you doing?
    


### Why f-strings

1. fast

expressions are evaluated at runtime rather than consttns values.

### Pitfalls


```python
# if you have to use quotations inside {}, make sure the one is different from the outside one

print(f"I am {me['name']}") # this works
# print(f"I am {me["name"]}") # this doesn't


# if you need to print out {}, then double it
print(f"this is a {{}}")

# if you need to print out two {}, then four times it
print(f"this is two {{{{}}}}")

# you cannot use backslaskes and comments# in the expression
# print(f"I am {\jes#}") . #won't work
```

    I am Jes
    this is a {}
    this is two {{}}


# Conclusion

I find f-string pretty useful. Don't forget to start typing f to format a string!
