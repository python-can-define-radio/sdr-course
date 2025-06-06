<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Aug 18: 050_gqrx_FM_Receive.md
2023 May 22: 040_gqrx_FM_Receive.md
</pre>
</details>

# gqrx FM Receive  

ℹ️ This material coincides with material from SDR slideshow B (slides 69-80).

⚠️ **Remember to respect your fellow classmates (audio level) they may be trying to work as well.**  
### Initial setup    
- Attach an SDR device, e.g. a HackRF One, to your computer
- Open a terminal (command line interface or CLI) window on your 🖥️ computer.  
- The first time you launch gqrx you may want to reset to its default settings using the terminal command below.  
  `$ gqrx -r`  (Note: "$" represents your command prompt.  Do not type it.)
- On the Configure I/O devices window select the "device" dropdown menu.
  - Choose the first HackRF entry which should look something like this:  
  - HackRF HackRF One `123456f` (The numbers will be part of a device identifier.) 
  <!-- - Change the input rate to `20000000` Hz (20 MHz). -->
  - Press the "OK" button at the bottom.
- Maximize or make your gqrx window as large as is practical.

### Settings 
- Check the audio volume level on your computer.  Set it to low or moderate as a starting point.
- Set gain levels (amplification) for SDR system -- Go to right side of window.  Select "Input controls".  Set these parameters:
  - RF gain:  0 (radio frequency gain)  ⚠️ **Always keep the RF gain at zero.** ⚠️ 
  - IF gain: 32 (intermediate freqency gain)  -- may be varied
  - BB gain: 50 (baseband gain)  -- may be varied
- Click the ▶️ Play button in the top left under "File".  (If the sound is much too load, Press Play button again.  Adjust system or gqrx (@ bottom right) sound level, and Play again.) 
- You should see some static (noise) and spikes in the spectrum display.
- If you do not hear any static ensure your 🖥️ computer audio settings are enabled.  
- If you still do not hear any static you may need to adjust your gain slider on the Audio pane (bottom right within gqrx).  

- **Frequency**  
  - Tune your frequency to `98.000.000`, which means 98 Million Hz, or 98 MHz. (This should allow you to see everything from 88.1 to 107.9 MHz "The FM band".) (Note: periods are used in place of commas to separate place values for one thousand, one million, etc.)
  - HOW: gqrx can be tuned either in the spectrum view window or in the Receiver Options pane (a tab on the right side).
  - In the spectrum view, clicking on the top of the numbers increases, and clicking on the bottom of the numbers decreases the frequency.  
  - In the Frequency box of the Receiver Options pane, it would be typed: `98000.000 kHz`.
- **Squelch**  
  - With your mouse, click anywhere on the spectrum where there is no spike present.
  - In the receiver options pane (on the right), click the <kbd>A</kbd> button (short for automatic) next to "Squelch".
  - This will readjust the noise floor dB level from `-150` dB to somewhere between `-60` dB and `-80` dB depending on the amount of "noise" present, and the speakers should go silent.  
- **Mode**
  - Using the dropdown menu next to "Mode", select Wideband Frequency Modulation (WFM), either mono or stereo.  
- **Experiment**
  - Click around on different spikes in the spectrum view (some of them will be radio stations).
  - Again you may have to adjust the 🖥️ computer audio settings and/or the audio gain slider in gqrx for optimal sound quality.  
  - Also remember antenna placement is very important.
  - Other than the RF gain, feel free to play around with the settings. You can always reset to default configuration with the `$ gqrx -r` terminal command.  
- **Optional**
  - You can increase the decimation in the Configure I/O devices window to get better view of the tuned frequency. Ask for a demonstration if this is unclear.

⚠️ **Keep the RF gain at zero.** ⚠️ 

⚠️ **Remember to respect your fellow classmates (audio level). They may be trying to work as well.**  

### Note: versions

- You have the option of using the GQRX AppImage, which is newer than our pre-installed GQRX. This is left as an activity for the student.

### ℹ️ Some useful resources for gqrx and HackRF One:
(Suggestion: When using a web-link, Right-Click with your mouse and select "open in new tab" or new window and then go to that tab/window.)
- https://gqrx.dk/
- https://hackrf.readthedocs.io/en/latest/index.html
