
# SDR Discussion

ℹ️ This material coincides with material from SDR slideshow A (slides 7-8, 21-22).

What is an SDR?  Well, it's a Software Defined Radio. But you're probably looking for a more in-depth answer than that.

So, let's look at what a radio is. Even before that, we'll start with what a wave is.

### What is a wave?

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

(_discuss in small groups. For more info about waves, [see this video](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound/sound-topic/v/sound-properties-amplitude-period-frequency-wavelength). See also [a speaker in slow motion](https://www.youtube.com/watch?v=J2BUvWRCBGM)._ )

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

A radio system is similarily interconnected:

```
                         <Radio 1>                    <Radio 2>
--------------        --------------                 ----------              -----------
  Microphone ---Wire--- Transmitter ~~~~~~ Air ~~~~~~ Receiver --- Wire ------ Speaker
--------------        --------------                 ----------              -----------
```

A traditional radio transmitter (Radio 1) is composed of electronics hardware without software.
So too, a traditional radio receiver (Radio 2) is composed of electronics hardware without software.

A "gimme" question:  What type of signal is exchanged through the air?  

### Software Defined Radio (SDR)

In an SDR, the transmitter and/or receiver functionality is divided into hardware and software:

```
                         <SDR 1>                      <SDR 2>
--------------        --------------                -------------             ----------
  Microphone ---Wire-- Transmitter(TX) ~~~ Air ~~~~~ Receiver(RX) --- Wire ---- Speaker
--------------          [software]                    [software]              ----------
                            +                             + 
                        [hardware]                    [hardware] 
                      --------------                -------------
```

The hardware and software of the software defined radio (SDR) may be housed in a single package or unit, e.g., a two-way hand-held digital radio or a digital car radio receiver, or may be housed in separate packaging, e.g., a computer and an SDR device.
<details> <summary> ℹ️ Expand for further explanation </summary>
 
* The diagram above shows two separate SDR's, one designated as the transmitter and the other as the receiver.  Either SDR may, optionally, communicate with a traditional radio as well.  
* Most SDR devices can be operated in both a transmission mode and a reception mode.
* Depending on its mode of operation, an SDR device may be called the "transmitter", the "reciever", or the "transciever.  For either mode of SDR operation (transmission or reception), some of the functionality is allocated to a separate computing device.
* In current discussion, the term "computer" may refer to a desktop computer, a laptop computer, a tablet computer, or a mobile smart telephone, as examples.
* Although wires are shown in the diagram, in some SDR systems, the microphone, speaker, etc. may be connected to the SDR via wireless communication technology.

</details>

_Further reading: https://wiki.gnuradio.org/index.php?title=What_Is_GNU_Radio_
