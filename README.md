[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/zrm4/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/zrm4/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# World News Front Page — 25 November 2026

A single-day world news front page for 25 November 2026, delivered as a deterministic 1024×1024 PNG. The page is built from fixed panels: a story ledger listing the day's items, a world map with numbered markers keyed to that ledger, a UTC timeline running across the day, a region bar summarizing coverage by area, a day-in-numbers panel, a two-way date-check band, and a LEFT OUT line for the stories that did not make the page. Rendering is fully reproducible — same inputs, same pixels.

## Run it

```shell
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` stages `entry.png` into the output directory (`out` here, `/output` by default). It is standard-library-only Python 3.13 — no dependencies, no build step.
