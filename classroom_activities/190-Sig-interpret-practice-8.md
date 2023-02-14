Like interpet 7, but with a delay that is a different size delay on each run.

Note that for both sig interpret 7 and 8, we should do a moving average (for which I should write a page) with length=exactly_the_symbol_length.

So 
band pass -> complex to mag -> Python block: wait for threshold -> moving average -> keep 1 in N
