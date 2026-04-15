from pathlib import Path

from textual.widgets import Markdown


CONTENT_DIR = Path(__file__).parent.parent / "content"


class PhilosophyContent(Markdown):
    """Philosophy tab loading from markdown."""

    def __init__(self, *args, **kwargs):
        content = self._load_content()
        super().__init__(content, *args, **kwargs)

    def _load_content(self) -> str:
        """Load markdown content from file."""
        content_path = CONTENT_DIR / "philosophy.md"
        if content_path.exists():
            return content_path.read_text()
        return "# Philosophy"
