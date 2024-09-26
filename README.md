# Argument Names

A Python library that provides a decorator to automatically retrieve and process the argument names of a function when it's called. This can be useful for tasks like debugging, logging, or other custom operations.

## Installation

Install argument-names via pip:

```python
pip install argument-names
```


## Use Case Example
This example demonstrates how to utilize the argument_names decorator to log the names of the arguments passed to a function:
```py
from argument_names import argument_names

@argument_names(function=lambda *args: print("Received arguments:", *args))
def process_data(_1, _2, _3):
    pass

# Example invocation
name = "Alice"
age = 30
occupation = "Engineer"

# Calling the process_data function with the specified arguments
process_data(name, age, occupation)   # Received arguments: name age occupation

process_data(occupation, age, age)   # Received arguments: occupation age age
```

```py
from argument_names import argument_names

@argument_names(function=lambda *args: print("".join(args)))
def foo(*args):
    pass

h = None
e = 1
l = 9
o = 3
w = True
r = 3.14
d = 600
_ = 0.03

foo(h, e, l, l, o, _, w, o, r, l, d) # hello_world
```
