Convert wiki to html:

1. `git clone https://github.com/python-can-define-radio/sdr-course.wiki.git`
2. Run this:

```python
from pathlib import Path
import subprocess

print("NOT DONE YET!")
pandoc_path = Path("whatever")

p = Path(".")
mdfiles = list(p.glob("*.md"))
fns = list(map(str, mdfiles))

def runPandoc(filen):
    newFn = filen + ".html"
    subprocess.run([pandoc_path, "-s", filen, "-o", newFn])

for fn in fns:
    print("This is where you would do runPandoc(fn).")
```


