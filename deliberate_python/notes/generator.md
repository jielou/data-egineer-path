# generator

## intro

## key takeaways

- generators are iterable objects
- they keep state between calls, meaning they can remember a place in a sequence without holding the entire sequence in memory
- they save memory, but are slower than other iterables, so there is a tradeoff

## generator expression

`nums_squared_gc = (num**2 for num in range(5))`