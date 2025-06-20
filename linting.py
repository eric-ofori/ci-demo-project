"""Random quote generator."""

import random


def get_random_quote():
    """Return a randomly selected motivational quote."""
    quotes = [
        "Believe you can and you're halfway there.",
        "Don’t watch the clock; do what it does. Keep going.",
        "The future depends on what you do today.",
        "Dream big and dare to fail.",
        "Act as if what you do makes a difference. It does."
    ]
    return random.choice(quotes)


print(get_random_quote())
