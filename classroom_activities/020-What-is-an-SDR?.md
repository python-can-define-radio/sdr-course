Well, it's a Software Defined Radio. But you're probably looking for a more in-depth answer than that.

So, let's look at what a radio is. Even before that, we'll start with what a wave is.

## What is a wave?

### Slinkies and Sound

Here's a [slinky](https://www.youtube.com/watch?v=g8GcMn7K0u4?t=11).

What's waving? The metal.

You can also make the metal wave [longitudinally](https://www.youtube.com/watch?v=fMJrtheQfZw).

But what if you wanted to convey audio?

Let's talk about the classic [string-between-two-cans](https://duckduckgo.com/?q=string+between+two+cans&t=h_&iar=images&iax=images&ia=images).

```
-------                     -------
  Can  ------- String ------  Can  
-------                     -------
```

1. What's happening?
2. What's waving?
3. Is it a longitudinal wave or a transverse wave?

(_discuss in small groups. For more info, [see this video](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound/sound-topic/v/sound-properties-amplitude-period-frequency-wavelength)._)

### Microphones

Let's imagine a new, similar setup:

```
--------------        -------------               -----------
  Microphone ---Wire--- Amplifier ----- Wire ------ Speaker
--------------        -------------               -----------
```

What's the difference between this and the string+cans setup?

What kind of signal is carried on the string? On the wire?

(_discuss in small groups._)

### Radios

A radio is almost identical:

```
                         <Radio 1>                    <Radio 2>
--------------        --------------                 ----------              -----------
  Microphone ---Wire--- Transmitter ~~~~~~ Air ~~~~~~ Receiver --- Wire ------ Speaker
--------------        --------------                 ----------              -----------
```
A traditional radio transmitter (Radio 1) is composed of electronics hardware without software.
So too, a traditional radio receiver (Radio 2) is composed of electronics hardware without software.

### Software Defined Radio (SDR)
In an SDR the transmitter and/or receiver functionality is divided into hardware and software:

```
                         <SDR 1>                      <Radio 2>
--------------        --------------                 ------------          ----------
  Microphone ---Wire--- Transmitter ~~~~~~ Air ~~~~~~ Receiver  --- Wire --- Speaker
--------------          [software]                    [software]           ----------
                       +[hardware]                   +[hardware] 
                      --------------                 ------------
```

The hardware and software of the transmitter may be housed in a single package or unit, e.g., a hand-held digital radio or a digital car radio, or may be housed in separate packaging, e.g., a computer and an SDR device.  The SDR device may be called the "transmitter," but, as stated above, some of the funcionality of transmission is allocated to a separte computing device.

(Of course, in some SDR systems, the microphone may be connected to the transmitter via a wireless communication technology.)


## For more info...

See https://wiki.gnuradio.org/index.php?title=What_Is_GNU_Radio
