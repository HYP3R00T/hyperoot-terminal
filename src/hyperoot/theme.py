"""Theme definition for the Hyperoot terminal app.

This module keeps the UI theme separate from application logic so it can be
reused and tested independently.
"""

from textual.theme import Theme

# Publicly exported theme object used by the app
theme: Theme = Theme(
    name="custom",
    primary="#88C0D0",
    secondary="#81A1C1",
    accent="#B48EAD",
    foreground="#D8DEE9",
    background="#2E3440",
    success="#A3BE8C",
    warning="#EBCB8B",
    error="#BF616A",
    surface="#3B4252",
    panel="#434C5E",
    dark=True,
    variables={
        "block-cursor-text-style": "none",
        "footer-key-foreground": "#88C0D0",
        "input-selection-background": "#81a1c1 35%",
    },
)

__all__: list[str] = ["theme"]
