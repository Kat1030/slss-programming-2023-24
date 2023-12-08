A function is a block of code that can be reused over and over again.

We can input data to the function. We refer to the data as **parameters**.

We describe the parameters in the docstring. A docstring (short for documentation string) tells a human what the purpose of the function is.

We use the term **arguments** to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float):
	"""Calculate and pring the area of a square.
	Results are in units squared.
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a square with side length {sidelength} is: {area} square units.")

area_of_a_square(12.2)
```

## Signature

The signature of a function contains the name of the function, its inputs/parameters/type, and the return type.


## Functions With Return Values

If a function has a **return** keyword in the body, we can call it a **fruitful function**.
```python
def adder(x: int, y: int) -> int:
	"""Returns the sum of the given numbers."""
	sum = x + y

	return sum

adder(10, 2) # 12
```
The `return` keyword does two things in a function:
1. Stops the function
2. If there is a value after the `return` keyword, it sends the value back to the function call
```python
def search(l : list, item: Any) -> list:
	"""Searches through a list and returns the index.
	
	Params:
		l - a list of anything
		item - thing we are looking for
		
	Returns:
		index of the list, -1 if not found
	"""

	counter = 0

	# search algo
	for thing in l:
		if thing == item:
			return counter
		else: counter += 1

	return -1
```


## Recursion

Recursion is an elegant way to repeat a pattern.

Fractals are examples of patterns that can be described recursively.

A recursive **function** must have three parts:
1. A *function*
2. A call to itself inside of hte body code block
3. A _base case_
	1. Where the function stops calling itself

### Fibonacci Sequence and Recursion
```
Fibonacci Sequence:
1  2  3
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
		 x

fib(1) = 1
fib(2) = 1
fib(3) = fib(2) + fib(1)
	   =   1    +   1
fib(4) = fib(3)          + fib(2)
	   =   2             +   1
	   = fib(2) + fib(1) + fib(2)
	   =   1    +   1    +   1
fib(100) = fib(99) + fib(98)
```