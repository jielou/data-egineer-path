
## reference
[python object](https://medium.com/@bdov_/https-medium-com-bdov-python-this-is-an-object-that-is-an-object-everything-is-an-object-fff50429cd4b)

[is operator](https://lerner.co.il/2015/06/16/why-you-should-almost-never-use-is-in-python/)

## key takeaways

1. id is memory address. Is is to compare the memory address. All the objects in Python are assigned a memory address. 

2. when initializing an immutable object, Python may first look for the address of any existing obejct. If found, then it would be assigned to the same address.
```python
a=12 # between -5 to 256
b=12
a is b # True
```

3. when initializing a muttable object, each would be assigned an address.
```python
a=[1,2,3]
b=[1,2,3]
a is b # False
```

4. string interning helps set two strings with the same content the same memory address.

5. is operator is often used when compared to None

6. == operator just compares the content. `__equal__`is under the hood.