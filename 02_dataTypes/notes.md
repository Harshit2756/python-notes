
---

## String Module - String Constants

### Import:

`import string`

### Constants:

```python
string.ascii_lowercase         # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase         # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters           # Lowercase + uppercase
string.digits                  # '0123456789'
string.hexdigits               # '0123456789abcdefABCDEF'
string.punctuation             # All punctuation
string.whitespace              # Space, tab, newline, etc.
```

### When to Use:

-   Character validation
-   String filtering
-   Character set operations

  

---

## List Methods - Common Operations

### Methods:

```python
lst = [1, 2, 3]
lst.append(4)                  # Add to end: [1, 2, 3, 4]
lst.extend([5, 6])             # Extend: [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)              # Insert at index 0: [0, 1, 2, 3, 4, 5, 6]
lst.remove(3)                  # Remove first 3: [0, 1, 2, 4, 5, 6]
lst.pop()                      # Remove last: returns 6, lst = [0, 1, 2, 4, 5]
lst.pop(0)                     # Remove at index 0: returns 0, lst = [1, 2, 4, 5]
lst.index(2)                   # Index of 2: 1
lst.count(2)                   # Count of 2: 1
lst.sort()                     # Sort: [1, 2, 4, 5]
lst.sort(reverse=True)         # Sort descending: [5, 4, 2, 1]
lst.reverse()                  # Reverse: [1, 2, 4, 5]
lst.clear()                    # Clear: []
lst = [1, 2, 3]
lst2 = lst.copy()              # Shallow copy: [1, 2, 3]
```

  

---

## Dict Methods - Dictionary Operations

### Methods:

```python
d = {'a': 1, 'b': 2}
d['a']                         # Get value: 1
d['c']                         # KeyError (missing key)
d.get('a')                     # Get value: 1
d.get('c', 0)                  # Get with default: 0
d['c'] = 3                     # Set value: {'a': 1, 'b': 2, 'c': 3}
d.update({'d': 4})             # Update: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d.pop('c')                     # Remove and return: 3
d.pop('x', -1)                 # Remove with default: -1 (key not found)
d.popitem()                    # Remove last: ('d', 4)
list(d.keys())                 # View of keys: ['a', 'b']
list(d.values())               # View of values: [1, 2]
list(d.items())                # View of pairs: [('a', 1), ('b', 2)]
d.clear()                      # Clear: {}
d = {'a': 1, 'b': 2}
'a' in d                       # Check if key exists: True
d2 = d.copy()                  # Shallow copy: {'a': 1, 'b': 2}
```

  

---

## Set Methods - Set Operations

### Methods:

```python
s = {1, 2, 3}
s.add(4)                        # Add element: {1, 2, 3, 4}
s.remove(2)                    # Remove: {1, 3, 4}
s.remove(5)                     # KeyError (not found)
s.discard(3)                    # Remove: {1, 4}
s.discard(5)                    # No error (not found): {1, 4}
s.pop()                         # Remove arbitrary: returns 1, s = {4}
s.clear()                       # Clear: set()
s = {1, 2, 3}
s2 = s.copy()                   # Shallow copy: {1, 2, 3}
```

### Operations:

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 | s2                         # Union: {1, 2, 3, 4, 5}
s1 & s2                         # Intersection: {3}
s1 - s2                         # Difference: {1, 2}
s1 ^ s2                         # Symmetric difference: {1, 2, 4, 5}
{1, 2} <= s1                    # Subset: True
s1 >= {1, 2}                    # Superset: True
```

  

---

## String Methods - String Operations

### Methods:

```python
s = "Hello World"
s.upper()                       # Uppercase: "HELLO WORLD"
s.lower()                       # Lowercase: "hello world"
s.capitalize()                  # First letter capital: "Hello world"
s.title()                       # Title case: "Hello World"
"  hello  ".strip()             # Remove whitespace: "hello"
s.split()                       # Split by space: ['Hello', 'World']
s.split('l')                    # Split by 'l': ['He', '', 'o Wor', 'd']
"-".join(['a', 'b', 'c'])       # Join: "a-b-c"
s.replace('World', 'Python')    # Replace: "Hello Python"
s.find('World')                 # Find index: 6
s.find('xyz')                  # Not found: -1
s.index('World')                # Find index: 6
s.index('xyz')                 # ValueError (not found)
s.startswith('Hello')          # Check prefix: True
s.endswith('World')            # Check suffix: True
s.count('l')                   # Count occurrences: 3
"abc".isalpha()                 # All alphabetic: True
"123".isdigit()                 # All digits: True
"abc123".isalnum()              # Alphanumeric: True
```

### Slicing:

```python
s = "Hello"
s[1:4]                          # Slice: "ell"
s[:3]                           # From start: "Hel"
s[2:]                           # To end: "llo"
s[::-1]                         # Reverse: "olleH"
s[::2]                          # Every 2nd char: "Hlo"
```
---


### Objects and Immutable vs Mutable

In Python, everything is an object. This includes not only data types like integers, strings, and lists, but also functions, classes, and even modules. Each object has a unique identity, a type, and a value.

## Immutable vs Mutable Objects

![alt text](Mutability.png)

- **Always check with the identity of the object using the id() function. If the id changes after an operation, it means a new object has been created i.e the original object is immutable.**

In Python, objects can be classified as either mutable or immutable:

1. **Immutable Objects**: Means the value of the object is not changed after it is created. Examples include:
   - Integers
   - Strings
   - Tuples => ()

2. **Mutable Objects**: Means the value of the object can be changed after it is created. Examples include:
   - Lists -> []
   - Dictionaries -> {}
   - Sets -> set()
   - Custom Objects (instances of user-defined classes)

## Integers



