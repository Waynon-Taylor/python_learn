import threading
import time

def func(y):
    print(":ran")
    time.sleep(1)
    print("done")


x  = threading.Thread(target=func,args=(5,))
x.start()
print(threading.active_count())
