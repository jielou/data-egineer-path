import time
import threading
import concurrent.futures

def my_func(name):
    print(f"myfunc started with {name}")
    time.sleep(10) # like a block
    print(f"myfunc ended")

def my_func1(name):
    print(f"myfunc1 started with {name}")
    time.sleep(10) # like a block
    print(f"myfunc1 ended")

def my_func2(name):
    print(f"myfunc2 started with {name}")
    time.sleep(10) # like a block
    print(f"myfunc2 ended")


def example0(name):
    """in this example, there is only one thread
    the results are expected:

    main started
    myfunc started with realpython
    myfunc ended
    main ended
    """
    print("main started")
    my_func("realpython")
    print("main ended")


def example1(name):
    """in this example, two threads are run: main thread and my_func thread.
    the results are expected:

    main started
    myfunc started with realpython
    main ended
    myfunc ended
    """
    print("main started") # main thread
    t = threading.Thread(target=my_func, args=['realpython']) # the second thread
    t.start()
    print("main ended")


def example2(name):
    """in this example, two threads are run: main thread and my_func thread.
    Instead, daemon concept is introduced: we do want main thread to end even though my_func does not finish

    the results are expected:
    main started
    myfunc started with realpython
    main ended

    daemon lets program ends when the main thread ends
    """
    print("main started") # main thread
    t = threading.Thread(target=my_func, args=['realpython'], daemon=True) # the second thread
    t.start()
    print("main ended")


def example3(name):
    """in this example, two threads are run: main thread and my_func thread.
    Instead, join concept is introduced: we do want main thread to wait for the other thread

    the results are expected:
    main started
    myfunc started with realpython
    myfunc ended
    main ended

    join lets main thread to wait

    same result to the example0 with complexity
    """
    print("main started") # main thread
    t = threading.Thread(target=my_func, args=['realpython']) # the second thread
    t.start()
    t.join() # tell the main thread to wait before continuing
    print("main ended") 

def example4(name):
    """in this example, multiple threads are run

    main started
    myfunc started with realpython
    myfunc1 started with foo
    myfunc2 started with haha
    myfunc ended
    myfunc2 ended
    myfunc1 ended
    main ended

    notice: the order of threads end could be different every time

    same result to the example0 with complexity
    """
    print("main started") # main thread
    t1 = threading.Thread(target=my_func, args=['realpython']) # the second thread
    t1.start()
    t2 = threading.Thread(target=my_func1, args=['foo']) # the third thread
    t2.start()
    t3 = threading.Thread(target=my_func2, args=['haha']) # the fourth thread
    t3.start()
    t1.join() # tell the main thread to wait before continuing
    t2.join() # tell the main thread to wait before continuing
    t3.join() # tell the main thread to wait before continuing
    print("main ended")

def example5(name):
    """ This example recreates example4 but in a more efficient way using thread pool

    main started
    myfunc started with realpython
    myfunc started with bar
    myfunc started with haha
    myfunc ended
    myfunc ended
    myfunc ended
    main ended

    notice: no repetitive code

    same result to the example0 with complexity
    """
    print("main started") # main thread
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(my_func, ['realpython', 'bar', 'haha'])
    print("main ended")


if __name__ == "__main__":
    example5("real_python")