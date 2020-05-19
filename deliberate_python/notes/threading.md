---
noteId: "bef8d7d097b711ea8b572b6747d84cb1"
tags: []

---

5.19

# Intro

Multi-threading seems fun. Time to jump into thread pool!

[intro to threading](https://realpython.com/intro-to-python-threading/)

## terminology

1. CPU: piece of hardware that executes code
2. OS: handles the scheduling of when the CPU can be used
3. Process: a program as it is being executed
4. Thread: part of a process 

## key takeaways

1. race conditions: more than one thread is trying to access a shared piece of data at the same time
2. Python GIL limits one Python thread to run at a time
3. Tasks that spend much of their time waiting for external events are generally good candidates for threading. Problems that require heavy CPU computation and spend little time waiting for external events might not run faster at all. Check out the multiprocessing module instead.
4. a daemon is a process that runs in the background. Python threading has a more specific meaning for daemon. A daemon thread will shut down immediately when the program exits.