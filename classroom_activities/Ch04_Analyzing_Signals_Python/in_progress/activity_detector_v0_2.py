import datetime
import time
from pcdr.flow import OsmoSingleFreqReceiver
import os
from playsound import playsound
 
 
def safePlay(fn, block):
    try:
        playsound(fn, block=block)
    except Exception:
        print("Failed to play the sound.")
 
 
rec = OsmoSingleFreqReceiver("hackrf=0", 462.7e6)
rec.start()
short_avg = 0
long_avg = 5  # Arbitrary; adjust to taste
count = 0
start_time = time.time()
fn = "activity.csv"
if os.path.exists(fn):
    newfile = False
else:
    newfile = True
with open(fn, "a", encoding="utf-8") as f:
    if newfile:
        f.write("passedThresh,date,time,unix_timestamp,time_since_start,strength,short_avg,long_avg\n")
    
    while True:
        stren = rec.get_strength()
        short_avg = 0.9*short_avg + 0.1*stren
        long_avg = 0.9999*long_avg + 0.0001*stren
        count += 1
        if count == 100:  # Record every hundredth
            count = 0
 
            nowtime = time.time()
            timedelta = nowtime - start_time
            dt = datetime.datetime.fromtimestamp(nowtime)
            print(f"{dt}  Recording to file.")
 
            if short_avg > 1.2 * long_avg:
                safePlay("Bell.wav", block=False)
                print("BIG SPIKE")
                f.write("BIG SPIKE,")
            elif short_avg > 1.1 * long_avg:
                safePlay("Buzzer.wav", block=False)
                print("SPIKE")
                f.write("SPIKE,")
            else:
                f.write("NO,")
            f.write(f"{dt.date()},{dt.time()},{nowtime},{timedelta},{stren},{short_avg},{long_avg}\n")
            f.flush()
