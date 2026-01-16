# Python Libraries Part 1 - Theory - TUF+

## Python Libraries for DSA & Interviews

### (Your Toolkit for Problem Solving)

Welcome to Python Libraries!  
Python provides powerful built-in libraries for data structures and algorithms.  
Comparable to C++ STL or Java Collections - essential tools for DSA!

### Reasons to Learn

-   Save time (pre-written, optimized code)
-   Interview essential (expected knowledge)
-   Makes DSA problems easier
-   Industry standard

### Essential Libraries:

-   **Collections:** deque, Counter, defaultdict, OrderedDict, namedtuple
-   **Heapq:** priority queue
-   **Bisect:** binary search
-   **Itertools:** combinations, permutations
-   **Functools:** lru\_cache, reduce
-   **Math:** GCD, LCM, sqrt, etc.
-   **Built-in functions:** sorted, min, max, sum, etc.

---

## Built-in Functions - Common Operations

### Sorting:

`sorted(iterable, key=None, reverse=False)`

-   Returns new sorted list
-   key: function to determine sort order
-   reverse: True for descending

#### Examples:


```python
arr = [3, 1, 4, 1, 5]
sorted(arr)                    # [1, 1, 3, 4, 5]
sorted(arr, reverse=True)      # [5, 4, 3, 1, 1]

arr = [-3, 1, -4, 2, -1]
sorted(arr, key=lambda x: abs(x))   # [1, -1, 2, -3, -4]

# Sort list in-place
arr.sort()                     # Modifies original list

# Sort by custom key
words = ["apple", "pie", "banana"]
sorted(words, key=len)         # ['pie', 'apple', 'banana']
```

### Min/Max:

`min(iterable, key=None)`: Minimum value  
`max(iterable, key=None)`: Maximum value

#### Examples:

```python
min([3, 1, 4, 1, 5])           # 1
max([3, 1, 4, 1, 5])           # 5
```

### Sum/Product:

`sum(iterable, start=0)`: Sum of elements  
For product, use: `functools.reduce` or `math.prod`

#### Examples:

```python
sum([1, 2, 3, 4])              # 10
sum([1, 2, 3], 10)             # 16 (starts from 10)

import math
math.prod([2, 3, 4])          # Product: 24 (Python 3.8+)
```

### Length/Count:

`len(iterable)`: Length/count  
`count = iterable.count(value)`: Count occurrences

#### Examples:

```python
len([1, 2, 3])                 # 3
"hello".count('l')             # 2
```

### Any/All:

`any(iterable)`: True if any element is True  
`all(iterable)`: True if all elements are True

#### Examples:

```python
any([False, True, False])       # True
all([True, True, True])        # True
any([])                        # False (empty is False)
```

### Enumerate:

`enumerate(iterable, start=0)`: Returns (index, value) pairs

#### Examples:

```python
for i, val in enumerate([10, 20, 30]):
    print(i, val)              # 0 10, 1 20, 2 30
list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]
list(enumerate(['a', 'b'], 1))     # [(1, 'a'), (2, 'b')] (start=1)
```

### Zip:

`zip(*iterables)`: Combine multiple iterables

#### Examples:

```python
list(zip([1, 2], [3, 4]))      # [(1, 3), (2, 4)]
list(zip([1, 2, 3], [4, 5]))   # [(1, 4), (2, 5)] (stops at shortest)
list(zip([1, 2], [3, 4], [5, 6]))  # [(1, 3, 5), (2, 4, 6)]
```

### Reversed:

`reversed(iterable)`: Reverse iterator

#### Examples:

```python
list(reversed([1, 2, 3]))     # [3, 2, 1]
"hello"[::-1]                  # "olleh" (string slicing)
```

### Range:

`range(stop)`: 0 to stop-1  
`range(start, stop)`: start to stop-1  
`range(start, stop, step)`: with step

#### Examples:

```python
list(range(5))                 # [0, 1, 2, 3, 4]
list(range(1, 5))              # [1, 2, 3, 4]
list(range(0, 10, 2))          # [0, 2, 4, 6, 8]
```
---

## Itertools - Iteration Tools

### Import:

`import itertools`

### Functions:

```python
# Cominations: returns r-length tuples from n-length iterable
list(itertools.combinations([1,2,3], 2))      # [(1,2), (1,3), (2,3)]
# Combinations with replacement: allows repeated elements
list(itertools.combinations_with_replacement([1,2], 2))  # [(1,1), (1,2), (2,2)]
# Permutations: returns r-length tuples from n-length iterable
list(itertools.permutations([1,2], 2))        # [(1,2), (2,1)]
# Cartesian product: returns tuples from multiple iterables
list(itertools.product([1,2], [3,4]))         # [(1,3), (1,4), (2,3), (2,4)]
# Infinite iterators: cycle, repeat, chain
# - Cycle: repeats elements indefinitely
# - Repeat: repeats element to the specified count [element, times]
# - Chain: chains multiple iterables into one
list(itertools.cycle([1,2,3]))[:7]            # [1,2,3,1,2,3,1] (first 7)
list(itertools.repeat(5, 3))                  # [5, 5, 5]
list(itertools.chain([1,2], [3,4], [5]))      # [1, 2, 3, 4, 5]
# Accumulate & Groupby: cumulative operations and grouping
list(itertools.accumulate([1,2,3,4]))        # [1, 3, 6, 10] (cumulative sum)
list(itertools.accumulate([1,2,3,4], lambda x,y: x*y))  # [1, 2, 6, 24]
# Groupby: groups consecutive identical elements
groups = itertools.groupby([1,1,2,2,2,3])
[(k, list(g)) for k, g in groups]            # [(1, [1,1]), (2, [2,2,2]), (3, [3])]
```

### When to Use:

-   Generate combinations/permutations
-   Cartesian products
-   Grouping elements
-   Complex iteration patterns

  

---

## Functools - Function Tools

### Import:

`import functools`

### Functions:

```python
# LRU Cache
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)                                  # First call: computes
fibonacci(10)                                  # Second call: uses cache (instant!)

# Reduce
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])      # Sum: 10
reduce(lambda x, y: x * y, [1, 2, 3, 4])      # Product: 24
reduce(lambda x, y: x + y, [1, 2, 3], 10)     # With initial: 16

# Partial
def multiply(x, y): return x * y
double = functools.partial(multiply, 2)
double(5)                                      # 10 (2 * 5)
triple = functools.partial(multiply, 3)
triple(4)                                      # 12 (3 * 4)

# Wraps (preserves function metadata)
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### When to Use:

-   Memoization (caching)
-   Function composition
-   Reducing sequences
-   Function manipulation

---

## Math Module - Mathematical Operations

### Import:

`import math`

### Constants:

`math.pi` (3.14...)  
`math.e` (2.71...)

### Functions:

```python
math.sqrt(16)                  # Square root: 4.0
math.pow(2, 3)                 # 2^3: 8.0
math.factorial(5)              # 5!: 120
math.gcd(48, 18)               # GCD: 6
math.lcm(12, 8)                # LCM: 24 (Python 3.9+)
math.log(math.e)               # Natural log: 1.0
math.log10(100)                # Base 10 log: 2.0
math.log2(8)                   # Base 2 log: 3.0
math.sin(math.pi/2)            # sin(90°): 1.0
math.cos(0)                    # cos(0°): 1.0
math.degrees(math.pi)          # Radians to degrees: 180.0
math.radians(180)              # Degrees to radians: 3.14159...
math.ceil(4.3)                # Ceiling: 5
math.floor(4.7)                # Floor: 4
math.isfinite(10)              # Check if finite: True
math.isinf(float('inf'))       # Check if infinite: True
```

### When to Use:

-   Mathematical calculations
-   GCD/LCM
-   Prime checking
-   Distance calculations

---

## Random Module - Randomness

### Import:

`import random`

### Functions:

```python
random.random()                # Float in [0.0, 1.0): 0.123456...
random.randint(1, 10)           # Integer in [1, 10]: 7 (example)
random.randrange(0, 10, 2)     # Even numbers 0-8: 4 (example)
random.choice([1, 2, 3, 4])    # Random element: 3 (example)
random.sample([1,2,3,4,5], 3)  # 3 random elements: [2, 5, 1] (example)
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)            # Shuffle in-place: arr = [3, 1, 5, 2, 4] (example)
random.uniform(1.0, 10.0)      # Float in [1.0, 10.0]: 5.678... (example)
```

### When to Use:

-   Generate test cases
-   Shuffle arrays
-   Random sampling
-   Testing algorithms

---

## Key Takeaways

### Remember:

-   Know when to use which library
-   Understand time complexities
-   Practice common patterns
-   Read documentation when needed
