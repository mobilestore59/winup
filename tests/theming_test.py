# tests/theming_test.py
import winup
from winup import ui, style

# 1. Define a global stylesheet using theme variables
# 'style' is now the style module.
style.add_style_dict({
    "QFrame#main-container": {
        "background-color": "$background-color",
        "border": "2px solid $border-color",
        "border-radius": "8px",
    },
    "QLabel": {
        "color": "$text-color",
        "font-size": "16px",
    },
    "QPushButton#themed-button": {
        "background-color": "$primary-color",
        "color": "$primary-text-color",
        "padding": "10px",
        "border-radius": "5px",
        "border": "none",
    },
    "QPushButton#themed-button:hover": {
        "background-color": "$hover-color",
        "color": "$secondary-text-color",
    }
})

@winup.component
def ThemedApp():
    """A component demonstrating the new theming system."""
    
    def toggle_theme():
        # Access the theme manager via the 'themes' attribute on the style module
        current_theme = style.themes.get_active_theme_name()
        next_theme = "dark" if current_theme == "light" else "light"
        style.themes.set_theme(next_theme)

    return ui.Frame(
        props={"id": "main-container", "padding": "20px"},
        children=[
            ui.Column(
                props={"spacing": 20},
                children=[
                    ui.Label("This is a themable application!"),
                    ui.Label("Click the button to change the theme at runtime."),
                    ui.Button(
                        "Toggle Theme", 
                        props={"id": "themed-button", "font-weight": "bold"},
                        on_click=toggle_theme
                    ),
                    ui.Input(
                        props={
                            "placeholder-text": "Themed Input...",
                            "background-color": "$secondary-color",
                            "color": "$secondary-text-color",
                            "border": "1px solid $border-color",
                            "padding": "8px",
                            "border-radius": "4px",
                        }
                    )
                ]
            )
        ]
    )

if __name__ == "__main__":
    # Add the project root to the path for hot reloading to work
    import sys
    import os
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    winup.run(
        main_component_path="tests.theming_test:ThemedApp",
        title="Theming System Demo",
        dev=True
    ) 