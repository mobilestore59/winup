import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, state

@winup.component
def StateDemoApp():
    """A component demonstrating reactive state management in WinUp."""
    
    # 1. Create a state object
    username_state = state.create("username", "Guest")

    # 2. Create the UI widgets
    title = ui.Label("Type in the input field to see the reactive update.", props={"font-weight": "bold"})

    # This input will update the 'username' state key whenever its text changes.
    # For two-way binding, the legacy `bind_two_way` is still a good option.
    # However, to show the new API, we can use a one-way binding from input to state.
    name_input = ui.Input(text=username_state.get(), on_text_changed=lambda text: username_state.set(text))

    # This label will be bound to the state object.
    bound_label = ui.Label()

    # 3. Create the binding using the new API.
    # The formatter makes it easy to prepend text to the state value.
    username_state.bind_to(bound_label, "text", lambda name: f"Hello, {name}!")

    # 4. Arrange widgets in a layout
    return ui.Column(props={"spacing": 10, "margin": "20px"}, children=[
        title,
        ui.Row(props={"spacing": 5}, children=[ui.Label("Input:"), name_input]),
        ui.Row(props={"spacing": 5}, children=[ui.Label("Bound Label (updates automatically):"), bound_label])
    ])


if __name__ == "__main__":
    winup.run(
        main_component_path="tests.state_demo:StateDemoApp",
        title="Reactive State Management",
        width=700,
        height=300,
        dev=True
    ) 