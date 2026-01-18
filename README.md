# CustomStack

CustomStack is an extended Stack (LIFO) implementation written in Python. In addition to the classical `push`/`pop` operations, it includes:

- Mode-based behavior (normal vs. monotonic increasing)
- Non-destructive “view” patterns (zigzag and wave)
- Destructive utilities (reverse, matrix reshape, pop-until)
- State snapshot and restore (checkpoint/rollback)
- Compression utilities (consecutive compression, unique compression, in-place compression)
- A lightweight state signature for quick comparisons

This repository is suitable for portfolio use, interview discussion, and experimenting with stack-oriented APIs.

---

## Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
  - [View vs Destructive Methods](#view-vs-destructive-methods)
  - [Modes](#modes)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Suggested Project Structure](#suggested-project-structure)
- [Notes and Considerations](#notes-and-considerations)
- [License](#license)

---

## Installation

No external dependencies are required.

1. Put your class into a file, for example:

- `custom_stack.py`

2. Import it in your scripts:

```python
from custom_stack import CustomStack
```

---

## Quick Start

```python
from custom_stack import CustomStack

s = CustomStack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())       # 3
print(s.peek())      # 2
print(s.elements)    # [1, 2]
```

---

## Core Concepts

### View vs Destructive Methods

Some methods only *read* and return derived outputs without modifying the stack. Others intentionally consume or modify the stack.

**View (non-destructive):**
- `peek`, `peek_k`
- `zigzag_view`, `wave_view`
- `checkpoint` (returns a copy)
- `compress`, `compress_unique`
- `signature` (computes a hash)

**Destructive (mutates or consumes the stack):**
- `pop`
- `reverse` (consumes all elements into a returned list)
- `Matrix` (consumes elements to produce a matrix)
- `pop_until`
- `rollback` (replaces current contents)
- `compress_inplace`
- `monotonic_push` (may pop elements)
- `push` when `mode="monotonic_increasing"` (delegates to `monotonic_push`)

---

### Modes

CustomStack supports two modes:

- **`normal`** (default)  
  `push(x)` behaves like a regular stack push.

- **`monotonic_increasing`**  
  `push(x)` becomes a “monotonic push”: it removes all top elements greater than `x` before pushing `x`, keeping the stack increasing from bottom to top.

Switch modes using:

```python
s.set_mode("monotonic_increasing")
```

---

## API Reference

### Constructor

#### `CustomStack(mode="normal")`
Creates a new stack.

- **Parameters**
  - `mode` (str): `"normal"` or `"monotonic_increasing"`.

---

### Basic Stack Operations

#### `isEmpty() -> bool`
Returns `True` if the stack is empty.

#### `size() -> int`
Returns the number of elements in the stack.

#### `push(element) -> None`
Pushes an element onto the stack.

- In `"normal"` mode: appends directly.
- In `"monotonic_increasing"` mode: behaves like `monotonic_push(element)`.

#### `pop()`
Pops and returns the top element.

- **Raises**
  - `IndexError` if the stack is empty.

#### `showLast()`
Returns the top element without removing it.

- **Raises**
  - `IndexError` if the stack is empty.

#### `peek()`
Alias for `showLast()`.

#### `peek_k(k: int) -> list`
Returns the top `k` elements without removing them, ordered from **top to bottom**.

Example with `elements = [1,2,3,4]` (top is `4`):
- `peek_k(3) -> [4,3,2]`

- **Raises**
  - `ValueError` if `k < 0` or `k > size()`.

---

### Mode Control

#### `set_mode(mode: str) -> None`
Sets the stack mode.

- Allowed values: `"normal"`, `"monotonic_increasing"`.
- **Raises**
  - `ValueError` if mode is unknown.

---

### Transformations (Destructive)

#### `reverse() -> list`
Consumes the stack by repeatedly popping elements into a list, returning the reversed order.

- After calling, the stack becomes empty.

Example:
- Before: `[1,2,3,4]`
- Return: `[4,3,2,1]`
- After: `[]`

#### `Matrix(rows: int, cols: int) -> list[list]`
Consumes the stack and reshapes it into a matrix of size `rows x cols` using LIFO pop order.

- **Requires**
  - `len(elements) == rows * cols`
- **Raises**
  - `ValueError` if sizes do not match.

Example:
- Stack: `[1,2,3,4,5,6]` (top is `6`)
- `Matrix(2,3) -> [[6,5,4],[3,2,1]]`
- Stack becomes empty afterwards.

---

### Pattern Views (Non-destructive)

Both of these methods return a new list derived from the stack contents without modifying `self.elements`.

#### `zigzag_view(group: int = 2) -> list`
Splits the stack into consecutive chunks of size `group`, reversing every second chunk.

- **Parameters**
  - `group` must be positive.
- **Raises**
  - `ValueError` if `group <= 0`.

Example (`group=2`):
- `[1,2,3,4,5,6] -> [1,2,4,3,5,6]`

#### `wave_view(amplitude: int = 2) -> list`
Same idea as `zigzag_view`, but the chunk size is called `amplitude`.

- **Parameters**
  - `amplitude` must be positive.
- **Raises**
  - `ValueError` if `amplitude <= 0`.

Example (`amplitude=3`):
- `[1,2,3,4,5,6,7] -> [1,2,3,6,5,4,7]`

Note: In the current implementation, `zigzag_view` and `wave_view` differ mainly by parameter naming; both alternate chunk orientation.

---

### Conditional Pop (Destructive)

#### `pop_until(value) -> list`
Pops elements from the stack until `value` is found (inclusive) or the stack becomes empty.

- Returns a list of popped elements in pop order (top-first).

Example:
- Stack: `[1,2,3,4]`
- `pop_until(2) -> [4,3,2]`
- Stack after: `[1]`

---

### State Management

#### `checkpoint() -> list`
Returns a shallow copy snapshot of the stack (`self.elements[:]`).

#### `rollback(snapshot: list) -> None`
Replaces current stack contents with the provided snapshot (copying it).

- This mutates the stack.

---

### Compression Utilities

#### `compress() -> list`
Consecutive compression (view). Removes only **adjacent duplicates** and returns a new list.

Example:
- `[1,1,2,2,2,3,3,1] -> [1,2,3,1]`

#### `compress_unique() -> list`
Global unique compression (view). Keeps the **first occurrence** of each value, removing later duplicates.

Example:
- `[1,1,2,2,3,1] -> [1,2,3]`

#### `compress_inplace() -> None`
Consecutive compression (destructive). Same logic as `compress()`, but updates `self.elements`.

---

### Identity

#### `signature() -> int`
Returns `hash(tuple(self.elements))`.

This can be used for quick state comparisons (e.g., checking whether the stack changed).  
Note: Hash values may vary between Python runs for some data types due to hash randomization.

---

### Monotonic Stack Operation (Destructive)

#### `monotonic_push(x) -> None`
Maintains an **increasing monotonic stack** (bottom to top).

- While the top element is greater than `x`, it pops.
- Then it pushes `x`.

Example:
- Start: `[3,4]`
- `monotonic_push(2)` pops `4` then `3`, pushes `2`
- Result: `[2]`

---

## Examples

### 1) Views do not change the stack

```python
s = CustomStack()
for x in [1,2,3,4,5,6]:
    s.push(x)

print(s.zigzag_view(2))   # [1, 2, 4, 3, 5, 6]
print(s.elements)         # unchanged
```

### 2) pop_until changes the stack

```python
s = CustomStack()
for x in [1,2,3,4]:
    s.push(x)

print(s.pop_until(2))  # [4, 3, 2]
print(s.elements)      # [1]
```

### 3) Monotonic mode changes what push means

```python
s = CustomStack(mode="monotonic_increasing")
for x in [5,3,4,2,6,1]:
    s.push(x)

print(s.elements)  # [1]
```

### 4) Matrix consumes the stack

```python
s = CustomStack()
for x in [1,2,3,4,5,6]:
    s.push(x)

print(s.Matrix(2,3))  # [[6,5,4],[3,2,1]]
print(s.elements)     # []
```

---

## Suggested Project Structure

```
custom-stack/
  custom_stack.py
  demo.py
  README.md
  .gitignore
```

---

## Notes and Considerations

- `reverse()` and `Matrix()` intentionally consume the stack; use `checkpoint()` if you want to restore after running them.
- `zigzag_view()` and `wave_view()` are non-destructive and are safe for display/visualization pipelines.
- `signature()` is useful for quick comparisons, but do not rely on it as a persistent identifier across different Python runs for all data types.

---

