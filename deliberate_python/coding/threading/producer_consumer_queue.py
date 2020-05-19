"""
definition of producer_consumer pipeline

producer produces data and put it into pipeline ====>
consumer reads data from the pipeline and processes it

This script changes:
1. uses queue module to support multi-producer&consumer
2. use event to flag when to stop and start
"""
import random
import time
import concurrent.futures
import threading
import queue

FINISH = 'The End'

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=20)
        #self.capacity = capacity
        self.message = None
        # self.producer_lock = threading.Lock()
        # self.consumer_lock = threading.Lock()
        # self.consumer_lock.acquire() # important


    def set_message(self, message):
        print(f"producing message of {message}")
        producer_pipeline.append(message)
        #self.producer_lock.acquire()
        self.put(message)
        #self.consumer_lock.release()

    def get_message(self):
        #self.consumer_lock.acquire()
        message = self.get()
        print(f"consuming message of {message}")
        consumer_pipeline.append(message)
        #self.producer_lock.release()
        return message

def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1,100)
        pipeline.set_message(message)

def consumer(pipeline, event):
    # message = None
    # while message is not FINISH:
    while not pipeline.empty() or not event.is_set():
        print(f"queue size is {pipeline.qsize()}")
        message = pipeline.get_message()
        # if message is not FINISH:
        time.sleep(random.random())

producer_pipeline = []
consumer_pipeline = []

if __name__ == "__main__":
    pipeline = Pipeline()
    event = threading.Event() #.set(), .clear()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event)
        ex.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()

    print(f"producer: {producer_pipeline}")
    print(f"consumer: {consumer_pipeline}")