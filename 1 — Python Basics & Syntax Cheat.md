# 1 — Python Basics & Syntax Cheat Sheet

---

# 1. `print()` Function

Used to display output on the screen.

## Syntax

```python
print(value)
```

## Examples

```python
print("Hello World")
print(10)
print(3.14)
```

## Multiple Values

```python
name = "Ravi"
age = 25

print(name, age)
```

Output:

```python
Ravi 25
```

## Separator

```python
print("Python", "SQL", "Power BI", sep=" | ")
```

Output:

```python
Python | SQL | Power BI
```

## End Parameter

```python
print("Hello", end=" ")
print("World")
```

Output:

```python
Hello World
```

---

# 2. Comments

Used to explain code.

## Single-line Comment

```python
# This is a comment
print("Python")
```

## Multi-line Comment

```python
"""
This is a
multi-line comment
"""

print("Hello")
```

---

# 3. Variables

Variables store data.

## Syntax

```python
variable_name = value
```

## Examples

```python
name = "John"
age = 22
salary = 25000
```

## Rules

✅ Can contain:

* letters
* numbers
* underscore `_`

❌ Cannot:

* start with numbers
* use spaces
* use keywords

## Valid Variables

```python
user_name = "Ravi"
age2 = 30
_total = 100
```

## Invalid Variables

```python
2age = 30
user name = "Ravi"
class = "Python"
```

---

# 4. Data Types

| Data Type | Example    |
| --------- | ---------- |
| int       | `10`       |
| float     | `3.14`     |
| str       | `"Python"` |
| bool      | `True`     |
| list      | `[1,2,3]`  |
| tuple     | `(1,2,3)`  |
| set       | `{1,2,3}`  |
| dict      | `{"a":1}`  |

## Check Type

```python
x = 10
print(type(x))
```

Output:

```python
<class 'int'>
```

---

# 5. `input()` Function

Used to take user input.

## Example

```python
name = input("Enter your name: ")

print(name)
```

## Important

`input()` always returns a string.

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```python
<class 'str'>
```

---

# 6. Type Conversion

Used to convert one data type to another.

| Function | Purpose            |
| -------- | ------------------ |
| int()    | Convert to integer |
| float()  | Convert to float   |
| str()    | Convert to string  |
| bool()   | Convert to boolean |

## Examples

### String to Integer

```python
age = int(input("Enter age: "))

print(age + 5)
```

### Integer to String

```python
num = 100

print(str(num))
```

### Float Conversion

```python
price = float(input("Enter price: "))
```

---

# 7. Basic Operators

---

## Arithmetic Operators

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | `5 + 2`  |
| -        | Subtraction    | `5 - 2`  |
| *        | Multiplication | `5 * 2`  |
| /        | Division       | `5 / 2`  |
| //       | Floor Division | `5 // 2` |
| %        | Modulus        | `5 % 2`  |
| **       | Power          | `5 ** 2` |

## Examples

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 3)
print(2 ** 3)
```

---

## Comparison Operators

| Operator | Meaning            |
| -------- | ------------------ |
| ==       | Equal              |
| !=       | Not Equal          |
| >        | Greater Than       |
| <        | Less Than          |
| >=       | Greater Than Equal |
| <=       | Less Than Equal    |

## Example

```python
print(10 > 5)
print(10 == 5)
```

---

## Logical Operators

| Operator | Meaning   |
| -------- | --------- |
| and      | Both True |
| or       | Any True  |
| not      | Reverse   |

## Example

```python
age = 20

print(age > 18 and age < 30)
```

---

# 8. Python Keywords

Reserved words in Python.

## Examples

```python
if
else
for
while
class
def
return
import
True
False
None
```

## View All Keywords

```python
import keyword

print(keyword.kwlist)
```

---

# 9. Indentation

Python uses indentation instead of `{}`.

## Correct

```python
if 10 > 5:
    print("Correct")
```

## Wrong

```python
if 10 > 5:
print("Wrong")
```

## Standard

Use **4 spaces**.

---

# Mini Practice Programs

---

## Program 1 — Addition

```python
a = 10
b = 20

print(a + b)
```

---

## Program 2 — User Input

```python
name = input("Enter name: ")

print("Welcome", name)
```

---

## Program 3 — Area of Rectangle

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
```

---

# Quick Revision

| Topic           | Key Point           |
| --------------- | ------------------- |
| print()         | Displays output     |
| comments        | Explain code        |
| variables       | Store data          |
| data types      | Type of value       |
| input()         | Takes user input    |
| type conversion | Change data type    |
| operators       | Perform operations  |
| keywords        | Reserved words      |
| indentation     | Defines code blocks |

---

# Common Beginner Mistakes

## Forgetting Colon `:`

❌

```python
if 5 > 2
```

✅

```python
if 5 > 2:
```

---

## Wrong Indentation

❌

```python
if True:
print("Hello")
```

✅

```python
if True:
    print("Hello")
```

---

## Adding String + Integer

❌

```python
age = input("Age: ")

print(age + 5)
```

✅

```python
age = int(input("Age: "))

print(age + 5)
```

---

# One-Line Cheats

```python
print("Hello")
```

```python
name = input("Name: ")
```

```python
age = int(input("Age: "))
```

```python
print(type(10))
```

```python
x += 1
```

```python
# Comment
```

```python
if x > 5:
    print(x)
```
