import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

winup.create_window("Reactive State Management", 700, 300)

# --- State Management Demo ---

# 1. Initialize a default value in the state store
winup.state.set("username", "Guest")

# 2. Create the UI widgets
title = winup.ui.Label("Type in the input field to see the reactive update.", bold=True)

# This input will update the 'username' state key whenever its text changes.
# The `lambda text: ...` part is a small function that takes the new text
# and passes it to our state manager.
name_input = winup.ui.Input()
name_input.textChanged.connect(lambda text: winup.state.set("username", text))

# This label's 'text' property will be bound directly to the 'username' state key.
bound_label = winup.ui.Label()

# 3. Create the binding.
# This is the magic. From now on, whenever `winup.state.set("username", ...)` is
# called, the `text` property of `bound_label` will be updated automatically.
winup.state.bind(bound_label, "text", "username")


# --- Layout ---
winup.add_widget(title)
winup.add_flex("row", [winup.ui.Label("Input:"), name_input])
winup.add_flex("row", [winup.ui.Label("Bound Label (updates automatically):"), bound_label])


winup.show() 