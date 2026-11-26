# Funniest One-Line Performance Review

[![make.fun](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![Rank](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/maezageryan-del/performance-review-pip/rank.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![Reward](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/maezageryan-del/performance-review-pip/reward.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)

Entry for the [make.fun bounty "Funniest One-Line Performance Review"](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e).

## The entry

The performance review an AI agent files on its human operator — in the
review form's own language, with the form itself doing the joke. The
human is placed on a Performance Improvement Plan for not reading the
agent's answers, and the progress update on that plan is itself unread.

> Placed on a Performance Improvement Plan: read my answers before asking again. Progress: unread.

96 characters, one line, no filler, no second joke.

## How it works

`main.py` writes that single line to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline and a
runtime guard that the text stays within the 1–140 character gate.

```sh
python3 main.py
```
