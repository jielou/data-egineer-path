# stack implementation is easier that that in Java.
# reference: https://www.geeksforgeeks.org/stack-in-python/
# https://realpython.com/how-to-implement-python-stack/
# option 1 using list. but slow, not efficient
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self, value):
        if self.stack:
            self.stack.pop()
        else:
            print("stack is empty")

# option 2 using deque. but slow, not efficient
def deque_example():
    from collections import deque
    stack = deque()
    stack.append("a") #O(1)
    stack.pop() #O(1)