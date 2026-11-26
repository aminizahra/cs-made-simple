# CS Made Simple

Code, experiments and slides behind my LinkedIn posts and the **Under the Hood** newsletter.
Computer science and AI explained simply, with real code and real measurements.

> Posts are published in Persian and English. Everything in this repo (code, comments, docs) is in English.

**Follow:** [LinkedIn](LINKEDIN_PROFILE_URL) · [Under the Hood newsletter](NEWSLETTER_URL)

---

## What's inside

| Folder | What it holds |
| --- | --- |
| [`posts/`](posts/) | Code and slides for regular posts (carousels, infographics, stories) |
| [`newsletter/`](newsletter/) | Full, runnable code for every issue of *Under the Hood* |
| [`experiments/`](experiments/) | *Experiment Wednesday*: A vs B, same budget, one knob, one metric |
| [`formula-sheets/`](formula-sheets/) | 9-card formula sheets (image + PDF carousel) |
| [`underrated/`](underrated/) | *Underrated algorithms*: lesser-known ideas, each with a small experiment |
| [`templates/`](templates/) | README template for new items |
| [`assets/`](assets/) | Shared plot style and brand colors |

## Index

| ID | Title | Format | Topic | Post | Code |
| --- | --- | --- | --- | --- | --- |
| 2.3 | Time Complexity on One Page | Infographic | Big-O | [post](POST_URL) | — |
| FS01 | How to Calculate Big-O: 9 Rules | Formula sheet | Big-O | [post](POST_URL) | [fs01](formula-sheets/fs01-big-o-rules/) |
| NL01 | Big-O in Practice: Why Was My Correct Code Slow? | Newsletter | Big-O | [article](ARTICLE_URL) | [nl01](newsletter/nl01-big-o-in-practice/) |
| 3.1 | Where Do Your Variables Live? Stack vs Heap | Carousel | Memory | [post](POST_URL) | [p03-1](posts/p03-1-stack-vs-heap/) |
| EX01 | Same Function, Wildly Different Cost | Experiment | Recursion | coming soon | [ex01](experiments/ex01-recursion-vs-memoization/) |

New items are added here as they are published. The full plan lives in my content calendar.

## Quick start

```bash
git clone https://github.com/YOUR_USERNAME/cs-made-simple.git
cd cs-made-simple

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python newsletter/nl01-big-o-in-practice/list_vs_set.py
```

Every script runs on its own: you can copy a single file and run it without the rest of the repo.

## How the experiments are measured

All numbers in posts come from the scripts in this repo, measured the same way:

- **Fixed seed** (`random.seed(42)`) so the data is the same on every run.
- **Best of several runs** with `timeit.repeat`, reporting the minimum (the run least disturbed by the rest of the system).
- **Results saved** as CSV in each item's `results/` folder, so charts are drawn from data, not memory.
- **Environment printed** at the top of every run (Python version, OS, CPU).

Absolute times depend on your machine. **Ratios** between methods should stay close to what the posts show. If yours don't, open an issue: I'd love to see it.

Set `QUICK=1` to run any experiment with small inputs in a few seconds (this is what CI does):

```bash
QUICK=1 python experiments/ex01-recursion-vs-memoization/fib_calls.py
```

## Naming convention

Each item lives in its own folder named `<id>-<slug>`:

| Prefix | Series | Example |
| --- | --- | --- |
| `pWW-N` | Regular post (week WW, post N) | `p03-1-stack-vs-heap` |
| `nlNN` | Newsletter issue | `nl01-big-o-in-practice` |
| `exNN` | Experiment Wednesday | `ex01-recursion-vs-memoization` |
| `fsNN` | Formula sheet | `fs01-big-o-rules` |
| `uNN` | Underrated algorithm | `u01-bloom-filter` |

Inside each folder:

```
<id>-<slug>/
├── README.md        # what it is, how to run it, results, link to the post
├── *.py             # standalone, runnable scripts
├── results/         # CSV output and charts (generated)
└── slides/          # PDF carousel or images used in the post (optional)
```

## Found a mistake?

Please [open an issue](../../issues). Corrections are credited in the next post or issue.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

- **Code** is released under the [MIT License](LICENSE).
- **Slides, images and written content** are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): share and adapt freely, with credit to Zahra Amini.
