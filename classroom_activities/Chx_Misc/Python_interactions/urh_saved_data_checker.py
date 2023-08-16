import os
import numpy as np


## Source for colors: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



print("""
This script checks for oversized or undersized samples
in complex data files to try to detect URH saving issues.
""")
files = os.listdir()
c = input("Enter to continue... ")
print("---------------------")

for fn in files:
    print(fn, end=" ")
    dat = np.fromfile(fn, dtype=np.complex64)
    rtw = False
    
    if any(np.isnan(dat)):
        rtw = True
        abd = None
    else:
        abd = abs(dat)
    if rtw == True or any(abd > 2) or all(abd < 0.0001):
        print(f"{bcolors.WARNING}Anomalous data detected{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN} ✓{bcolors.ENDC}")
