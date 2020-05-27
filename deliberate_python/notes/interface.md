# interface

## intro

reference:

- [abstract class](https://dbader.org/blog/abstract-base-classes-in-python)
- [interface in python](https://realpython.com/python-interface/)

## quick facts

- blueprint for designing classes
- Python does not have interface keyword

## implementation in python

### informal interfaces
create base class with methods not defined and to be overridden by subclasses.
### metaclass


### abstract method

1. instantiating the abstract class is impossible
2. forgetting to implement interface methods in one of the subclasses raises an error

```Python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
```