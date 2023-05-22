<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Oct 12: 057-File-Source.md
2022 Oct 17: 065-File-Source.md
2023 Feb 22: 065-Unicode-and-File-Source.md
2023 May 22: 010_Unicode_and_File_Source.md
</pre>
</details>

We've talked about sending pulses to represent binary. However, most "real life"  data is more interesting than simply zeros and ones (even if it is stored as zeros and ones on the hard drive). We're going to talk about how text is stored as binary, and how to work with text in both GNU Radio and Python.

# Reading from Files

We've used a Vector Source block to provide data. Now, let's try a File Source. First, we're going to build the concepts in Python.

Let's create a file. Name this `create_text_file_1.py`.

```python3
f = open("my_text_file.txt", "w")
f.write("ABCD")
f.close()
```

When you run this, it won't display any output in the terminal; it only creates a text file. Open that text file in the editor of your choice to verify that it contains ABCD.

Now, let's read the file in Python. Name this `read_text_file_basic.py`.

```python3
f = open("my_text_file.txt", "r")
contents = f.read()
f.close()
print(contents)
```

This reads the file.

However, we'll see later that when GNU Radio reads the file, it's going to produce numbers instead of letters. Where do the numbers come from?

## Encoding

All data on a computer is stored as binary (0s and 1s). So when we asked Python to write "ABCD", behind the scenes, it converted each letter to a sequence of zeros and ones. This is called _encoding_ the data.

The most common way to encode text is Unicode. Here are a few characters in Unicode:

| Letter | Decimal | Hexadecimal | Binary   |
|--------|---------|-------------|----------|
| A      | 65      | 41          | 01000001 |
| B      | 66      | 42          | 01000010 |
| C      | 67      | 43          | 01000011 |

<details><summary>:information_source: Note:</summary>
  
If you look up a [Unicode table](https://unicode-table.com/en/#0041), you'll often see the hexadecimal representation.

Also, we've generally found that more people have heard of ASCII than Unicode. Unicode and ASCII are the same for the Basic Latin characters (A through Z, a through z), so for the purpose of this class, you can think of them as synonymous. 

</details>

So, when we asked Python to write "ABCD", it wrote this:

```
01000001  01000010  01000011  01000100
```

<details><summary>:information_source: Note:</summary>
  
The spaces between binary numbers are not actually written to the file. They are there for ease of reading.

</details>

We usually don't see the binary because most tools that open the file will interpret the numbers as text. But we can ask Python to interpret it as numbers:

Filename: `read_text_file_integers.py`

```python3
f = open("my_text_file.txt", "rb")
contents = f.read()
f.close()
contents_as_numbers = list(map(int, contents))
print(contents_as_numbers)
```

This will print the decimal representations: [65, 66, 67, 68], which corresponds to ABCD.

<details><summary>:information_source: If you want to see it as binary:</summary>
  
We can ask Python to display the numbers as binary:

```python3
def binformat(x):
    return f"{x:08b}"
contents_as_binary = list(map(binformat, contents_as_numbers))
print(contents_as_binary)
```
</details>

### Plotting in Python

To prepare for what we'll see in GNU Radio, let's plot some data in Python.

Name this `python_plot_basic_3.py`.

```python3
import matplotlib.pyplot as plt

datapoints = [20, 30, 40, 10, 50, 60, 80]

plt.plot(datapoints, "o")

plt.show()
```

That example doesn't read from a file. Let's make it do that:

`python_plot_from_file_1.py`
```python3
import matplotlib.pyplot as plt

f = open("my_text_file.txt", "rb")
contents = f.read()
f.close()
datapoints = list(map(int, contents))

plt.plot(datapoints, "o")

plt.show()
```

You should see four data points (one each for the characters ABCD).

Let's make the file a little bit longer. This will help when we get to the GNU Radio part.

Run this to write the longer file:

`create_text_file_2.py`
```python3
f = open("my_text_file.txt", "w")
f.write("ABC ABC ABC ABC THERE ARE WORDS IN THIS FILE")
f.close()
```

Then re-run your python plotting program (`python_plot_from_file_1.py` above). See if you can spot the ABC ABC ABC ABC in the plot.

### Plotting in GNU Radio

We're going to do the same thing in GNU Radio.

Name this `file_source_time_sink_1.grc`
```
File Source  -->  UChar to Float  -->  Time Sink
```

<details><summary> :information_source: What's <kbd>UChar to Float</kbd>? (Click to expand) </summary>

We want to read the File Source using the purple type, a.k.a. Integer 8. That type tells GNU Radio to interpret the file data in the way described above. However, the Time Sink expects Float data instead of Integer data, so we must convert the values using <kbd>UChar to Float</kbd>.

</details>

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `1`
- File Source:
  - File: _Click the "..." button, and then pick the text file that you created earlier using Python (`my_text_file.txt`)._
  - Output Type: `byte`
  - Repeat: `No`
- Time Sink:
  - General Tab:
    - Type: `Float`
    - Number of Points: `40`
    - Y min: `0`
    - Y max: `100`
  - Config Tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

You should see a graph that looks very similar to the one we saw in Python.

Things to try:
- Use the Print block in addition to the Time Sink. Does it print what you expect?