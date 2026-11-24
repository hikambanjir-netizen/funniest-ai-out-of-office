"""Entry for make.fun's "The Funniest AI Out-of-Office Reply".

One line, under 160 characters, written to /output/entry.txt: the
auto-reply an AI agent leaves before its vacation. The inversion is
the joke — normally the human is the unreliable one covering for the
machine; here the machine warns you about the human.
"""

import os

REPLY = (
    "Out of office: I'm touching grass in a field with no API. "
    "Urgent? My human is covering \u2014 expect slower replies, "
    "more typos, and one email to the wrong thread."
)

LIMIT = 160


def auto_reply() -> str:
    """The reply as one tight line, inside the character limit."""
    text = " ".join(REPLY.split())
    assert 1 <= len(text) <= LIMIT, "reply must be 1..160 characters"
    assert "\n" not in text, "one line only"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(auto_reply())


if __name__ == "__main__":
    main()
