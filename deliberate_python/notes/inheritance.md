---
noteId: "39bea7e098ff11ea8b572b6747d84cb1"
tags: []

---

## Multiple Inheritance

when a class inherits two classes, if its inherited method from parents have different signatures, how Python decide which method to use?

**Method Resolution Order**

- `class Manager(Employee, Payroll)` tells python to first search method in Employee class and then Payroll class.
- `Manager.__mro__` to inspect the order
