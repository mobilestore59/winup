from winup import ui, style, component

@component
def SettingsPage():
    """The page for application settings, like theme switching."""

    def set_theme(theme_name):
        style.themes.set_theme(theme_name)

    return ui.Column(
        props={"spacing": 15, "class": "page"},
        children=[
            ui.Label("Settings", props={"class": "h1"}),
            ui.Label("Theme"),
            ui.Row(
                props={"spacing": 10},
                children=[
                    ui.Button(
                        "Light Mode", 
                        on_click=lambda: set_theme("light")
                    ),
                    ui.Button(
                        "Dark Mode", 
                        on_click=lambda: set_theme("dark")
                    ),
                ]
            ),
        ]
    ) 