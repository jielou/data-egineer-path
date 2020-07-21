def infinite_sequence():
    num=0
    while True:
        yield num
        num+=1
        yield "This is the second yield statement!"

def finite_sequence():
    num=0
    while num<4:
        yield num
        num+=1
        

if __name__ == "__main__":
    # infinite = infinite_sequence()
    # print(type(infinite))
    # print(next(infinite))
    # print(next(infinite))
    # for i in infinite:
    #     print(i)
    #     if i==3:
    #         break

    finite = finite_sequence()
    # for i in finite:
    #     print(i)
    print(next(finite))
    print(next(finite))
    print(next(finite))
    print(next(finite))
    print(next(finite)) #StopIteration

    #generator syntax
    nums_squared_gc = (num**2 for num in range(5))