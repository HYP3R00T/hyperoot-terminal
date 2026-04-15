from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, TabbedContent, TabPane

from rajeshdas.widgets import (
    LearnContent,
    PhilosophyContent,
    ProjectsContent,
    WelcomeSection,
)


class HomeScreen(Screen):
    """Main home screen for the portfolio."""

    BINDINGS = [
        ("1", "switch_tab('home')", "Home"),
        ("2", "switch_tab('projects')", "Projects"),
        ("3", "switch_tab('philosophy')", "Philosophy"),
        ("4", "switch_tab('learn')", "Learn"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent(id="tabs"):
            with TabPane("Home", id="home"):
                yield WelcomeSection(id="welcome")
            with TabPane("Projects", id="projects"):
                yield ProjectsContent(id="projects-tab")
            with TabPane("Philosophy", id="philosophy"):
                yield PhilosophyContent(id="philosophy-tab")
            with TabPane("Learn", id="learn"):
                yield LearnContent(id="learn-tab")

        yield Footer()

    def action_switch_tab(self, tab_id: str) -> None:
        """Switch to a specific tab."""
        tabs = self.query_one("#tabs", TabbedContent)
        tabs.active = tab_id
