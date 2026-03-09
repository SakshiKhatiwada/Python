from textual.app import App
from textual.widgets import Header, Footer, Static

class MyApp(App):

    CSS = """
    Screen {
        align: center middle;
    }

    Static {
        background: blue;
        color: white;
        padding: 2;
    }
    """

    def compose(self):
        yield Header()
        yield Static("Hello, Textual!")
        yield Footer()

if __name__ == "__main__":
    MyApp().run()