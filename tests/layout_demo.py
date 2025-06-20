import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, style

@winup.component
def LayoutDemoApp():
    """A component demonstrating layout and sizing in WinUp."""

    # Create widgets
    title = ui.Label("Layout Demo", props={"font-size": "24px", "font-weight": "bold"})
    stretchy_button = ui.Button("I stretch to fill space")
    fixed_button = ui.Button("I stay a fixed size", props={"max-width": "150px"})
    another_label = ui.Label("Some more text here.")

    # Use a Column layout. By default, items will stretch to the container's width.
    # The button with a 'max-width' will be constrained.
    return ui.Column(props={"spacing": 10, "margin": "20px"}, children=[
        title,
        stretchy_button,
        fixed_button,
        another_label
    ])

if __name__ == "__main__":
    winup.run(
        main_component_path="layout_demo:LayoutDemoApp",
        title="Layout & Sizing Demo",
        width=600,
        height=400,
        dev=True
    )