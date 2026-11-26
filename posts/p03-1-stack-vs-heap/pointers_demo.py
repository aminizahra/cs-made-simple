"""Post 3.1 · Where do your variables live? Stack vs Heap.

Small demos for the carousel: frames on the stack, objects on the heap,
references (the "sticky notes") and reference counting.
Run: python pointers_demo.py
"""

import sys


def area(w, h):
    result = w * h  # lives in area's frame on the call stack
    return result  # the frame is removed when the function returns


def make_list():
    nums = [1, 2, 3]  # the list object lives on the heap
    return nums  # it survives after the function returns


def main() -> None:
    # 1. Stack frames
    print("area(3, 4) =", area(3, 4))
    print("default recursion limit:", sys.getrecursionlimit(), "frames")

    # 2. The heap: objects outlive the function that created them
    data = make_list()
    print("make_list() returned:", data)

    # 3. References: b = a copies the sticky note, not the box
    a = [1, 2, 3]
    b = a
    b.append(4)
    print("a after b.append(4):", a, "| same object?", a is b)

    c = a.copy()  # a real copy: a new box on the heap
    c.append(5)
    print("a after c.append(5):", a, "| same object?", a is c)

    # 4. Reference counting (CPython): when no names point to an object, it is freed.
    # Note: sys.getrefcount() counts its own argument too, so the number is one higher.
    box = [1, 2, 3]
    print("refcount with one name:", sys.getrefcount(box))
    other = box
    print("refcount with two names:", sys.getrefcount(box))
    del other
    print("refcount after del:", sys.getrefcount(box))


if __name__ == "__main__":
    main()
