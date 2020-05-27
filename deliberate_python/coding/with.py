# good reference: https://dbader.org/blog/python-context-managers-and-with-statement
from contextlib import contextmanager


class MyContextManager:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print(f"{self.name} is open")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} is closed")
     
    def show(self):
        print(self.name*3)

@contextmanager
def show_file(name):
    print(f"{name} is open")
    try:
        for _ in range(3):
            yield name
    finally:
        print(f"{name} is closed")

def show_file_gen(name):
    print(f"{name} is open")
    try:
        for _ in range(3):
            yield name
    finally:
        print(f"{name} is closed")

if __name__ == "__main__":
    with MyContextManager("test.txt") as f:
        f.show()

    # with show_file("second.txt") as f:
    #     print(f,end=" ")
    # for i in range(3):
    #     print(show_file_gen("second.txt"))

