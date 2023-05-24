#PRODUCER AND CONSUMER

import threading
import queue
import time

MAX_SIZE = 5  # Maximum size of the shared queue
NUM_ITEMS = 10  # Total number of items to produce

shared_queue = queue.Queue(MAX_SIZE)  # Shared queue to store items


def producer():
    for i in range(NUM_ITEMS):
        item = f"Item {i+1}"
        shared_queue.put(item)
        print(f"Produced {item}")
        time.sleep(1)  # Simulating time to produce an item


def consumer():
    while True:
        item = shared_queue.get()
        print(f"Consumed {item}")
        shared_queue.task_done()
        time.sleep(2)  # Simulating time to consume an item


def main():
    # Creating producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Starting the threads
    producer_thread.start()
    consumer_thread.start()

    # Waiting for threads to complete
    producer_thread.join()
    consumer_thread.join()

    # Waiting for all items to be consumed
    shared_queue.join()


if __name__ == "__main__":
    main()