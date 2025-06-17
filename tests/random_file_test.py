import sys
import os
import random

# Add the project root to the path so we can import 'winup'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

# --- App Logic ---

def find_random_file():
    """Scans the entire project directory and returns a random file or folder path."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    all_paths = []
    for root, dirs, files in os.walk(project_root):
        # Add all directories and files to our list
        for name in dirs:
            all_paths.append(os.path.join(root, name))
        for name in files:
            all_paths.append(os.path.join(root, name))
            
    if not all_paths:
        return "No files or folders found."
        
    # Select and return a random path
    return random.choice(all_paths)

# --- UI Setup ---

winup.create_window("Random File Finder", 700, 200)

# Create the widgets we'll need
title_label = winup.ui.Label("Click the button to find a random file in your project:", bold=True)
result_label = winup.ui.Label("...")
find_button = winup.ui.Button("Find a Random File!")

# Define what happens when the button is clicked
def update_random_file_label():
    random_path = find_random_file()
    result_label.setText(random_path)

# Assign the function to the button's on_click handler
find_button.on_click = update_random_file_label

# --- Layout ---

# Use a Column to arrange the widgets vertically
app_layout = winup.ui.Column(
    children=[
        title_label,
        result_label,
        find_button
    ]
)

winup.add_widget(app_layout)
winup.show() 