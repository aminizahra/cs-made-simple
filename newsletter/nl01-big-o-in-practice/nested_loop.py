"""NL01 · Experiment 2: four ways to find the emails two lists have in common.

v1  explicit nested loop          O(n·m)
v2  `a in B` on a list (hidden)   O(n·m)
v3  build set(B), then look up    O(n + m)
v4  set(A) & set(B)               O(n + m), returns a set (no order)

Run:            python nested_loop.py
Fast check:     QUICK=1 python nested_loop.py
"""

import csv
import os
import platform
import random
import timeit
from pathlib import Path

QUICK = os.getenv("QUICK") == "1"
SIZES = (200, 500) if QUICK else (1_000, 5_000, 10_000, 20_000)
OUT = Path(__file__).parent / "results" / ("nested_loop.quick.csv" if QUICK else "nested_loop.csv")


def make_lists(n: int) -> tuple[list[str], list[str]]:
    """Two lists of n emails each, drawn from 2n possible addresses (about half overlap)."""
    a = [f"user{i}@mail.com" for i in random.sample(range(2 * n), n)]
    b = [f"user{i}@mail.com" for i in random.sample(range(2 * n), n)]
    return a, b


def common_v1(A, B):
    out = []
    for a in A:
        for b in B:
            if a == b:
                out.append(a)
                break
    return out


def common_v2(A, B):
    return [a for a in A if a in B]  # `in` on a list is a loop


def common_v3(A, B):
    B_set = set(B)  # O(m), once
    return [a for a in A if a in B_set]  # O(1) each


def common_v4(A, B):
    return set(A) & set(B)


def best_ms(fn, A, B, number: int) -> float:
    return min(timeit.repeat(lambda: fn(A, B), number=number, repeat=3)) / number * 1000


def main() -> None:
    print(f"Python {platform.python_version()} · {platform.system()} · {platform.processor() or platform.machine()}")
    random.seed(42)
    rows = []
    print(f"{'n':>8} {'common':>8} {'v1 ms':>10} {'v2 ms':>10} {'v3 ms':>8} {'v4 ms':>8}")
    for n in SIZES:
        A, B = make_lists(n)
        assert len(common_v1(A, B)) == len(common_v3(A, B)) == len(common_v4(A, B))
        r = [best_ms(common_v1, A, B, 1), best_ms(common_v2, A, B, 1),
             best_ms(common_v3, A, B, 20), best_ms(common_v4, A, B, 20)]
        rows.append([n, len(common_v3(A, B)), *[f"{x:.2f}" for x in r]])
        print(f"{n:>8,} {rows[-1][1]:>8,} {r[0]:>10.2f} {r[1]:>10.2f} {r[2]:>8.2f} {r[3]:>8.2f}")

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "common", "v1_nested_ms", "v2_hidden_in_ms", "v3_set_lookup_ms", "v4_set_and_ms"])
        w.writerows(rows)
    print(f"saved {OUT}")


if __name__ == "__main__":
    main()
