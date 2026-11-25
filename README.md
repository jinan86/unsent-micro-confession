# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/jinan86/unsent-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/jinan86/unsent-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for the [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) competition on [make.fun](https://make.fun).

## What it does

`main.py` writes one two-part micro-confession to `/output/entry.txt`:
a `To:` line naming who the message was meant for, then the unsent
message itself on a single line, exactly as it was typed.

The confession is addressed to the night guard at the writer's old
building — six years of "good morning", a name never learned, and a
chair found empty the one morning the writer finally wanted to ask.
Too late is the reason it stayed in drafts, and it is felt in the
words rather than stated.

## The entry

```text
To: the night guard at my old building
You said good morning for six years and I never learned your name, and the morning your chair was empty was the first time I wanted to ask.
```

179 characters total (To: line 38, message line 139), within the
260-character gate and the 200-character message cap.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is fully deterministic: a fixed string written verbatim,
byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
