```python3
import datetime
import time
from pcdr.flow import OsmoSingleFreqReceiver
import os


rec = OsmoSingleFreqReceiver("hackrf=0", 104.1e6)
rec.start()
avg = 0
count = 0
fn = "activity.csv"
if os.path.exists(fn):
    newfile = False
else:
    newfile = True
with open(fn, "a", encoding="utf-8") as f:
    if newfile:
        f.write("date,time,unix_timestamp,strength,avg_strength\n")
    while True:
        stren = rec.get_strength()
        avg = 0.99*avg + 0.01*stren

        count += 1
        if count == 100:  # Record every hundredth
            count = 0
            nowtime = time.time()
            dt = datetime.datetime.fromtimestamp(nowtime)
            print(f"{dt}  Activity. Recording to file.")
            f.write(f"{dt.date()},{dt.time()},{nowtime},{stren},{avg}\n")
            f.flush()

```
