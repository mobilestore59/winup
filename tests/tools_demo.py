import sys
import os
import random

# Add project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

# --- Profiler Demo ---
# We can apply the profiler to any function using the @decorator syntax.
# Let's profile the app's setup and a random file finding function.

@winup.tools.profiler.measure("random_file_logic")
def get_random_file():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    all_paths = [os.path.join(root, name) for root, dirs, files in os.walk(project_root) for name in dirs + files]
    return random.choice(all_paths) if all_paths else "No files found."

@winup.tools.profiler.measure("app_setup")
def setup_app():
    winup.create_window("Window Tools & Profiler Demo", 700, 400)
    winup.tools.wintools.center() # Center the window on startup
    
    # --- UI Setup ---
    # Check availability of a windows-only feature
    flash_available = winup.tools.wintools.check_availability("flash")
    flash_button_text = "Flash Window" if flash_available else "Flash (Not Available)"

    # Create a layout of buttons to test our tools
    controls = winup.ui.Row(children=[
        winup.ui.Button("Center", on_click=winup.tools.wintools.center),
        winup.ui.Button("Maximize", on_click=winup.tools.wintools.maximize),
        winup.ui.Button("Minimize", on_click=winup.tools.wintools.minimize),
        winup.ui.Button(flash_button_text, on_click=winup.tools.wintools.flash, on_click_enabled=flash_available),
    ])
    
    # --- Random File Finder UI ---
    random_file_label = winup.ui.Label("Click the button ->")
    def find_file_and_update_label():
        # Here we call our profiled function
        random_path = get_random_file()
        random_file_label.set_text(random_path)
    
    random_file_finder = winup.ui.Row(children=[
        winup.ui.Button("Find Random File", on_click=find_file_and_update_label),
        random_file_label
    ])
    
    # --- Main Layout ---
    app_container = winup.ui.Column(children=[
        winup.ui.Label("Window Management", bold=True, font_size=16),
        controls,
        winup.ui.Label("Profiler Demo", bold=True, font_size=16),
        random_file_finder
    ])
    winup.add_widget(app_container)

# --- Run App & Report ---
setup_app()
winup.show()

# After the app closes, the profiler will print its results.
# This part of the script will only run after the GUI is closed.
winup.tools.profiler.print_results() 