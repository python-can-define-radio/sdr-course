Your task:
1. Set the frequency three times in a row with 2 seconds in between.
2. Use a loop of your choice to set the frequency to 100, 101, 102, 103, 104, 105 MHz with 1 second in between.
3. Use a loop of your choice to set the IF gain to 0, 1, 2, 3, ... 45, 46, 47 with 1 second in between.
4. Modify this example so that the frequencies are radio stations of your choice.
5. Use `random.randint`  to make it switch to each station for a random amount of time instead of a fixed amount. Hint: `random.randint(1, 5)` returns 1, 2, 3, or 4.
6. Use random.choice to randomly pick the frequency. (Note: this does not require a `for` loop.)

   Hint:
   
       while True:
           # on this line, you should pick a random freq
           tb.osmosdr_sink_0.set_center_freq(the_freq_you_picked)
