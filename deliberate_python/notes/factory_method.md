# factory method

## intro

factory method is a design pattern. It separates the process of creating an object from the code that depends on the interface of the object.

Instead of using a complex if/elif/else conditional structure to determine the concrete implementation, the application delegates that decision to a separate component that creates the concrete object.

[reference](https://realpython.com/factory-method-python/#introducing-factory-method)

## key takeaways

- The single responsibility principle states that a module, a class, or even a method should have a single, well-defined responsibility.
- opportunities to use factory method
    - Replacing complex logical code
    - Constructing related objects from external data
    - Supporting multiple implementations of the same feature
    - Combining similar features under a common interface
    - Integrating related external services


