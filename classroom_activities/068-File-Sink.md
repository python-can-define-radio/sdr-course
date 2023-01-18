# File Sink

`File_Sink_Demo_1.grc`

```
Vector Source  -->  Throttle  -->  File Sink
```

- Vector: [70, 73, 65], repeat yes, type byte
- Throttle type byte
- File Sink: 
  - Type: byte
  - File: "/home/yourusername/Desktop/myfilesinkoutputfile.txt"  
         _Note: make sure to type your username instead of "yourusername". For example, "/home/bob/Desktop/myfilesinkoutputfile.txt"
  - Unbuffered: yes

### In a normal text editor...

Try opening that text file in a normal text editor before you open it using Python. Does it contain what you expect?

### In Python...

To read that in Python, we can copy from an earlier exercise. Name this `read_text_file_integers_2.py`

```python3
f = open("~/Desktop/myfilesinkoutputfile.txt", "rb")
contents = f.read()
f.close()
contents_as_numbers = list(map(int, contents))
print(contents_as_numbers)
```
