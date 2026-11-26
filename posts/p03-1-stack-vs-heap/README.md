# 3.1 · Where Do Your Variables Live? Stack vs Heap

**Carousel** · [English post](POST_URL_EN) · [Persian post](POST_URL_FA)

Your program's memory works like an office: a small, fast **desk** (the stack) and a big **warehouse** (the heap). A **pointer** is a sticky note with the shelf number, and the **garbage collector** is the cleaner who throws out boxes nobody points to.

## What's inside

| File | What it does |
| --- | --- |
| [`pointers_demo.py`](pointers_demo.py) | Stack frames, heap objects, `b = a` vs `a.copy()`, reference counting |
| [`slides/`](slides/) | The carousel as PDF, in English and Persian |

## Run it

```bash
python pointers_demo.py
```

## Key takeaways

- **Stack:** one frame per function call, cleared automatically when the call returns. Too deep and you get a stack overflow (Python stops at 1,000 frames by default).
- **Heap:** objects that are big, change size or must outlive a function. In Python, every object lives here; the stack holds only the names that point to them.
- **References:** `b = a` copies the reference, not the list. Use `a.copy()` for a real copy.
- **Garbage collection:** CPython counts references and frees an object when the count reaches zero, plus a cycle detector for objects that point to each other.

## Further reading

- [Python Tutor](https://pythontutor.com/): watch frames and references while your code runs.
- [Python docs: `gc` module](https://docs.python.org/3/library/gc.html)
