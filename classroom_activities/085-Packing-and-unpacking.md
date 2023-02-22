In the most recent signal interpretation exersise, you manually converted a binary sequence to a Unicode character. Wouldn't it be great to have the computer do this for you?

Back in the File Source and File Sink activities, we saw that if you write the number 65 to a file, it will show up as "A" in a text editor. So that means the conversion from numbers to letters is done automatically. What, then, is our task?

_Note: You may wish to review how to convert from binary to decimal, which is outside the scope of this lesson._

## A chain of numbers

We know that the binary number `101` is `5` in decimal. This is true regardless of how many leading zeros there are: `00000101` is the same as `101`.

Now, let's say we have a list of people's ages.

45, 62, 87, 21, 7, 12

You could save some space by concatenating them:

456287210712

It's certainly harder for people to read, but it makes transmission simpler because you don't need separator characters.

Notice that we had to zero-pad the single digit ages: `7` became `07`. This is necessary to make each number exactly two digits long.

### In binary

Now, let's do the same exercise in binary.

Here are the same ages in binary:

101101, 111110, 1010111, 10101, 111, 1100

And now we zero-pad and concatenate, just as before:

001011010011111001010111000101010000011100001100

Quite difficult to read, but much easier to transmit, as it can now be expressed using only two characters.

How much should we zero-pad? Thinking back to the ages example, it's possible that some people in our list would be more than 99 years old. However, it's quite unlikely that anyone is more than 999 years old. Therefore, 3-digit numbers would probably be a good fit: 53 would become 053 with padding, 7 would become 007, and 104 would be unchanged.

When working with binary, the standard is to work with groups of 8 bits. One such group is called a byte. You can see in the above example that we followed this convention:

```
Original numbers:
101101, 111110, 1010111, 10101, 111, 1100

Numbers with zero padding to 8 total digits:
00101101, 00111110, 01010111, 00010101, 00000111, 00001100

Concatenated:
001011010011111001010111000101010000011100001100
```

<details><summary>Question: What is the largest number you can express using 8 bits? (click for answer)</summary>

In binary, 11111111. In decimal, that's 255.
</details>

<details><summary>What if you're working with larger numbers? (<i>click</i>)</summary>
Use multiple bytes to express the number. That's outside the scope of this lesson, but an amusing example of using not enough bytes to express a number happened when a certain video on a certain website exceeded the max view count of 2,147,483,647. The view count overflowed and became a negative number. The website hosting the video adjusted to use more bytes, and the problem was resolved.
</details>

## Working with letters

Let's say we want to transmit the string "YES" using binary.

We would first convert the letters to decimal numbers (using the Unicode standard), then to binary:

```
       Y        E        S
      89       69       83
01011001 01000101 01010011
```

## Making the computer do the work

Let's say we have received that binary string, and we want to convert it back to the original message.

We'll convert the binary back to decimal numbers, and then the numbers back to letters. 

As you may remember, the numbers-to-letters part is taken care of already. To prove it, try this flowgraph:

`number_writer_3.grc`

```
                 |--->  UChar to Float --> Python Block: Print
Vector source  --|
                 |-->  File sink
```

- Vector source:
  - Type: byte 
  - Vector: `[76, 69, 84, 84, 69, 82, 83]`
  - Repeat: No
- File sink:
  - File: `/home/yourusername/Desktop/numberwrite_outputfile.txt`  
     _Change yourusername to your actual username_
  - Type: byte
  - Unbuffered: on
- Python Block: Print
  - _Note_: You'll create this block using the method described in an earlier exercise (036 at time of writing).

Run that GRC file, and open the text file that it produced. You'll see that you don't see any numbers, rather, it says "LETTERS". 

We can view the "behind the scenes" numbers to make sure it worked using this command in the terminal:

```
od --format=u1 myfilesinkoutputfile.txt
```

### Packing the bits

Now, we've reached one of the key steps: packing the bits.

We are imagining having received the following data:

```
01011001 01000101 01010011
```

In GNU Radio, this would be represented like so:

```
[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
```

If you simply sent that to a file sink, it would not produce the string "YES"; it would produce a sequence of non-printable characters. (Feel free to try it; different text editors will display it differently, but none of them will display "YES".)

How do we tell GNU Radio to treat each group of 8 as a single number? The Pack Bits block.

`number_writer_4.grc`

```
                               |-->  UChar to Float -->  Python Block: Print
Vector source  --> Pack Bits --|
                               |-->  File sink
```

- Vector source:
  - Type: byte 
  - Vector: `[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]`
  - Repeat: No
- Pack Bits:
  - General tab:
    - K: `8`
  - Advanced tab:
    - Comment: 
      ```
      Takes groups of 8 bits and 
      "packs" them into a single byte.
      ```
- File sink:
  - File: `/home/yourusername/Desktop/numberwrite_outputfile.txt`  
     _Change yourusername to your actual username_
  - Type: byte
  - Unbuffered: on
- Python Block: Print
  - _Note_: You'll create this block using the method described in an earlier exercise (036 at time of writing).

This should write a file that contains "YES". Success!

Recommended: Use a Time Sink to look at the data before and after packing. Note that the data after packing is far larger than 1, so you'll want to adjust the Y-Max in the Time Sink.
