"""NL01 · Experiment 1: membership test in a list vs a set.

1,000 lookups (half present, half absent) in a collection of 1,000,000 integers.
Run:            python list_vs_set.py
Fast check:     QUICK=1 python list_vs_set.py
"""

import csv
import os
import platform
import random
import sys
import timeit
from pathlib import Path

QUICK = os.getenv("QUICK") == "1"
N = 10_000 if QUICK else 1_000_000
LOOKUPS = 100 if QUICK else 1_000
OUT = Path(__file__).parent / "results" / ("list_vs_set.quick.csv" if QUICK else "list_vs_set.csv")


def main() -> None:
    print(f"Python {platform.python_version()} · {platform.system()} · {platform.processor() or platform.machine()}")
    random.seed(42)

    data_list = list(range(N))
    data_set = set(data_list)

    half = LOOKUPS // 2
    queries = random.sample(range(N), half) + list(range(N, N + half))  # present + absent
    random.shuffle(queries)

    def search_list():
        return sum(1 for q in queries if q in data_list)

    def search_set():
        return sum(1 for q in queries if q in data_set)

    t_list = min(timeit.repeat(search_list, number=1, repeat=3))
    t_set = min(timeit.repeat(search_set, number=100, repeat=5)) / 100
    t_build = min(timeit.repeat(lambda: set(data_list), number=1, repeat=5))

    per_list = t_list / LOOKUPS
    per_set = t_set / LOOKUPS
    break_even = t_build / (per_list - per_set)

    print(f"{LOOKUPS:,} lookups in {N:,} items")
    print(f"list : {t_list:.4f} s   ({per_list * 1e6:,.1f} µs per lookup)")
    print(f"set  : {t_set * 1e3:.4f} ms  ({per_set * 1e9:,.0f} ns per lookup)")
    print(f"speedup: {t_list / t_set:,.0f}x")
    print(f"building the set: {t_build * 1e3:.1f} ms, pays off after ~{break_even:.0f} lookups")
    print(f"container size: list {sys.getsizeof(data_list) / 1e6:.1f} MB, set {sys.getsizeof(data_set) / 1e6:.1f} MB")

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "lookups", "list_s", "set_s", "build_set_s", "speedup"])
        w.writerow([N, LOOKUPS, f"{t_list:.6f}", f"{t_set:.9f}", f"{t_build:.6f}", f"{t_list / t_set:.0f}"])
    print(f"saved {OUT}")


if __name__ == "__main__":
    main()
