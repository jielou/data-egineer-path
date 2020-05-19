import threading

lock = threading.Lock()
print(lock)

lock.acquire() # no other thread can be run under this code
# protected: only owner of the lock is allowed to process
lock.release() # release lock
print(lock)

## deadlock: lock when lock is locked
# frozen
# solution: using context manager
lock.acquire()
lock.release() # or add release manually
lock.acquire()

#using Rlock
rlock = threading.RLock()
rlock.acquire()
rlock.acquire() #<locked _thread.RLock object owner=4348890560 count=2 at 0x103232cc0>
rlock.release()
print(rlock)
print(threading.current_thread())