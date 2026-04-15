from textual.app import App
from textual.binding import Binding

from rajeshdas.screens import HomeScreen


class PortfolioApp(App):
    CSS_PATH = "app.tcss"

    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.theme = "catppuccin-mocha"

    def on_mount(self) -> None:
        self.push_screen(HomeScreen())

    def action_open_link(self, url: str) -> None:
        """Open a URL in the default browser."""
        import webbrowser

        webbrowser.open(url)


if __name__ == "__main__":
    app = PortfolioApp()
    app.run()
