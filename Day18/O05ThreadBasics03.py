
import time
import threading

st = time.perf_counter()

def doJob(secs, tname):
    print(f"Sleeping for {secs} second.......{tname}->  {threading.current_thread().name}" )
    time.sleep(2)
    print(f"Just got up from sleep.......{threading.current_thread().name}")

threads = []

for i in range(50):
    t = threading.Thread(target=doJob, name="t"+str(i), args=[2, 'thread-'+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"Completed the task in {round(et - st, 2)}")