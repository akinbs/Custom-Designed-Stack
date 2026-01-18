class CustomStack:

    def __init__(self, mode="normal"):
        self.elements = []
        self.set_mode(mode)


    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def push(self, element):

        if self.mode == "normal":
            self.elements.append(element)
        elif self.mode == "monotonic_increasing":
            self.monotonic_push(element)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.elements.pop()

    def showLast(self):
        if self.isEmpty():
            raise IndexError("showLast from empty stack")
        return self.elements[-1]

    def peek(self):
        return self.showLast()

    def peek_k(self, k):
        if k < 0:
            raise ValueError("k must be >= 0")
        if k > self.size():
            raise ValueError("k cannot be greater than stack size")
        return list(reversed(self.elements[-k:]))

    def set_mode(self, mode):
        allowed = {"normal", "monotonic_increasing"}
        if mode not in allowed:
            raise ValueError(f"mode must be one of {allowed}")
        self.mode = mode

    def reverse(self):
        reversed_stack = []
        while not self.isEmpty():
            reversed_stack.append(self.pop())
        return reversed_stack

    def Matrix(self, rows, cols):
        if len(self.elements) != rows * cols:
            raise ValueError("The number of elements in the stack must be the same as rows*cols.")

        matrix = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(self.pop())  
            matrix.append(row)
        return matrix

    def zigzag_view(self, group=2):
        if group <= 0:
            raise ValueError("group must be positive.")

        arr = self.elements[:]
        out = []
        flip = False
        i = 0
        while i < len(arr):
            chunk = arr[i:i+group]
            if flip:
                chunk.reverse()
            out.extend(chunk)
            flip = not flip
            i += group
        return out

    def wave_view(self, amplitude=2):
        if amplitude <= 0:
            raise ValueError("amplitude must be positive.")

        arr = self.elements[:]
        out = []
        flip = False
        i = 0
        while i < len(arr):
            chunk = arr[i:i+amplitude]
            if flip:
                chunk.reverse()
            out.extend(chunk)
            flip = not flip
            i += amplitude
        return out

    def pop_until(self, value):
        out = []
        while not self.isEmpty():
            x = self.pop()
            out.append(x)
            if x == value:
                break
        return out

    def checkpoint(self):
        return self.elements[:]

    def rollback(self, snapshot):
        self.elements = snapshot[:]

    def compress(self):
        if self.isEmpty():
            return []
        out = [self.elements[0]]
        for x in self.elements[1:]:
            if x != out[-1]:
                out.append(x)
        return out

    def signature(self):
        return hash(tuple(self.elements))

    def monotonic_push(self, x):
        while not self.isEmpty() and self.showLast() > x:
            self.pop()
        self.elements.append(x)
        
    def compress_unique(self):
        seen = set()
        out = []
        for x in self.elements:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out
    
    def compress_inplace(self):
        if self.isEmpty():
            return
        out = [self.elements[0]]
        for x in self.elements[1:]:
            if x != out[-1]:
                out.append(x)
        self.elements = out
