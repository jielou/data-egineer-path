import threading

sem = threading.Semaphore(value=50)
print(sem._value) # value is atomic counter
#print(dir(sem))

sem.acquire()
sem.acquire()
sem.acquire()
sem.release()
print(sem._value)
# make sure only a limited number of cps get used to the resources