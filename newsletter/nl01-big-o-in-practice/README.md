# NL01 · Big-O in Practice: Why Was My Correct Code Slow?

**Under the Hood, issue #1** · [Read the article](ARTICLE_URL)

Correct code can still be slow. Two experiments show where the slowness hides and how a one-line change makes code thousands of times faster.

## What's inside

| File | What it does |
| --- | --- |
| [`list_vs_set.py`](list_vs_set.py) | 1,000 lookups in 1,000,000 items: `list` vs `set` |
| [`nested_loop.py`](nested_loop.py) | Common emails in two lists: nested loop vs hidden loop vs two set-based versions |
| [`results/`](results/) | CSV output from my run |

## Run it

```bash
python list_vs_set.py
python nested_loop.py

# fast version with small inputs
QUICK=1 python nested_loop.py
```

No dependencies beyond the Python standard library.

## Results (my run)

Python 3.13, `random.seed(42)`, best of several runs with `timeit.repeat`.

**Experiment 1: 1,000 lookups in 1,000,000 items**

| | Time | Per lookup |
| --- | --- | --- |
| `list` | 4.07 s | ~4 ms |
| `set` | 0.037 ms | ~37 ns |
| Speedup | **~110,000×** | |

Building the set took 28 ms and paid off after about 7 lookups. The set container is about 34 MB vs 8 MB for the list (`sys.getsizeof`, elements not included).

**Experiment 2: common emails in two lists of n emails (ms)**

| n | v1 nested loop | v2 `in` on list | v3 `set(B)` + `in` | v4 `set & set` |
| --- | --- | --- | --- | --- |
| 1,000 | 15.5 | 6.2 | 0.04 | 0.05 |
| 5,000 | 402 | 134 | 0.38 | 0.67 |
| 10,000 | 1,626 | 891 | 0.73 | 1.19 |
| 20,000 | 6,082 | 2,887 | 2.33 | 3.30 |

When n doubles, the nested loop takes about 4× longer: that's O(n²). The hidden loop in v2 is about 2× faster than v1 (the `in` operator runs in C) but grows the same way.

## Key takeaways

- `x in list` is a hidden loop; `x in set` is close to free.
- To remove a nested loop, build a fast lookup (set or dict) once, then query it.
- Measure before and after. Without numbers, optimization is a guess.

## Exercises

1. Rewrite an O(n²) `has_duplicates` function in O(n).
2. Two Sum: does any pair add up to `target`? Do it in one pass.

Solutions are at the end of the article.
