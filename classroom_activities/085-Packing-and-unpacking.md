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

## Making the computer do the work

Let's say we have that binary string, and we want to convert it back to the original list of ages in a human-readable format.

First, let's make sure that we can write numbers to a file. We're going to use different numbers; you'll see why in a moment.

`number_writer_3.grc`

```
Vector source  -->  File sink
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

Run that GRC file, and open the text file that it produced. You'll see that you don't see any numbers, rather, it says "LETTERS". 

Depending on our goal, this might be a good thing. If we want to see the aforementioned ages as numbers, then perhaps not.

We can view the "behind the scenes" numbers using this command in the terminal:

```
od --format=u1 myfilesinkoutputfile.txt
```

### Looking again at the original data

TODO