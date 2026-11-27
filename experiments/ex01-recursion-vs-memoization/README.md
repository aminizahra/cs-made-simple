# EX01 · Same Function, Wildly Different Cost

**Experiment Wednesday #1** · [Post](POST_URL)

| | |
| --- | --- |
| **A vs B** | Naive recursive `fib(n)` vs the same function with `functools.lru_cache` |
| **Knob** | n, from 1 to 30 |
| **Metric** | How many times the function body runs |
| **Baseline** | The memoized version runs once per value: n + 1 times |

## Run it

```bash
python fib_calls.py

# fast version
QUICK=1 python fib_calls.py
```

The script saves `results/fib_calls.csv` and, if matplotlib is installed, `results/fib_calls.png` in the same dark style as the posts.

## Result (my run)

| n | naive | `lru_cache` |
| --- | --- | --- |
| 10 | 177 | 11 |
| 20 | 21,891 | 21 |
| 30 | **2,692,537** | **31** |

## 🎬 Recursion vs Memoization

<p align="center">
  <img src="experiments/ex01-recursion-vs-memoization/EX01-recursion-vs-memoization.gif"
       width="700"
       alt="Recursion vs Memoization Demo">
</p>

The naive version recomputes the same values again and again, so its work grows exponentially (roughly ×1.6 for every +1 in n). The memoized version computes each value once.

## Why it matters

This is dynamic programming in one line: **recursion + memory**. The same idea powers the DP posts later in the series (coin change, knapsack, LCS).
