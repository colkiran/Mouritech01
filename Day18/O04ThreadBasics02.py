
# synchronous / sequential execution of code

import threading
import time

st = time.perf_counter()

def doJob():
    print(f"Going to sleep for 2 secs.....{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just got up from sleep....{threading.current_thread().name}")

thrd1 = threading.Thread(target=doJob, name="t1")
thrd2 = threading.Thread(target=doJob, name="t2")
thrd3 = threading.Thread(target=doJob, name="t3")

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

et = time.perf_counter()

print(f"Completed the task in {round(et - st, 2)}")
