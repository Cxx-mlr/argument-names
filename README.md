# Argument Names

A Python library that provides a decorator to automatically retrieve and print the argument names of a function when it's called. This can be particularly useful for debugging or logging purposes.

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
process_data(name, age, occupation)  
# This will output: Received arguments: name age occupation
```
