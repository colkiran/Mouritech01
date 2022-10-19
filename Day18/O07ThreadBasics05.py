
import time
import threading
import concurrent.futures

ST = time.perf_counter()

def doJob(secs):
    print(f"Sleeping for {secs} seconds.....{threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just got up from sleep......{threading.current_thread().name}")
    return "hello"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = [executor.submit(doJob, sec) for sec in secs]

    for res in concurrent.futures.as_completed(results):
        print(res.result())

ET = time.perf_counter()

print(f"Completed the task in {round(ET- ST, 2)}")