import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, state

def StateDemoApp():
    """A component demonstrating reactive state management in WinUp."""
    
    # 1. Initialize a default value in the state store
    state.set("username", "Guest")

    # 2. Create the UI widgets
    title = ui.Label("Type in the input field to see the reactive update.", props={"font-weight": "bold"})

    # This input will update the 'username' state key whenever its text changes.
    name_input = ui.Input(on_text_changed=lambda text: state.set("username", text))

    # This label's 'text' property will be bound directly to the 'username' state key.
    bound_label = ui.Label()

    # 3. Create the binding.
    # From now on, whenever `state.set("username", ...)` is called, the `text`
    # property of `bound_label` will be updated automatically.
    state.bind(bound_label, "text", "username")

    # 4. Arrange widgets in a layout
    return ui.Column(props={"spacing": 10, "margin": "20px"}, children=[
        title,
        ui.Row(props={"spacing": 5}, children=[ui.Label("Input:"), name_input]),
        ui.Row(props={"spacing": 5}, children=[ui.Label("Bound Label (updates automatically):"), bound_label])
    ])


if __name__ == "__main__":
    winup.run(
        main_component=StateDemoApp,
        title="Reactive State Management",
        width=700,
        height=300
    ) 