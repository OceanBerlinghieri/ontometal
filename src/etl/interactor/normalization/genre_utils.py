import re


def clean_and_split_genres(genre_str: str) -> list[str]:
    """Clean a raw genre string and split into individual genre parts.
    Removes parentheses content, apostrophes, normalizes whitespace,
    splits on common delimiters and filters fragments <= 3 chars.
    """
    cleaned = re.sub(r"\(.*?\)|\'|'", "", str(genre_str))
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return [
        g.strip()
        for g in cleaned.replace(",", "/").replace(";", "/").replace(".", "/").split("/")
        if g.strip() and len(g.strip()) > 3
    ]
