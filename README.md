# CustomStack – Beyond Classical LIFO

CustomStack is an extended stack implementation written in Python.
It goes beyond the classical LIFO (Last In, First Out) behavior by introducing
pattern-based traversals, state management utilities, and analytical stack operations.

This project is designed as a portfolio-oriented exploration of data structure design,
focusing on behavior, extensibility, and clarity.

---

## Features

- Classic stack operations (push, pop, peek)
- Mode-based behavior (normal / monotonic)
- Non-destructive traversal patterns
- Destructive conditional operations
- Stack state checkpointing and rollback
- Analytical and transformation utilities

---

## Design Philosophy

The stack is designed around three core ideas:

1. Separation of concerns  
   Some methods only view the stack, others intentionally mutate it.

2. Pattern-oriented traversal  
   Stack elements can be observed using zigzag or wave patterns.

3. Behavior-driven design  
   The same push API can behave differently based on the active mode.

---

## Installation

```bash
git clone https://github.com/your-username/custom-stack.git
cd custom-stack
```

No external dependencies are required.

---

## Basic Usage

```python
from custom_stack import CustomStack

s = CustomStack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.peek())
```

---

## Stack Modes

### Normal Mode

```python
s = CustomStack(mode="normal")
```

Classic LIFO behavior.

### Monotonic Increasing Mode

```python
s = CustomStack(mode="monotonic_increasing")
```

Automatically maintains an increasing monotonic stack.

---

## Non-Destructive View Operations

### zigzag_view(group=2)

Alternates direction for each fixed-size group.

### wave_view(amplitude=3)

Applies chunk-based oscillating traversal.

### peek_k(k)

Returns the top k elements without removing them.

---

## Destructive Operations

### pop_until(value)

Pops elements until the given value is found.

### reverse()

Reverses the stack using pure stack logic.

### Matrix(rows, cols)

Consumes the stack and reshapes it into a matrix.

---

## Compression Utilities

### compress()

Removes consecutive duplicate elements.

### compress_unique()

Removes all duplicate elements globally.

### compress_inplace()

Applies compression and mutates the stack.

---

## State Management

### checkpoint()

Creates a snapshot of the stack.

### rollback(snapshot)

Restores a previous snapshot.

---

## Identity

### signature()

Returns a hash-based signature of the stack state.

---

## Demo

```bash
python demo.py
```

---

## Project Structure

custom-stack/
  custom_stack.py
  demo.py
  README.md
  .gitignore

---

## License

MIT License
