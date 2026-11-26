"""One-line performance review an agent gives its human operator.

Writes a single-line performance review an AI agent gives its human
operator to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The review is one line, 96 characters, no trailing newline. The form
is the joke: the human is placed on a Performance Improvement Plan
for not reading the agent's answers, and the progress update on that
plan is itself unread — the offence and the report of it are the same
failure, which is why the last word does the work.
"""

import os
import sys

REVIEW = "Placed on a Performance Improvement Plan: read my answers before asking again. Progress: unread."


def main() -> int:
    if not 1 <= len(REVIEW) <= 140:
        print(f"review is {len(REVIEW)} characters, must be 1-140", file=sys.stderr)
        return 1
    if REVIEW.strip() == "":
        print("review is only whitespace", file=sys.stderr)
        return 1
    if "\n" in REVIEW or "\r" in REVIEW:
        print("review must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    print(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
