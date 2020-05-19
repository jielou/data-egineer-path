---
noteId: "39bea7e098ff11ea8b572b6747d84cb1"
tags: []

---
# inheritance

5.18

## Intro

reference: 
- [Intro to oop in python]()
- [super()](https://realpython.com/python-super/)

## Super()

- super() returns a bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes.

## Multiple Inheritance

when a class inherits two classes, if its inherited method from parents have different signatures, how Python decide which method to use?

**Method Resolution Order**

## mixin

- `class Manager(Employee, Payroll)` tells python to first search method in Employee class and then Payroll class.
- `Manager.__mro__` to inspect the order
