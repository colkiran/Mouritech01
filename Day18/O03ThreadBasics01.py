# synchronous / sequential execution of code

import time

st = time.perf_counter()
def doJob():
    print("Going to sleep for 2 secs.....")
    time.sleep(2)
    print("Just got up from sleep....")

doJob()
doJob()
doJob()

et = time.perf_counter()

print(f"Completed the task in {round(et - st, 2)}")
