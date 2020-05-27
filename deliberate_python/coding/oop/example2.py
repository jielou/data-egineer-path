class First(object):
    def __init__(self):
        print("init first")
        #super().__init__()

class Second(object):
    def __init__(self):
        print("init second")
        # super().__init__()

class Third(First, Second):
    def __init__(self):
        print("init third")
        # super().__init__()
        # Second.__init__(self)

# https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way

class A(object):
    def __init__(self):
        print("Entering A")
        super().__init__()
        print("Leaving A")

class B(object):
    def __init__(self):
        print("Entering B")
        super().__init__()
        print("Leaving B")

class C(A, B):
    def __init__(self):
        print("Entering C")
        A.__init__(self)
        B.__init__(self)
        # super().__init__()
        print("Leaving C")

if __name__ == "__main__":
    # print(Third.__mro__)
    # third = Third()
    # print(A.__mro__)
    c = C()
    # super(A).__init__()
    # a = A()
