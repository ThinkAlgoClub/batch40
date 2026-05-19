# 3 — Numbers & Math Operations

---

# 1. Numeric Data Types

Python supports:

| Type    | Example  |
| ------- | -------- |
| int     | `10`     |
| float   | `3.14`   |
| complex | `2 + 3j` |

---

# 2. Integer (`int`)

Whole numbers without decimals.

## Examples

```python id="n0w2x1"
x = 10
y = -50
z = 0

print(type(x))
```

Output:

```python id="m8f3qe"
<class 'int'>
```

---

# 3. Float (`float`)

Numbers with decimal points.

## Examples

```python id="6qf0m3"
price = 99.99
pi = 3.14159

print(type(price))
```

Output:

```python id="c6m9kr"
<class 'float'>
```

---

# 4. Complex Numbers (`complex`)

Used in scientific calculations.

## Syntax

```python id="h1d6wy"
a + bj
```

---

## Examples

```python id="3rv3h8"
x = 2 + 3j

print(x)
print(type(x))
```

Output:

```python id="5h7wzn"
(2+3j)
<class 'complex'>
```

---

## Real & Imaginary Parts

```python id="h2a8z9"
x = 5 + 7j

print(x.real)
print(x.imag)
```

Output:

```python id="h4e7s1"
5.0
7.0
```

---

# 5. Arithmetic Operators

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | `5 + 2`  |
| -        | Subtraction    | `5 - 2`  |
| *        | Multiplication | `5 * 2`  |
| /        | Division       | `5 / 2`  |
| //       | Floor Division | `5 // 2` |
| %        | Modulus        | `5 % 2`  |
| **       | Power          | `5 ** 2` |

---

# 6. Addition

```python id="e1u4i7"
print(10 + 5)
```

Output:

```python id="4h3q8x"
15
```

---

# 7. Subtraction

```python id="r0p2v8"
print(10 - 3)
```

Output:

```python id="f2x7j4"
7
```

---

# 8. Multiplication

```python id="a8n6d5"
print(5 * 4)
```

Output:

```python id="o6s4z1"
20
```

---

# 9. Division `/`

Always returns float.

```python id="z5m8x2"
print(10 / 2)
print(5 / 2)
```

Output:

```python id="w7n1h3"
5.0
2.5
```

---

# 10. Floor Division `//`

Removes decimal part.

```python id="u3r9t0"
print(5 // 2)
```

Output:

```python id="l0y8m4"
2
```

---

# 11. Modulus `%`

Returns remainder.

```python id="i9w3c2"
print(10 % 3)
```

Output:

```python id="s7q1n5"
1
```

---

# 12. Power `**`

Exponentiation.

```python id="j2f6v7"
print(2 ** 3)
```

Output:

```python id="b9k3w0"
8
```

---

# 13. Operator Precedence

Order of execution.

| Priority | Operator   |
| -------- | ---------- |
| 1        | `()`       |
| 2        | `**`       |
| 3        | `* / // %` |
| 4        | `+ -`      |

---

## Example

```python id="z6h4r1"
print(2 + 3 * 4)
```

Output:

```python id="g2v9k7"
14
```

---

## Using Parentheses

```python id="n8x1m5"
print((2 + 3) * 4)
```

Output:

```python id="x4w6s3"
20
```

---

# 14. Assignment Operators

| Operator | Example  |
| -------- | -------- |
| =        | `x = 5`  |
| +=       | `x += 2` |
| -=       | `x -= 2` |
| *=       | `x *= 2` |
| /=       | `x /= 2` |

---

## Examples

```python id="v5k2m9"
x = 10

x += 5
print(x)

x *= 2
print(x)
```

Output:

```python id="t7q1e6"
15
30
```

---

# 15. `math` Module

Provides advanced math functions.

---

## Import Module

```python id="n3w7f2"
import math
```

---

# 16. Square Root

```python id="d9s5k1"
import math

print(math.sqrt(25))
```

Output:

```python id="f6j4t8"
5.0
```

---

# 17. Power

```python id="m8q2w7"
import math

print(math.pow(2, 3))
```

Output:

```python id="y3v0c4"
8.0
```

---

# 18. Absolute Value

```python id="p1d8h6"
print(abs(-20))
```

Output:

```python id="u9r5m2"
20
```

---

# 19. Ceiling Value

Rounds UP.

```python id="h7m4q9"
import math

print(math.ceil(4.2))
```

Output:

```python id="a1t6x5"
5
```

---

# 20. Floor Value

Rounds DOWN.

```python id="r6v2n1"
import math

print(math.floor(4.9))
```

Output:

```python id="e3w8p7"
4
```

---

# 21. Factorial

```python id="c4x9s2"
import math

print(math.factorial(5))
```

Output:

```python id="m5q1z6"
120
```

---

# 22. Value of PI

```python id="d0n3w8"
import math

print(math.pi)
```

Output:

```python id="v7m2c9"
3.141592653589793
```

---

# 23. Value of Euler Number

```python id="t9x6q3"
import math

print(math.e)
```

---

# 24. Min & Max

```python id="g8p4m1"
print(min(10, 5, 8))
print(max(10, 5, 8))
```

Output:

```python id="w2k7n0"
5
10
```

---

# 25. Sum Function

```python id="s1q6r8"
nums = [1, 2, 3, 4]

print(sum(nums))
```

Output:

```python id="l9t5h2"
10
```

---

# 26. Random Module

Used to generate random values.

---

## Import Module

```python id="f4v2m7"
import random
```

---

# 27. Random Integer

```python id="n7x5p1"
import random

print(random.randint(1, 10))
```

Returns random number between 1 and 10.

---

# 28. Random Float

```python id="q3m8v6"
import random

print(random.random())
```

Returns number between 0 and 1.

---

# 29. Random Choice

```python id="a9k4w2"
import random

colors = ["red", "blue", "green"]

print(random.choice(colors))
```

---

# 30. Shuffle List

```python id="j5r1n9"
import random

nums = [1, 2, 3, 4]

random.shuffle(nums)

print(nums)
```

---

# 31. Rounding Numbers

---

## `round()`

```python id="o8w6v3"
print(round(4.6))
print(round(4.4))
```

Output:

```python id="u1x5m7"
5
4
```

---

## Decimal Places

```python id="d7p2q4"
print(round(3.14159, 2))
```

Output:

```python id="f0n8h1"
3.14
```

---

# 32. Convert Between Number Types

---

## Integer to Float

```python id="m4v7q8"
x = 10

print(float(x))
```

---

## Float to Integer

```python id="x2n9w5"
price = 99.99

print(int(price))
```

Output:

```python id="p6r1k3"
99
```

---

# 33. Scientific Notation

```python id="z1w3m6"
x = 5e3

print(x)
```

Output:

```python id="k8q4v2"
5000.0
```

---

# 34. Useful Built-in Math Functions

| Function | Purpose        |
| -------- | -------------- |
| abs()    | Absolute value |
| pow()    | Power          |
| round()  | Rounding       |
| min()    | Minimum        |
| max()    | Maximum        |
| sum()    | Total          |

---

# Mini Practice Programs

---

## Program 1 — Calculator

```python id="n6t8x1"
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

---

## Program 2 — Square Root

```python id="q9r3m5"
import math

num = int(input("Enter number: "))

print(math.sqrt(num))
```

---

## Program 3 — Random Password Digit

```python id="t2w7p8"
import random

print(random.randint(1000, 9999))
```

---

# Quick Revision Table

| Topic          | Example                |
| -------------- | ---------------------- |
| Integer        | `10`                   |
| Float          | `3.14`                 |
| Complex        | `2+3j`                 |
| Addition       | `5 + 2`                |
| Division       | `5 / 2`                |
| Floor Division | `5 // 2`               |
| Modulus        | `5 % 2`                |
| Power          | `2 ** 3`               |
| Square Root    | `math.sqrt(25)`        |
| Random Integer | `random.randint(1,10)` |
| Rounding       | `round(3.14, 2)`       |

---

# One-Line Cheats

```python id="k5n1v7"
print(2 ** 3)
```

```python id="h8q4m2"
print(10 % 3)
```

```python id="v6x9p5"
print(5 // 2)
```

```python id="m1t7w8"
import math
```

```python id="j4q2n6"
math.sqrt(25)
```

```python id="z8r3v1"
round(3.14159, 2)
```

```python id="c5m9x4"
abs(-100)
```

```python id="u2p7k1"
import random
```

```python id="f7n4w3"
random.randint(1, 100)
```

```python id="e1v6q9"
random.choice(["a", "b", "c"])
```
