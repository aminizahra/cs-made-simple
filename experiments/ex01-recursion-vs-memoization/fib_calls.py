"""EX01 · Same function, wildly different cost: naive recursion vs memoization.

Counts how many times the function body runs for fib(n), with and without
functools.lru_cache, and saves a CSV plus a chart.
Run:            python fib_calls.py
Fast check:     QUICK=1 python fib_calls.py
"""

import csv
import os
import platform
import timeit
from functools import lru_cache
from pathlib import Path

QUICK = os.getenv("QUICK") == "1"
N_MAX = 20 if QUICK else 30
HERE = Path(__file__).parent
SUFFIX = ".quick" if QUICK else ""
OUT_CSV = HERE / "results" / f"fib_calls{SUFFIX}.csv"
OUT_PNG = HERE / "results" / f"fib_calls{SUFFIX}.png"
STYLE = HERE.parents[1] / "assets" / "brand.mplstyle"

calls = 0


def fib_naive(n: int) -> int:
    global calls
    calls += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    global calls
    calls += 1  # counts real executions; cache hits never reach this line
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def count(fn, n: int) -> int:
    global calls
    calls = 0
    if fn is fib_memo:
        fib_memo.cache_clear()
    fn(n)
    return calls


def main() -> None:
    print(f"Python {platform.python_version()} · {platform.system()} · {platform.processor() or platform.machine()}")
    rows = []
    for n in range(1, N_MAX + 1):
        naive, memo = count(fib_naive, n), count(fib_memo, n)
        rows.append((n, naive, memo))

    t_naive = min(timeit.repeat(lambda: fib_naive(N_MAX), number=1, repeat=3))

    def run_memo():
        fib_memo.cache_clear()
        fib_memo(N_MAX)

    t_memo = min(timeit.repeat(run_memo, number=100, repeat=5)) / 100

    n, naive, memo = rows[-1]
    print(f"fib({n}): naive runs the body {naive:,} times, memoized {memo:,} times")
    print(f"time: naive {t_naive * 1e3:.1f} ms, memoized {t_memo * 1e6:.1f} µs")

    OUT_CSV.parent.mkdir(exist_ok=True)
    with OUT_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "naive_calls", "memo_calls"])
        w.writerows(rows)
    print(f"saved {OUT_CSV}")

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed: skipping the chart")
        return

    if STYLE.exists():
        plt.style.use(STYLE)
    ns = [r[0] for r in rows]
    fig, ax = plt.subplots()
    ax.plot(ns, [r[1] for r in rows], marker="o", label="naive recursion")
    ax.plot(ns, [r[2] for r in rows], marker="o", label="lru_cache")
    ax.set_yscale("log")
    ax.set_xlabel("n")
    ax.set_ylabel("times the function body runs (log scale)")
    ax.set_title(f"fib(n): {naive:,} runs vs {memo}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_PNG)
    print(f"saved {OUT_PNG}")


if __name__ == "__main__":
    main()
