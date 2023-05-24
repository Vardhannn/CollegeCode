#MULTI THREADING

import threading
import time
def my_function():
    print("Thread starting...")
    time.sleep(5)
    print("Thread exiting...")
thread = threading.Thread(target=my_function)
thread.start()
thread.join()
del thread
print("Thread has been deleted.")