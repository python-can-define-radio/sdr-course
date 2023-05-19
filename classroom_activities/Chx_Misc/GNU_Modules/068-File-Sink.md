You can also write files using GNU Radio. The concepts are the same as we've just discussed in the previous exercise. Here's an example flowgraph.

# File Sink

`File_Sink_Demo_1.grc`

```
Vector Source  -->  Throttle  -->  File Sink
```

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `10`
- Vector Source:
  - Type: `byte`
  - Vector: `[70, 73, 65]`
  - Repeat: `yes`
- Throttle:
  - Type: byte
- File Sink: 
  - Type: byte
  - File: "/home/yourusername/Desktop/myfilesinkoutputfile.txt"  
         _Note: make sure to type your username instead of "yourusername". For example, "/home/bob/Desktop/myfilesinkoutputfile.txt". You can use the `pwd` command in the terminal to see an example._
  - Unbuffered: yes

Also, try adding the print block to see if it displays what you expect. You'll need to either change the type of the print block, or use a `UChar to Float` block.

### In a normal text editor...

Try opening that text file in a normal text editor before you open it using Python. Does it contain what you expect?

### Reading the numbers

To read that in Python, we can copy from an earlier exercise. Name this `read_text_file_integers_2.py`

```python3
f = open("~/Desktop/myfilesinkoutputfile.txt", "rb")
contents = f.read()
f.close()
contents_as_numbers = list(map(int, contents))
print(contents_as_numbers)
```

You can also view it in a single command on the GNU/Linux terminal:

```
od --format=u1 myfilesinkoutputfile.txt
```

