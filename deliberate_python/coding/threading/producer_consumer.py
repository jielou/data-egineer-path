"""
definition of producer_consumer pipeline

producer produces data and put it into pipeline ====>
consumer reads data from the pipeline and processes it
"""
import random
import time
import concurrent.futures
import threading

FINISH = 'The End'

class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() # important


    def set_message(self, message):
        print(f"producing message of {message}")
        producer_pipeline.append(message)
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()

    def get_message(self):
        self.consumer_lock.acquire()
        print(f"consuming message of {self.message}")
        consumer_pipeline.append(self.message)
        self.producer_lock.release()
        return self.message


def producer(pipeline):
    for _  in range(pipeline.capacity):
        message = random.randint(1,100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)

def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())

producer_pipeline = []
consumer_pipeline = []

if __name__ == "__main__":
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)

    print(f"producer: {producer_pipeline}")
    print(f"consumer: {consumer_pipeline}")