# tests/custom_widget_test.py
import winup
from winup import ui, style
import sys
import os

# 1. Define styles for our custom components
style.add_style_dict({
    ".btn-primary": {
        "background-color": "$primary-color",
        "color": "$primary-text-color",
        "border": "none",
        "font-weight": "bold",
    },
    ".btn-primary:hover": { "background-color": "$hover-color" },
    ".label-alert": {
        "background-color": "$error-color",
        "color": "$primary-text-color",
        "border-radius": "4px",
        "font-size": "14px",
    },
})

# 2. Create reusable component variants using ui.create_component
PrimaryButton = ui.create_component(
    ui.Button, 
    {"class": "btn-primary", "padding": "10px", "border-radius": "5px"}
)

AlertLabel = ui.create_component(
    ui.Label,
    {"class": "label-alert", "padding": "15px"}
)


# 3. Use the new components just like any other ui element
@winup.component
def CustomWidgetDemo():
    
    def on_click():
        print("Primary button clicked!")

    return ui.Column(
        props={"spacing": 20, "margin": 15},
        children=[
            ui.Label("This demonstrates creating reusable, styled components."),
            
            # Use our new PrimaryButton
            PrimaryButton("Click Me", on_click=on_click),
            
            # Use it again, but override one of its default props
            PrimaryButton(
                "I have different padding!", 
                props={"padding": "20px"},
                on_click=on_click
            ),

            # Use our new AlertLabel
            AlertLabel("This is an important alert!"),
        ]
    )


if __name__ == "__main__":
    # Add the project root to the path for hot reloading to work
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    winup.run(
        main_component_path="tests.custom_widget_test:CustomWidgetDemo",
        title="Custom Components Demo",
        dev=True
    ) 