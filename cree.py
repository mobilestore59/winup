import winup
from winup import ui

def App():
    # The initial text can be the current state value.
    label = ui.Label(f"Counter: {winup.state.get('counter', 0)}") 

    # Subscribe the label to changes in the 'counter' state
    def update_label(new_value):
        label.set_text(f"Counter: {new_value}")

    winup.state.subscribe("counter", update_label)

    def increment():
        # Get the current value, increment it, and set it back
        current_counter = winup.state.get("counter", 0)
        winup.state.set("counter", current_counter + 1)

    return ui.Column([
        label,
        ui.Button("Increment", on_click=increment)
    ])

if __name__ == "__main__":
    # Initialize the state before running the app
    winup.state.set("counter", 0)
    winup.run(main_component=App, title="My App", width=300, height=150) 