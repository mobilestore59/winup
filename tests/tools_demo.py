import sys
import os
import random

# Add project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, tools

# --- Profiler Demo ---
# We can apply the profiler to any function using the @decorator syntax.
# Let's profile the app's setup and a random file finding function.

@tools.profiler.measure("random_file_logic")
def get_random_file():
    """Finds a random file in the project directory, with profiling."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    all_paths = [os.path.join(root, name) for root, dirs, files in os.walk(project_root) for name in dirs + files]
    return random.choice(all_paths) if all_paths else "No files found."

# --- Main Application Component ---
def ToolsDemoApp():
    """Main component for the tools demonstration application."""
    
    # Check availability of a windows-only feature
    flash_available = tools.wintools.check_availability("flash")
    flash_button_text = "Flash Window" if flash_available else "Flash (Not Available)"

    # Create a layout of buttons to test our window tools
    window_controls = ui.Row(props={"spacing": 10}, children=[
        ui.Button("Center", on_click=tools.wintools.center),
        ui.Button("Maximize", on_click=tools.wintools.maximize),
        ui.Button("Minimize", on_click=tools.wintools.minimize),
        ui.Button(flash_button_text, on_click=tools.wintools.flash, on_click_enabled=flash_available),
    ])
    
    # --- Random File Finder UI ---
    random_file_label = ui.Label("Click the button ->")
    def find_file_and_update_label():
        random_path = get_random_file()
        random_file_label.set_text(random_path)
    
    random_file_finder = ui.Row(props={"spacing": 10}, children=[
        ui.Button("Find Random File", on_click=find_file_and_update_label),
        random_file_label
    ])
    
    # --- Final Layout ---
    return ui.Column(props={"spacing": 15, "margin": "20px"}, children=[
        ui.Label("Window Management", props={"font-size": "16px", "font-weight": "bold"}),
        window_controls,
        ui.Label("Profiler Demo", props={"font-size": "16px", "font-weight": "bold"}),
        random_file_finder
    ])

# --- Run App & Report ---
if __name__ == "__main__":
    winup.run(
        main_component=ToolsDemoApp,
        title="Window Tools & Profiler Demo",
        width=700,
        height=400
    )
    
    # After the app closes, the profiler will print its results.
    tools.profiler.print_results() 