# FS01 · How to Calculate Big-O: 9 Rules

**Formula sheet #1** · [Post](POST_URL)

Nine rules that turn any piece of code into one clean formula.

| # | Rule | Example → result |
| --- | --- | --- |
| 1 | Drop the constants | `3n + 5` → O(n) |
| 2 | Biggest term wins | `n² + n + 100` → O(n²) |
| 3 | In a row? Add. | two separate loops → O(n + m) |
| 4 | Nested? Multiply. | loop inside a loop → O(n · m) |
| 5 | Halving = log n | `while n > 1: n //= 2` → O(log n) |
| 6 | Recursion tree | `T(n) = 2T(n/2) + n` → O(n log n) |
| 7 | Master theorem | binary search: a = 1, b = 2, d = 0 → O(log n) |
| 8 | Amortized cost | `list.append` → O(1) amortized |
| 9 | Space counts too | `xs[:]` → O(n) extra memory |

## Files

| File | What it is |
| --- | --- |
| [`slides/Formula-Sheet-01-BigO-Carousel.pdf`](slides/Formula-Sheet-01-BigO-Carousel.pdf) | 11-slide PDF carousel: the full sheet, one slide per rule, TL;DR |

## Try the rules yourself

The timings in [NL01](../../newsletter/nl01-big-o-in-practice/) show rules 3 and 4 in action: a nested loop gets about 4× slower every time n doubles.
