from winup import component, ui, state

@component
def SettingsPage():
    """The page for application settings."""
    
    def toggle_theme():
        current_theme = state.get('theme', 'light')
        new_theme = 'dark' if current_theme == 'light' else 'light'
        state.set('theme', new_theme)

    theme_button = ui.Button("Toggle Dark/Light Mode", on_click=toggle_theme)

    # We can add more settings here in the future
    
    return ui.Column(
        children=[
            ui.Label("Appearance", props={"font-weight": "bold", "font-size": "18px"}),
            theme_button
        ],
        props={"class": "card"}
    ) 