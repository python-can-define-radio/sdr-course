# SDR: Receiving 

<!--
Note regarding what goes in the quad chart:

Action: Discuss the fundamentals of Software Defined Radios (SDRs).
Standard: Students will be able to explain fundamentals of SDRs.


Evaluation: Check on Learning
-->

<!-- pandoc-only ### Purpose -->
### Summary  <!-- pandoc-exclude-line -->

Gqrx is an SDR program that can receive, view, and demodulate signals. This lesson provides basic familiarity with Gqrx.

<!-- pandoc-only ### Outcome -->

<!-- pandoc-only By the end of this lesson, students will be able to: -->  
<!-- pandoc-only - Launch the software -->  
<!-- pandoc-only - Configure basic settings for reception -->  

<!-- pandoc-only ### Learning Step Activities -->

<!-- pandoc-only - LSA 1: Launch the software -->  
<!-- pandoc-only - LSA 2: Configure basic settings for reception -->

# <!-- pandoc-only LSA 1: --> Launch the software

### Launch Gqrx

- Attach an SDR device, e.g. a HackRF One, to your computer.
- Open a terminal window on your 🖥️ computer.
- The first time you launch gqrx, reset it to its default settings.
  - Use the terminal command `$ gqrx -r`.
  - Note: "$" represents your command prompt.  Do not type it.
- On the "Configure I/O devices" window, in the "Device" dropdown menu, choose the first HackRF entry.  
  - It should look something like this:  
    - `HackRF HackRF One 123456f` 
  - Press the "OK" button at the bottom.


# <!-- pandoc-only LSA 2: --> Configure basic settings

<!-- pandoc-only ### Configure Gqrx settings -->

- Set the computer's volume to low or moderate as a starting point.
- ⚠️ **Remember to respect your fellow classmates (audio level)**.
- Click the ▶️ Play button in the top left under "File".
- Select "Input controls" on the right and set these parameters:
  - RF gain:  0 (radio frequency gain)  
    ⚠️ **Always keep the RF gain at zero.** ⚠️
  - IF gain: 32 (intermediate freqency gain)
  - BB gain: 50 (baseband gain)

<!-- pandoc-only ### Configure Gqrx settings -->

- Adjust these settings **other than RF** to improve your sound quality.
- You should see some static (noise) and spikes in the spectrum display.
- If you do not hear any static ensure your 🖥️ computer audio settings are enabled.
- If you still do not hear any static you may need to adjust your audio gain slider within the Audio pane.  

<!-- pandoc-only ### Configure Gqrx settings -->

- **Frequency**  
  - Tune your frequency to 98 Million Hz, or 98 MHz.
  - Gqrx can be tuned either in the spectrum view window or in the Receiver Options pane.
  - In the spectrum view, clicking on the top of the numbers increases, and clicking on the bottom of the numbers decreases the frequency.
    - Alternatively, you can you the mouse center wheel when the cursor is on that digit.
  - In the Frequency box of the Receiver Options pane, it would be typed: `98000.000 kHz`.

<!-- pandoc-only ### Configure Gqrx settings -->

- **Squelch**  
  - Click anywhere on the spectrum where there is no spike present.
  - In the receiver options pane, click the <kbd>A</kbd> button next to "Squelch".
  - This will readjust the noise floor dB level from `-150` dB to somewhere between `-60` dB and `-80` dB depending on the amount of "noise" present, and the speakers should go silent.
- **Mode**
  - Using the dropdown menu next to "Mode", select Wideband Frequency Modulation (WFM), either mono or stereo.

<!-- pandoc-only ### Configure Gqrx settings -->

- **Experiment**
  - Click around on different spikes in the spectrum view (some of them will be radio stations).
  - Again you may have to adjust the 🖥️ computer audio settings and/or the audio gain slider in gqrx for optimal sound quality.
  - Also remember antenna placement is very important.
  - Other than the RF gain, feel free to play around with the settings. You can always reset to default configuration with the `$ gqrx -r` terminal command.

<!-- pandoc-only ### Configure Gqrx settings -->

- **Warnings**
  - ⚠️ **Keep the RF gain at zero.** ⚠️  

  - ⚠️ **Remember to respect your fellow classmates (audio level). They may be trying to work as well.**  

### ℹ️ Resources for gqrx and HackRF One <!-- pandoc-exclude-line -->

<!-- pandoc-only ### Summary -->

<!-- pandoc-only In summary, you learned: -->

<!-- pandoc-only - How to launch the software -->  
<!-- pandoc-only - How to configure basic settings for reception -->  

<!-- pandoc-only ### References -->

- https://gqrx.dk/
- https://hackrf.readthedocs.io/en/latest/index.html
