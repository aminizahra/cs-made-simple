# Contributing

Thanks for reading the code behind the posts.

## Found a mistake?

Open an issue with:

1. The item ID (for example `NL01` or `EX01`).
2. What looks wrong: a number, a claim, or the code.
3. If it's about timings: your Python version, OS and the output of the script.

Corrections are credited in the next post or newsletter issue.

## Got different numbers?

That's expected for absolute times. If the **ratio** between methods is very different from the post, please share your output in an issue. Results from different machines make the experiments better.

## Pull requests

Small fixes (typos, clearer comments, bug fixes) are welcome.
Please keep every script standalone (no imports from other folders) and run:

```bash
ruff check .
QUICK=1 python path/to/script.py
```
