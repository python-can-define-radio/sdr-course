Run this:

```python3
try:
    import pcdr
    print("Imported pcdr module successfully. Have fun!")
except ImportError:
    print("""
Run this in the terminal:

pip install "pcdr @ git+https://github.com/python-can-define-radio/sdr-course/#subdirectory=classroom_activities/Chx_Misc/pcdr_python_module"

      """)


## for more info on importing from a git repository: 
##    https://pip.pypa.io/en/stable/topics/vcs-support/#url-fragments
```