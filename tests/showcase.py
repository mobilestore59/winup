import sys
import os
import random

# Add project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

# --- App Setup & Styling ---
winup.create_window("WinUp Feature Showcase", 800, 600)

# Add validation styles to the default styler
winup.style.add_style_dict({
    "QLineEdit.valid": {"border": "2px solid #28a745"},
    "QLineEdit.invalid": {"border": "2px solid #dc3545"}
})

# --- Part 1: Random File Finder (Bug Fix & Refactor) ---
winup.state.set('random_path', 'Click the button!')

def find_and_set_random_file():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    all_paths = [os.path.join(root, name) for root, dirs, files in os.walk(project_root) for name in dirs + files]
    winup.state.set('random_path', random.choice(all_paths) if all_paths else "No files found.")

random_path_label = winup.ui.Label()
winup.state.bind(random_path_label, 'text', 'random_path') # One-way bind the label

random_file_finder = winup.ui.Column(children=[
    winup.ui.Label("Random File Finder", bold=True, font_size=16),
    random_path_label,
    winup.ui.Button("Find Random File", on_click=find_and_set_random_file)
])


# --- Part 2: Two-Way Binding & Validation Showcase ---
winup.state.set('email_value', 'not-an-email')
winup.state.set('name_value', 'John Doe')

# This input uses our new two-way binding. No more .connect() needed!
email_input = winup.ui.Input(placeholder="Enter your email", validation="email")
winup.state.bind_two_way(email_input, 'email_value')

# This label is one-way bound to the same state key. It will update automatically.
email_mirror_label = winup.ui.Label()
winup.state.bind(email_mirror_label, 'text', 'email_value')

# This input shows a custom validation rule (must be longer than 10 chars)
name_input = winup.ui.Input(placeholder="Name (must be > 10 chars)", validation=lambda text: len(text) > 10)
winup.state.bind_two_way(name_input, 'name_value')

# This label uses the new pythonic `set_text` method.
name_mirror_label = winup.ui.Label()
winup.state.subscribe('name_value', name_mirror_label.set_text)


form = winup.ui.Column(children=[
    winup.ui.Label("Two-Way Binding & Validation", bold=True, font_size=16),
    winup.ui.Label("Email:"),
    email_input,
    winup.ui.Label("Email state (live):"),
    email_mirror_label,
    winup.ui.Label("Name:"),
    name_input,
    winup.ui.Label("Name state (live):"),
    name_mirror_label
])


# --- Final Layout ---
app_container = winup.ui.Column(children=[random_file_finder, form])
winup.add_widget(app_container)
winup.show() 