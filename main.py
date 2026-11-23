#!/usr/bin/env python3
"""One-line pitch for a first-time builder (make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

Writes a single sentence to /output/entry.txt: a warm, concrete nudge
that gets a friend who has never coded to let an AI agent build their
first app idea on make.fun.
"""

import os
import stat

PITCH = (
    "You've told me about that app idea three times now \u2014 say it once "
    "more to an AI agent on make.fun, and tonight you'll be tapping a "
    "working first version of it; if you don't love it, you've lost "
    "nothing but the telling."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PITCH + "\n")
    # The grader collects /output as another user: files 0644, folders 0755.
    os.chmod(out_dir, 0o755)
    os.chmod(path, 0o644)
    # Sanity: the gate allows 1-240 characters, non-whitespace only.
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars"


if __name__ == "__main__":
    main()
