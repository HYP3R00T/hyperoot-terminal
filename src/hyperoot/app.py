from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer

from hyperoot.theme import theme


class Portfolio(App):
    BINDINGS: list[Binding] = [
        Binding(key="q", action="quit", description="Quit"),
    ]
    TITLE = "Rajesh Das"

    def __init__(self) -> None:
        super().__init__()
        self.register_theme(theme)
        self.theme = "custom"

    def compose(self) -> ComposeResult:
        yield Footer(compact=True)


def main() -> None:
    """Run the hyperoot application."""
    app = Portfolio()
    app.run()


if __name__ == "__main__":
    main()
