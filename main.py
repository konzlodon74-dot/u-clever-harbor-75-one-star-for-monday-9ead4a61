#!/usr/bin/env python3
"""One-star review of Monday, written as if Monday were a restaurant.

Writes the review as a single line to <output dir>/entry.txt
with no trailing newline.
"""

import os

REVIEW = (
    "One star. The waiter Monday took 48 hours to bring the menu, "
    "then served my motivation cold and charged me a week for it."
)


def main() -> None:
    # The review must be one line, at most 25 words and 180 characters.
    assert "\n" not in REVIEW, "review must be a single line"
    assert len(REVIEW) <= 180, "review exceeds 180 characters"
    assert len(REVIEW.split()) <= 25, "review exceeds 25 words"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
