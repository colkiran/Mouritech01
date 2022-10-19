
import time
import threading
import concurrent.futures

st = time.perf_counter()

def doJob(secs):
    print(f"Sleeping for {secs} second.......{threading.current_thread().name}" )
    time.sleep(2)
    print(f"Just got up from sleep.......{threading.current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)
    
    thrd1.result()
    thrd2.result()

et = time.perf_counter()
print(f"Completed the task in {round(et - st, 2)}")
