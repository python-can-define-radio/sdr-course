# The numpy module

https://numpy.org/doc/stable/user/absolute_beginners.html#numpy-the-absolute-basics-for-beginners

### Create a numpy array from a list

- Basic example.

```python3

## 1
## Try this.
import numpy as np

y = np.array([1, 3, 5, 6, 12, 32])
print(y)

```

### dtype=

- Each array has a data type:

```python3

## 2
## Try this.
import numpy as np

x = np.array([1, 3, 5, 6, 12, 32])
print(x)
print(x.dtype)

y = np.array([1.26, 5.0, 1.1])
print(y)
print(y.dtype)
```

- Notice that the dtype of `x` is `int64` (integers with 64 bit precision), and the dtype of `y` is `float64` (floating-point numbers with 64 bit precision).

<details><summary>What that means: </summary>

As per [this page](https://developers.google.com/discovery/v1/type-format#:~:text=string-,int64,string): "int64. A 64-bit signed integer. It has a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807 (inclusive)."

</details>

Here's a [list of numpy data types](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases).


### Create a numpy array using the linspace function

- np.linspace(start, stop, num=50, endpoint=True)  
    - Returns `num` evenly spaced samples, calculated over the interval `start, stop`. (defaults to 50 samples if not specified)
    - The endpoint of the interval can optionally be excluded `endpoint=False`. (default is True if not specified)
 
```python3
## 3
## Try this.
import numpy as np

y = np.linspace(0, 5, 10, endpoint=True)
print(y)
```

- This will create an evenly spaced array of 10 data points between 0 and 5 including 5 as the last data point.  
If `endpoint=False` was used it would give an array of 10 evenly spaced data points between 0 and 4.5 (not including the stop of 5).  
An optional approach would be to use `np.arange` which is similar to linspace, but uses a step size (instead of the number of samples). However, the [numpy docs](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) show that `np.arange` has numerical stability issues, so `np.linspace` is generally preferred.

```python3
## 4
## Try this to create the same array as the previous example with endpoint=False
import numpy as np

y = np.arange(0, 5, .5)
print(y)
```

Like all numpy arrays, arrays generated using linspace have a `dtype`. As per the [numpy docs](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) for the `np.linspace` function:

> If dtype is not given, the data type is inferred from start and stop.  
> The inferred dtype will never be an integer; float is chosen even if the arguments would produce an array of integers.

Examples:

```python3
## 5
## Try this.
import numpy as np

y = np.linspace(0, 5, 10, endpoint=False)
print(y)
print(y.dtype)
```

- If we force the issue by using `dtype=int` when the result would normally produce floats, it will still work, but may create some unintended outcomes.

```python3
## 6
## Try this.
import numpy as np

y = np.linspace(0, 5, 10, endpoint=False, dtype=int)
print(y)
```

### Operations on an array using a constant (+,-,*,/)
- addition, subtraction, and division by a constant does not work on lists

<details><summary> Expand for examples.</summary>
    
   - ### multiplying for a list
```python3 
y = [4, 5, 6]  
z = 3 * y
print(z)
```
z is now `[4, 5, 6, 4, 5, 6, 4, 5, 6]` repeats all elements 3 times
   
   - ### multiplying for an array
```python3
y = np.array([4, 5, 6])  
z = 3 * y
print(z)
```
z is now `np.array([12, 15, 18])` multiplies each element by 3
   
   - ### adding for an array (cannot be done with lists)
```python3
x =np.array([3, 8, 15])  
z = x + 3  
print(z)
```
z is now `np.array([6, 11, 18])` adds to each element by the constant
   
   - ### subtracting for an array (cannot be done with lists)
```python3
x =np.array([3, 8, 15])  
z = x - 3
print(z)
```
z is now `np.array([0, 5, 12])` subtracts from each element by the constant
   
   - ### dividing for an array (cannot be done with lists)
```python3 
x =np.array([3, 9, 18])  
z = x / 3
print(z)
```
z is now `np.array([1., 3., 6.])` divides from each element by the constant (produces floats)

</details>

### Performing operations on multiple lists or arrays (+,-,*,/)
- multiplication, subtraction, and division does not work on lists

<details><summary> Expand for examples.</summary>
    
   - ### adding for a list
```python3 
x = [5, 6, 7]  
y = [8, 9, 10]  
z = x + y
print(z)
```
z is now `[5, 6, 7, 8, 9, 10]` creates new list with all elements from each list
   
   - ### adding for an array
```python3   
x = np.array([5, 6, 7])  
y = np.array([8, 9, 10])  
z = x + y
print(z)
```
z is now `np.array([13, 15, 17])` adds each element to its counterpart same index
   
   - ### subtracting for an array (cannot be done with lists)
```python3
x =np.array([3, 8, 15])  
y =np.array([1, 2, 3])  
z = x - y
print(z)
```
z is now `np.array([2, 6, 12])` subtracts counterpart same index element from first array element
   
   - ### multiplying for an array (cannot be done with lists)
```python3
x = np.array([5, 6, 7])  
y = np.array([8, 9, 10])  
z = x * y
print(z)
```
z is now `np.array([40, 54, 70])` multiplies each element to its counterpart same index
    
   - ### dividing for an array (cannot be done with lists)
```python3
x = np.array([3, 8, 15])  
y = np.array([1, 2, 3])  
z = x / y
print(z)
```
z is now `np.array([3., 4., 5.])` divides elements in first array to its counterpart index in other array (produces float)

</details>

### Concatenate arrays 
- `np.concatenate` appends the second array to the first instead of adding each element.

```python3
## 7
## Try this.
x = np.array([3, 9, 18])  
y = np.array([64, 7, 12])  
z = np.concatenate([x, y])
print(z)
``` 
z is now `np.array([3, 9, 18, 64, 7, 12])`
   
### == with arrays

- Try the examples below.

```python3
import numpy as np

## 8
x = 5
y = 6
print(a == b)

## 9
x = 5
y = 5
print(a == b)

## 10
x = [1, 2, 3]
y = [1, 2, 4]
print(x == y)


## 11
## this will give an error; look at #12 below for correct way
x = np.array([3, 9, 18])
y = np.array([64, 7, 12])
if x == y:
     print("same")
else:
     print("different")


## 12
## This works
x = np.array([1, 2, 3])
y = np.array([1, 2, 4])
print(x == y)
areAllEqual = (x == y).all()
print(areAllEqual)


## 13
## Using the > comparison operator
x = np.array([3, 2, 1])
y = np.array([5, 0, 4])
print(x > y)


## 14
## Another example
x = np.array([4, 3, 1])
print(x > 2)



```
