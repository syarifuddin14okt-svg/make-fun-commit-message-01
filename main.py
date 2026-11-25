"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one commit-message line to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "fix: removed the login page so nobody can fail to log in anymore"

MAX_CHARS = 100


def validate(text: str) -> None:
    """Enforce the kit gate: UTF-8 text of 1-100 chars, not only whitespace,
    single line (no newline). Raises ValueError on any violation."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
