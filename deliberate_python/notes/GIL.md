# Global Interpreter Lock

## intro

reference:

[python gil](https://realpython.com/python-gil/)

## what is gil

a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. Therefore, only one thread can be in a state of execution at any point in time. 

## why gil?
Python uses reference counting for memory management. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object.

reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. 

The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead.

Some languages avoid the requirement of a GIL for thread-safe memory management by using approaches other than reference counting, such as garbage collection.

A lot of extensions were being written for the existing C libraries whose features were needed in Python. To prevent inconsistent changes, these C extensions required a thread-safe memory management which the GIL provided.

## CPU bound vs I/O bound

- cpu-bound: pushing the CPU to its limit. This includes programs that do mathematical computations like matrix multiplications, searching, image processing, etc.
- I/O bound: spend time waiting for Input/Output which can come from a user, file, database, network, etc. I/O-bound programs sometimes have to wait for a significant amount of time till they get what they need from the source due to the fact that the source may need to do its own processing before the input/output is ready
- In the multi-threaded version the GIL prevented the CPU-bound threads from executing in parellel.
- The GIL does not have much impact on the performance of I/O-bound multi-threaded programs as the lock is shared between threads while they are waiting for I/O.


## workaround with GIL

- use a multi-processing approach where you use multiple processes instead of threads. 
= user alternative python interpreters
