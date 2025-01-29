# Unit conversions

Many of us have heard frequency units mentioned, for example, when buying a router that has 2.4 GHz or 5 GHz capability. This lesson discusses how to convert between different frequency units, and how to express those using scientific notation (e.g., `2.4e9` = 2.4 GHz).

### Reference Table

|                    | 1 Hz | 1 kHz    | 1 MHz        | 1 GHz            |
|--------------------|------|----------|--------------|------------------|
| Converted to Hz    | 1 Hz | 1,000 Hz | 1,000,000 Hz | 1,000,000,000 Hz |
| Converted to GHz   |   0.000 000 001 GHz  |     0.000 001 GHz     |       0.001 GHz       |         1 GHz    |
| Scientific notation| 1 Hz | 1e3 Hz   | 1e6 Hz       | 1e9 Hz           |

![Image showing MHz, kHz, and Hz place values](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/ghz.jpg?raw=true)  

_Image source: https://www.trendytechbuzz.com/2016/11/what-is-gigahertz-ghz-or-megahertz-mhz.html_

### Reviewing the basics

Most of us learned fairly early in school how to say numbers like these:

- 23,000 = twenty three thousand
- 6,200,000 = six point two million

We may also have experience saying these numbers using metric prefixes:

- 23,000 Hz = twenty three thousand Hertz = twenty three kilohertz
- 6,200,000 = six point two million Hertz = six point two Megahertz

The challenge often arises when we need to convert between, for example, Gigahertz and Megahertz. For example, how would you express 2 GHz in Megahertz? We are going to try to use an intuitive approach.

_Answers appear at the end of the page for checking your work._


```
## Exercise 1
## Given: 1 GHz = 1,000 MHz
## Determine the following:
## a.   2    GHz = ____ MHz
## b.   2.3  GHz = ____ MHz
## c.  52    GHz = ____ MHz
## d.   0.3  GHz = ____ MHz
## e.   0.04 GHz = ____ MHz
## f.  ____  GHz = 7000 MHz
## g.  ____  GHz = 2500 MHz
## h.  ____  GHz =  734 MHz
## i.  ____  GHz =   40 MHz
## j.  23.73 GHz = ____ MHz
```

```
Exercise 2
## Given: 1 MHz = 1,000,000 Hz
## Given: 1 kHz = 1,000 Hz
## Determine the following:
## a.  2   MHz = ____ Hz  = ____ kHz
## b.  1   MHz =    ____ kHz
## c.  7.3 MHz =    ____ kHz
## d.  0.6 MHz =    ____ kHz
## e. 23.6 MHz =    ____ kHz
## f. ____ MHz =    2345 kHz
## g. ____ MHz =     600 kHz
## h. ____ MHz =  106200 kHz
```

```
## Exercise 3
## Given: 1 GHz = 1,000,000,000 Hz
## Given: 1 MHz = 1,000,000 Hz
## Given: 1 kHz = 1,000 Hz
## Determine the following:
## a. 3 GHz  = ___ Hz
## b. 10 MHz = ___ Hz
## c. 3,260,000 Hz = ___ MHz
## d. 342 MHz = ___ GHz
```

```
## Exercise 4
## The channels for a particular radio frequency band range from 88 MHz to 108 MHz with a spacing of 200 kHz.
## a. The first channel spans from 88.0 MHz to ___ MHz.
## b. The center of the first channel is ____ MHz.
## c. The second channel spans from _____ to ____ MHz.
## d. The center of the second channel is ____ MHz.
## e. The center of the third, fourth, fifth, and sixth channels are ____, ____, ____, ____.
## f. (optional, may require Internet research) In the United States, these are channels that are licensed for ____.
```


```python3
## Exercise 5
## In python, evaulate the following:
print(7e3)
## It should display 7000.0, that is, seven thousand.
## Convert the following from scientific notation to standard notation:
## a. 26e3   Hz = ____
## b.  2.7e3 Hz = ____
## c.  7e6   Hz = ____
## d. 98e6   Hz = ____
```

```
## Exercise 6
## a. List the numbers from 10 to 20 with a step size of 2, including both endpoints.
## b. Same exercise, but from 3000 to 7000 with a step size of 1000.
## Now try doing it with scientific notation. (e.g. 3e3 is our starting point)
## c. Same exercise, but start=2e3, stop=6e3, step=1e3.
## d. Same exercise, but start=8e6, stop=9e6, step=200e3.
## e. Same exercise, but start=2.4e9, stop=2.6e9, step=500e6.
```

<details><summary>Exercise 1 Answers:</summary>

```
a. 2,000 MHz
b. 2,300 MHz
c. 52,000 MHz
d. 300 MHz
e. 40 MHz
f. 7 GHz
g. 2.5 GHz
h. 0.734 GHz
i. 0.04 GHz
j. 23,730 MHz
```

</details>

<details><summary>Exercise 2 Answers:</summary>

```
a. 2,000,000 Hz = 2,000 kHz
b. 1,000 kHz
c. 7,300 kHz
d. 600 kHz
e. 23,600 kHz
f. 2.345 MHz
g. 0.6 MHz
h. 106.2 MHz
```

</details>

<details><summary>Exercise 3 Answers:</summary>

```
a. 3,000,000,000 Hz
b. 10,000,000 Hz
c. 3.26 MHz
d. 0.342 GHz
```

</details>

<details><summary>Exercise 4 Answers:</summary>

```
a. 88.2 MHz
b. 88.1 MHz
c. 88.2 to 88.4 MHz
d. 88.3 MHz
e. 88.5, 88.7, 88.9, 90.1
f. FM Radio
```

</details>

<details><summary>Exercise 5 Answers:</summary>

```
a. 26,000 Hz
b. 2,700 Hz
c. 7,000,000 Hz
d. 98,000,000 Hz  
```

</details>

<details><summary>Exercise 6 Answers:</summary>

```
a. 10, 12, 14, 16, 18, 20
b. 3000, 4000, 5000, 6000, 7000  or
    3e3,  4e3,  5e3,  6e3,  7e3
c. 2e3, 3e3, 4e3, 5e3, 6e3
d. 8e6, 8.2e6, 8.4e6, 8.6e6, 8.8e6, 9.0e6
e. 2.4e9, 2.45e9, 2.5e9, 2.55e9, 2.6e9
```

</details>
