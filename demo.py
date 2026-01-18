from MyCustomStack import CustomStack

def print_state(title, stack):
    print(f"\n--- {title} ---")
    print("Mode:", getattr(stack, "mode", "N/A"))
    print("Stack elements:", stack.elements)
    print("Size:", stack.size())

def main():
    print("\n==============================")
    print("   CustomStack DEMO (v2)")
    print("==============================\n")

    # ---------------------------
    # BASIC PUSH / POP
    # ---------------------------
    s = CustomStack()
    print("### BASIC PUSH / POP ###")
    for x in [1, 2, 3, 4, 5]:
        s.push(x)
    print_state("After push", s)

    print("pop():", s.pop())
    print_state("After pop", s)

    # ---------------------------
    # PEEK / PEEK_K
    # ---------------------------
    print("\n### PEEK / PEEK_K ###")
    print("peek():", s.peek())
    print("peek_k(3):", s.peek_k(3))
    print_state("After peek operations (unchanged)", s)

    # ---------------------------
    # ZIGZAG VIEW
    # ---------------------------
    print("\n### ZIGZAG VIEW (NON-DESTRUCTIVE) ###")
    print("zigzag_view(group=2):", s.zigzag_view(2))
    print("zigzag_view(group=3):", s.zigzag_view(3))
    print_state("After zigzag_view (unchanged)", s)

    # ---------------------------
    # WAVE VIEW
    # ---------------------------
    print("\n### WAVE VIEW (NON-DESTRUCTIVE) ###")
    print("wave_view(amplitude=2):", s.wave_view(2))
    print("wave_view(amplitude=3):", s.wave_view(3))
    print_state("After wave_view (unchanged)", s)

    # ---------------------------
    # CHECKPOINT / ROLLBACK
    # ---------------------------
    print("\n### CHECKPOINT / ROLLBACK ###")
    snap = s.checkpoint()
    print("Checkpoint saved:", snap)

    s.pop()
    s.pop()
    print_state("After popping twice", s)

    s.rollback(snap)
    print_state("After rollback", s)

    # ---------------------------
    # POP UNTIL
    # ---------------------------
    print("\n### POP UNTIL (DESTRUCTIVE) ###")
    print("pop_until(2):", s.pop_until(2))
    print_state("After pop_until", s)

    # ---------------------------
    # REVERSE (DESTRUCTIVE)
    # ---------------------------
    print("\n### REVERSE (DESTRUCTIVE) ###")
    s = CustomStack()
    for x in [1, 2, 3, 4]:
        s.push(x)
    print_state("Before reverse", s)
    print("reverse():", s.reverse())
    print_state("After reverse (stack consumed)", s)

    # ---------------------------
    # COMPRESS variants
    # ---------------------------
    print("\n### COMPRESS VARIANTS ###")
    s = CustomStack()
    for x in [1, 1, 2, 2, 2, 3, 3, 1]:
        s.push(x)
    print_state("Before compress", s)

    print("compress() (consecutive, view):", s.compress())
    print("compress_unique() (global unique, view):", s.compress_unique())
    print_state("After compress views (unchanged)", s)

    s.compress_inplace()
    print_state("After compress_inplace() (mutated)", s)

    # ---------------------------
    # SIGNATURE
    # ---------------------------
    print("\n### SIGNATURE ###")
    print("signature():", s.signature())

    # ---------------------------
    # MONOTONIC MODE
    # ---------------------------
    print("\n### MODE: monotonic_increasing ###")
    s = CustomStack(mode="monotonic_increasing")
    for x in [5, 3, 4, 2, 6, 1]:
        s.push(x)
        print(f"push({x}) ->", s.elements)
    print_state("Final monotonic stack", s)

    # ---------------------------
    # MATRIX (DESTRUCTIVE)
    # ---------------------------
    print("\n### MATRIX (CONSUMES STACK) ###")
    s = CustomStack()
    for x in [1, 2, 3, 4, 5, 6]:
        s.push(x)
    print_state("Before Matrix", s)

    matrix = s.Matrix(2, 3)
    print("Matrix(2,3):", matrix)
    print_state("After Matrix (stack consumed)", s)

    print("\nDemo completed.\n")

if __name__ == "__main__":
    main()
