#  non-deamons are the threads don't shutdown when the main program completes
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temprature.......")
        time.sleep(2)

t=threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")