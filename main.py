"""Real-life patch note: the doorway effect, as a release note.

The entry is a single changelog line for a bug in human biology: walk
through a doorway and the reason you walked in evaporates. It is written
in the terse register of a real release note — a version number, a fix
verb, and the failure described as if it shipped — and dropped into
/output/entry.txt, where the judge reads it.
"""

from pathlib import Path

# The patch note in two fragments, joined at write time by assemble().
# The joke is the doorway effect — crossing a threshold flushes working
# memory — told with the dry vocabulary of a cache bug: flushed, dropped,
# no log. One line, 126 characters.
VERSION_AND_FIX = "v2.4.1: fixed a bug where crossing a doorway "
BUG_DESCRIPTION = (
    "flushed the working-memory cache and dropped the pending task "
    "without logging it."
)


def assemble() -> str:
    """Join the two note fragments into the single-line patch note."""
    return VERSION_AND_FIX + BUG_DESCRIPTION


OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def validate(line: str) -> str:
    """Check the line against the gate; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate(assemble())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
