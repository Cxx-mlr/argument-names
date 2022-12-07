```py
from identifiers import identifiers

@identifiers(function=lambda *ids: print(ids))
def func(*args):
    pass

x = 1
y = 2
func(x, x, y) # ('x', 'x', 'y')
```
