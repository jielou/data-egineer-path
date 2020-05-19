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
- [OOP guide] (https://realpython.com/inheritance-composition-python/)


## Unifired Modeling Language (UML)

a standardized way to view the design of a system

## inheritance
what common attributes and behaviors exist between real-world objects?

- is-a relationship
- liskov substitution principle: in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program


## composition
how are objects in the real world composed of one another?

- has-a relationship

## interface

a description of the features and behaviors an object has

- python does not have actual mechanisms called interfaces. instead conceptual idea.



## Super()

- super() returns a bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes.

## Multiple Inheritance

when a class inherits two classes, if its inherited method from parents have different signatures, how Python decide which method to use?

**Method Resolution Order**

## mixin

- `class Manager(Employee, Payroll)` tells python to first search method in Employee class and then Payroll class.
- `Manager.__mro__` to inspect the order
