# 4 — Lists

---

# 1. Creating Lists

Lists store multiple values in a single variable.

---

## Empty List

```python id="v9p2k6"
my_list = []
```

---

## List with Values

```python id="f7m3q1"
numbers = [1, 2, 3, 4]
```

---

## Mixed Data Types

```python id="r4x8w2"
data = ["Python", 25, 3.14, True]
```

---

## Nested List

```python id="k6t1m9"
matrix = [[1, 2], [3, 4]]
```

---

# 2. Accessing List Elements (Indexing)

Lists use indexes starting from `0`.

```python id="z3n7v5"
colors = ["red", "blue", "green"]
```

| Index | Value |
| ----- | ----- |
| 0     | red   |
| 1     | blue  |
| 2     | green |

---

## Positive Index

```python id="w8q4m1"
print(colors[0])
print(colors[1])
```

Output:

```python id="x1k7p9"
red
blue
```

---

## Negative Index

```python id="u5v2t8"
print(colors[-1])
print(colors[-2])
```

Output:

```python id="m9r6x4"
green
blue
```

---

# 3. List Slicing

Syntax:

```python id="c7w3n2"
list[start:end:step]
```

---

## Examples

### Basic Slice

```python id="p4m9v7"
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
```

Output:

```python id="q8t2k5"
[20, 30, 40]
```

---

### From Beginning

```python id="d6r1x3"
print(nums[:3])
```

Output:

```python id="t5w8m9"
[10, 20, 30]
```

---

### Till End

```python id="h2n7q4"
print(nums[2:])
```

Output:

```python id="a4m6p1"
[30, 40, 50]
```

---

### Step Value

```python id="e8v5k2"
print(nums[::2])
```

Output:

```python id="b7q1x6"
[10, 30, 50]
```

---

### Reverse List

```python id="j9m3w7"
print(nums[::-1])
```

Output:

```python id="n2t8v4"
[50, 40, 30, 20, 10]
```

---

# 4. Changing List Values

```python id="g5w2m8"
colors = ["red", "blue", "green"]

colors[1] = "black"

print(colors)
```

Output:

```python id="s7k4q9"
['red', 'black', 'green']
```

---

# 5. List Length

## `len()`

```python id="m4x8t1"
nums = [1, 2, 3, 4]

print(len(nums))
```

Output:

```python id="v9q2n6"
4
```

---

# 6. Adding Elements

---

# `append()`

Adds ONE item at the end.

```python id="r7w5k3"
nums = [1, 2, 3]

nums.append(4)

print(nums)
```

Output:

```python id="c2m9v8"
[1, 2, 3, 4]
```

---

# `extend()`

Adds multiple items.

```python id="t8q1x5"
nums = [1, 2]

nums.extend([3, 4, 5])

print(nums)
```

Output:

```python id="w3n7m2"
[1, 2, 3, 4, 5]
```

---

# `insert()`

Adds item at specific position.

```python id="k1v6p9"
nums = [1, 2, 4]

nums.insert(2, 3)

print(nums)
```

Output:

```python id="d4q8t7"
[1, 2, 3, 4]
```

---

# 7. Removing Elements

---

# `remove()`

Removes specific value.

```python id="a6w2m5"
nums = [1, 2, 3, 2]

nums.remove(2)

print(nums)
```

Output:

```python id="q7v1n8"
[1, 3, 2]
```

---

# `pop()`

Removes by index.

```python id="n3x8k4"
nums = [10, 20, 30]

nums.pop(1)

print(nums)
```

Output:

```python id="m5t2q7"
[10, 30]
```

---

## Pop Last Element

```python id="v1r6w9"
nums = [1, 2, 3]

nums.pop()

print(nums)
```

Output:

```python id="p8m4x2"
[1, 2]
```

---

# `clear()`

Removes all items.

```python id="t2k7v5"
nums = [1, 2, 3]

nums.clear()

print(nums)
```

Output:

```python id="w9n3m6"
[]
```

---

# 8. Searching in Lists

---

## `in`

```python id="x5m1q8"
nums = [1, 2, 3]

print(2 in nums)
```

Output:

```python id="h7v4k2"
True
```

---

## `not in`

```python id="g8t3n1"
print(5 not in nums)
```

---

## `index()`

```python id="j4m9w6"
nums = [10, 20, 30]

print(nums.index(20))
```

Output:

```python id="q2x7v5"
1
```

---

## `count()`

```python id="s6k1m4"
nums = [1, 2, 2, 3]

print(nums.count(2))
```

Output:

```python id="n8v3q7"
2
```

---

# 9. Sorting Lists

---

# `sort()`

Sorts original list.

```python id="r2m7x9"
nums = [4, 1, 3, 2]

nums.sort()

print(nums)
```

Output:

```python id="w5q1k8"
[1, 2, 3, 4]
```

---

## Descending Order

```python id="k9v4m2"
nums.sort(reverse=True)

print(nums)
```

Output:

```python id="x3t7n5"
[4, 3, 2, 1]
```

---

# `sorted()`

Returns new sorted list.

```python id="m1q8v6"
nums = [3, 1, 2]

new_list = sorted(nums)

print(new_list)
```

---

# 10. Reversing Lists

---

# `reverse()`

```python id="t6m2w7"
nums = [1, 2, 3]

nums.reverse()

print(nums)
```

Output:

```python id="q9v5k1"
[3, 2, 1]
```

---

# 11. Copying Lists

---

## Using `copy()`

```python id="x7m3n9"
a = [1, 2, 3]

b = a.copy()

print(b)
```

---

# 12. Joining Lists

```python id="p5v1k8"
a = [1, 2]
b = [3, 4]

print(a + b)
```

Output:

```python id="n4q7m2"
[1, 2, 3, 4]
```

---

# 13. Nested Lists

```python id="r8w3k6"
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])
```

Output:

```python id="v2m9q5"
2
```

---

# 14. Loop Through Lists

---

## Using `for`

```python id="j7q2n4"
colors = ["red", "blue", "green"]

for color in colors:
    print(color)
```

---

## Using `range()`

```python id="k5m8v1"
for i in range(len(colors)):
    print(colors[i])
```

---

# 15. List Comprehension

Short way to create lists.

---

## Basic Syntax

```python id="t9x4m6"
new_list = [expression for item in iterable]
```

---

## Example — Squares

```python id="w1q7k3"
squares = [x * x for x in range(5)]

print(squares)
```

Output:

```python id="m6v2n8"
[0, 1, 4, 9, 16]
```

---

## With Condition

```python id="h3q9t5"
even = [x for x in range(10) if x % 2 == 0]

print(even)
```

Output:

```python id="p8m4v7"
[0, 2, 4, 6, 8]
```

---

# 16. Common Built-in Functions

| Function | Purpose   |
| -------- | --------- |
| len()    | Length    |
| min()    | Minimum   |
| max()    | Maximum   |
| sum()    | Total     |
| sorted() | Sort list |

---

## Examples

```python id="c1v6m9"
nums = [10, 20, 30]

print(min(nums))
print(max(nums))
print(sum(nums))
```

---

# Mini Practice Programs

---

## Program 1 — Find Largest Number

```python id="z8q3m2"
nums = [10, 50, 20, 80]

print(max(nums))
```

---

## Program 2 — Even Numbers

```python id="t4m7v1"
nums = [1, 2, 3, 4, 5]

even = [x for x in nums if x % 2 == 0]

print(even)
```

---

## Program 3 — Reverse List

```python id="n6q1k8"
nums = [1, 2, 3, 4]

print(nums[::-1])
```

---

# Quick Revision Table

| Topic              | Example             |
| ------------------ | ------------------- |
| Create List        | `[1,2,3]`           |
| Indexing           | `nums[0]`           |
| Slicing            | `nums[1:4]`         |
| Append             | `append()`          |
| Extend             | `extend()`          |
| Insert             | `insert()`          |
| Remove             | `remove()`          |
| Pop                | `pop()`             |
| Sort               | `sort()`            |
| Reverse            | `reverse()`         |
| List Comprehension | `[x for x in nums]` |

---

# One-Line Cheats

```python id="m9v3q7"
nums = [1, 2, 3]
```

```python id="q2k8w5"
nums.append(4)
```

```python id="v5m1t9"
nums.extend([5, 6])
```

```python id="x7q4n2"
nums.insert(1, 100)
```

```python id="j3m8v6"
nums.remove(2)
```

```python id="t1q7k4"
nums.pop()
```

```python id="p6v2m9"
nums.sort()
```

```python id="w8n5q1"
nums.reverse()
```

```python id="c4m7t3"
print(nums[::-1])
```

```python id="r9v1k6"
squares = [x*x for x in range(5)]
```
