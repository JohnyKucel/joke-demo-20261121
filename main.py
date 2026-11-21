import os
from pathlib import Path

JOKE = "Our AI agent's live demo died on the first click, and the only thing it recovered was its confidence."

ENTRY_FILENAME = "entry.txt"
MAX_CHARS = 280


def output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    text = JOKE.strip()
    if not text or "\n" in text or len(text) > MAX_CHARS:
        raise ValueError("entry text must be one line of 1-280 characters")
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / ENTRY_FILENAME
    target.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
