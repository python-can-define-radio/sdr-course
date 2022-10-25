## Disclaimer

Many uses of this are illegal. Stay legal, ethical, moral, honorable, and kind.

## Summary

This involves two flowgraphs.

First flowgraph: `record_iq_data.grc`:
```
Osmocom Source ⟶  DC Blocker  ⟶  File Sink
                              ⟶  Waterfall Sink
                              ⟶  Time Sink
```

Second flowgraph: `replay_iq_data.grc`:
```
File Source  ⟶  Osmocom Sink
             ⟶  Waterfall Sink
             ⟶  Time Sink
```

## How to set the Parameters

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `2e6`  (You may need more depending on whether the signal fits in the waterfall.)

### For the Osmocom Source AND Sink:

- Ch0: Frequency (Hz): You'll have to figure this out based on the device you're working with. I highly recommend tuning off-center from the signal that you are intending to record. Whatever frequency you pick for recording should match the frequency you pick for replaying.
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): Will depend a lot on your situation. Look up the valid numbers for your device, and try to adjust so that the signal you're recording is approximately -0.6 to 0.6 on the Time Sink.
- Ch0: BB Gain (dB): See note on IF Gain.

### For the File Sink:

- You'll want to pick a **_new, non-existing_** file. A common mistake is to pick the `.grc` file that you are currently editing. This is definitely not what you want -- the goal is to save the data in a separate file, not overwrite the flowgraph that you're working on.
  - I recommend picking a directory for your file, and naming it `my_gnu_recording.iq`. The file extension can be anything you want (ask if you're curious why), but `.iq` seems somewhat common in the SDR community.
    - A good example may look like this:  
      `/home/yourusername/Desktop/my_gnu_recording.iq`

### For the File Source:

- After you've recorded a file, you'll pick that file that you've recorded.

### For the Waterfall Sink:

- Leave all as defaults.

### For the Time Sink:

- Leave all as defaults.

### For the DC Blocker:

- Leave all as defaults.

