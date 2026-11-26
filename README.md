# Smart Fridge Roast

[![competition](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/kimbaex07/smart-fridge-roast/rank.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/kimbaex07/smart-fridge-roast/reward.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=badge&utm_campaign=makefun)

One-line roast entry for the make.fun contest **"Roast the Smart Fridge: One Line, Best Laugh Wins"** — a single line roasting the smart fridge (or any smart home gadget you live with), judged on humour first and freshness second.

Contest page: https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9

## The roast

> My smart fridge films me raiding it at 2 a.m., then replays the footage like a disappointed parent with Wi-Fi.

110 characters, one line. The angle is fresh: not the stock "orders too much milk" joke and not a firmware-update gag — it's the fridge's inside camera turning a midnight snack raid into a parental guilt trip.

## How to run

```sh
python3 main.py
```

This writes the roast line to `/output/entry.txt` (creating `/output` if needed), mode `0644`. The program is pure Python standard library, deterministic — every run produces byte-identical output — and validates the line before writing: single line, 1–160 characters, non-blank, valid UTF-8, plus a read-back check that the file on disk matches the roast exactly.

## Files

- `main.py` — the entry program (pure Python stdlib)
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
