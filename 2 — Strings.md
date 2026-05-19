# 2 — Strings

---

# 1. String Creation

Strings are sequences of characters.

---

## Using Single Quotes

```python id="qf4w6k"
name = 'Python'
```

## Using Double Quotes

```python id="mzix8g"
language = "Python"
```

## Using Triple Quotes

```python id="kj0q7z"
text = """Python
is
easy"""
```

---

# 2. Accessing Characters (Indexing)

Each character has an index.

```python id="4ecvlf"
text = "Python"
```

| Character      | P  | y  | t  | h  | o  | n  |
| -------------- | -- | -- | -- | -- | -- | -- |
| Positive Index | 0  | 1  | 2  | 3  | 4  | 5  |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

---

## Positive Index

```python id="7x4j5x"
text = "Python"

print(text[0])
print(text[1])
```

Output:

```python id="azmt1p"
P
y
```

---

## Negative Index

```python id="v6b5tu"
text = "Python"

print(text[-1])
print(text[-2])
```

Output:

```python id="t5wy3w"
n
o
```

---

# 3. String Slicing

Syntax:

```python id="i34f1h"
string[start:end:step]
```

---

## Examples

### Basic Slice

```python id="r2snrz"
text = "Python"

print(text[0:4])
```

Output:

```python id="0i4d7h"
Pyth
```

---

### From Start

```python id="6aqo8s"
print(text[:3])
```

Output:

```python id="l1m7k8"
Pyt
```

---

### Till End

```python id="x17j6q"
print(text[2:])
```

Output:

```python id="h1nm8z"
thon
```

---

### Step Value

```python id="3l7xka"
print(text[::2])
```

Output:

```python id="2k5t3h"
Pto
```

---

### Reverse String

```python id="7c8v1l"
print(text[::-1])
```

Output:

```python id="d8d1a7"
nohtyP
```

---

# 4. String Length

## `len()`

```python id="rvdjq9"
text = "Python"

print(len(text))
```

Output:

```python id="ocm7u6"
6
```

---

# 5. String Methods

---

## Uppercase

```python id="v8a4z3"
text = "python"

print(text.upper())
```

Output:

```python id="vdu1g6"
PYTHON
```

---

## Lowercase

```python id="6v6x8x"
text = "PYTHON"

print(text.lower())
```

---

## Capitalize

```python id="yqkhp4"
text = "python"

print(text.capitalize())
```

Output:

```python id="n57vgw"
Python
```

---

## Title Case

```python id="10j8t7"
text = "learn python"

print(text.title())
```

Output:

```python id="j26o0t"
Learn Python
```

---

## Remove Spaces — `strip()`

```python id="lyl1f7"
text = "  Python  "

print(text.strip())
```

---

## Replace Text

```python id="2bx9gl"
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```python id="h5sp1r"
I like Python
```

---

## Split String

```python id="y7i3ct"
text = "Python,SQL,Power BI"

print(text.split(","))
```

Output:

```python id="p4o8wu"
['Python', 'SQL', 'Power BI']
```

---

## Join Strings

```python id="dcrg5x"
words = ["Python", "SQL", "AI"]

print(" | ".join(words))
```

Output:

```python id="yj8mxm"
Python | SQL | AI
```

---

## Find Position

```python id="iwb6n2"
text = "Python"

print(text.find("h"))
```

Output:

```python id="w5rk71"
3
```

---

## Count Characters

```python id="90x5uh"
text = "banana"

print(text.count("a"))
```

Output:

```python id="qzq4sl"
3
```

---

# 6. Checking Methods

---

## Starts With

```python id="5wlb4r"
text = "Python"

print(text.startswith("Py"))
```

---

## Ends With

```python id="0i0pby"
print(text.endswith("on"))
```

---

## Is Digit

```python id="q3kmd9"
text = "123"

print(text.isdigit())
```

---

## Is Alphabet

```python id="oj1q6y"
text = "Python"

print(text.isalpha())
```

---

## Is Alphanumeric

```python id="9h2tqg"
text = "Python123"

print(text.isalnum())
```

---

# 7. String Concatenation

Combine strings using `+`.

```python id="8qev4s"
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```python id="0uh37s"
Hello World
```

---

# 8. String Repetition

```python id="i6vtrt"
print("Python " * 3)
```

Output:

```python id="j2zx0d"
Python Python Python
```

---

# 9. Escape Characters

Used for special formatting.

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New Line     |
| `\t`   | Tab          |
| `\\`   | Backslash    |
| `\'`   | Single Quote |
| `\"`   | Double Quote |

---

## New Line

```python id="qwhd9v"
print("Python\nSQL")
```

Output:

```python id="l3pjpd"
Python
SQL
```

---

## Tab Space

```python id="4hcn3t"
print("Python\tSQL")
```

---

## Quotes Inside String

```python id="vz8xih"
print("He said \"Hello\"")
```

---

# 10. f-Strings (Formatted Strings)

Best way to insert variables into strings.

---

## Basic Example

```python id="6bg0m6"
name = "Ravi"
age = 25

print(f"My name is {name} and I am {age}")
```

Output:

```python id="m6jxtw"
My name is Ravi and I am 25
```

---

## Expressions Inside f-Strings

```python id="7a80w2"
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```python id="km5e4z"
Sum = 30
```

---

# 11. String Formatting

---

## Using `format()`

```python id="nwh4j0"
name = "Ravi"
age = 25

print("My name is {} and age is {}".format(name, age))
```

---

## Indexed Formatting

```python id="8o5s6n"
print("{1} is learning {0}".format("Python", "Ravi"))
```

Output:

```python id="d4q3y4"
Ravi is learning Python
```

---

# 12. Multiline Strings

```python id="ptkgv3"
message = """
Python
SQL
Power BI
"""

print(message)
```

---

# 13. Membership Operators

Check if text exists.

---

## `in`

```python id="s1t3b5"
text = "Python"

print("Py" in text)
```

---

## `not in`

```python id="8v1s6e"
print("Java" not in text)
```

---

# 14. Immutable Nature of Strings

Strings cannot be changed directly.

❌ Wrong

```python id="e7z5sl"
text = "Python"

text[0] = "J"
```

✅ Correct

```python id="gxjlwm"
text = "Python"

text = "J" + text[1:]

print(text)
```

Output:

```python id="xfmgcu"
Jython
```

---

# Mini Practice Programs

---

## Program 1 — Reverse String

```python id="sm8w3t"
text = input("Enter text: ")

print(text[::-1])
```

---

## Program 2 — Count Vowels

```python id="20v4ys"
text = input("Enter text: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)
```

---

## Program 3 — Palindrome Check

```python id="7k9mho"
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# Quick Revision Table

| Topic         | Example      |
| ------------- | ------------ |
| Create String | `"Python"`   |
| Indexing      | `text[0]`    |
| Slicing       | `text[1:4]`  |
| Reverse       | `text[::-1]` |
| Length        | `len(text)`  |
| Uppercase     | `upper()`    |
| Lowercase     | `lower()`    |
| Replace       | `replace()`  |
| Split         | `split()`    |
| Join          | `join()`     |
| f-string      | `f"{name}"`  |

---

# One-Line Cheats

```python id="gj8i7k"
text = "Python"
```

```python id="u9p73y"
print(text[0])
```

```python id="jrz1n4"
print(text[::-1])
```

```python id="0s86e7"
print(text.upper())
```

```python id="ozst9x"
print(text.lower())
```

```python id="4ye2p5"
print(text.replace("P", "J"))
```

```python id="wg2hr0"
print(len(text))
```

```python id="mj1lq0"
print(f"Hello {text}")
```

```python id="fxkm8h"
print("Py" in text)
```

```python id="otprq5"
print(text.split())
```
