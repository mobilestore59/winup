import sys
import os
import random

# Add the project root to the path so we can import 'winup'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, state

# --- App Logic ---

def find_random_file():
    """Scans the entire project directory and returns a random file or folder path."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    all_paths = []
    for root, dirs, files in os.walk(project_root):
        for name in dirs:
            all_paths.append(os.path.join(root, name))
        for name in files:
            all_paths.append(os.path.join(root, name))
            
    if not all_paths:
        return "No files or folders found."
        
    return random.choice(all_paths)

# --- UI Setup ---

def RandomFileApp():
    """Main component for the Random File Finder application."""
    
    # Use state management for the result label to make it reactive
    state.set("random_path", "...")

    def update_random_file_label():
        """Finds a random file and updates the state."""
        random_path = find_random_file()
        state.set("random_path", random_path)

    # Create widgets
    title_label = ui.Label("Click the button to find a random file in your project:", props={"font-weight": "bold"})
    result_label = ui.Label() # Text will be bound from state
    find_button = ui.Button("Find a Random File!", on_click=update_random_file_label)
    
    # Bind the label's text property to our state key
    state.bind(result_label, "text", "random_path")

    # Arrange widgets in a layout
    return ui.Column(props={"spacing": 10, "margin": "20px"}, children=[
        title_label,
        result_label,
        find_button
    ])


if __name__ == "__main__":
    winup.run(
        main_component=RandomFileApp,
        title="Random File Finder",
        width=700,
        height=200
    )