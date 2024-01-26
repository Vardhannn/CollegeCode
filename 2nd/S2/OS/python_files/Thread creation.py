#THREAD CREATION

import threading
import time


def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} exiting")


def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()