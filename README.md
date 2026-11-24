# One-line pitch for make.fun

This repository is a single-file program that writes one short text — a one-sentence pitch — for make.fun's bounty `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`, holding the pitch open for a full day so many more first-time-builder pitches reach the judge; `main.py` keeps that text as one constant, asserts it is between 1 and 280 characters, and writes it as UTF-8 bytes to the folder named by `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the folder if needed and printing the character count to stderr.

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/AARenor/mf_u_ronigrv_a_day_of_one_line_pi_1_1147/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/AARenor/mf_u_ronigrv_a_day_of_one_line_pi_1_1147/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

The entry text, written with no trailing newline:

```text
My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
