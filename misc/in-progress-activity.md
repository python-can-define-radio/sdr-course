Flask server:
```python3
from flask import Flask, render_template
from glob import glob
from dataclasses import dataclass
import os


@dataclass
class FC:
    name: str
    content: str

def makeFCs(filePaths):
    # type: (list[str]) -> list[FC]
    def makeone(path):
        bn = os.path.basename(path)
        with open(path) as f:
            return FC(bn, f.read())
    return list(map(makeone, filePaths))

app = Flask(__name__)



@app.route("/")
def home():
    files = glob("activity_records/*")
    return render_template("home.html", files=makeFCs(files))

if __name__ == "__main__":
    app.run()
```

`home.html`

```html
<html>
<head>
    <meta http-equiv="refresh" content="1" >

</head>
<body>
<table>
    <tr>
        <th>Timestamp</th>
        <th>Activity Frequency</th>
    </tr>
    {% for f in files %}
    <tr>
        <td>{{ f.name }}</td>
        <td>{{ f.content }}</td>
    </tr>
    {% endfor %}
</table>
</body>
</html>
```

in the activity_records dir:

name: 2022_12_14_16:19:03
content: 123.456 MHz
