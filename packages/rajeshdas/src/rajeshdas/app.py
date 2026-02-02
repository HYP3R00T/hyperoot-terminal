from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static


class PortfolioApp(App):
    CSS_PATH = "app.tcss"

    def __init__(self):
        super().__init__()
        self.theme = "catppuccin-mocha"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, World!")
        yield Footer()


if __name__ == "__main__":
    app = PortfolioApp()
    app.run()
