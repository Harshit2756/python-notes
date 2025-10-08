#  deamons are the threads which automatically shudowns when the main program shutdowns
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temprature.......")
        time.sleep(2)

t=threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")