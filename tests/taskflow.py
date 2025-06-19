import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Apply the critical patch for the state manager

import winup
from winup import ui, style, state, tasks
from tests.taskflow_app.database import init_db, get_tasks, add_task, delete_task, toggle_task_status
from tests.taskflow_app.components.navbar import Navbar
from tests.taskflow_app.pages.tasks_page import TasksPage
from tests.taskflow_app.pages.settings_page import SettingsPage
from tests.taskflow_app.themes import apply_base_theme

# --- 1. State and DB Initialization ---

init_db()
# Create the reactive state objects that will drive the application
state.create("tasks", get_tasks())
state.create("current_page", "tasks")

# --- 2. Main Application Component ---

@winup.component
def App():
    """The root component for the TaskFlow application."""
    apply_base_theme()
    
    # The page container needs a layout to be able to hold children.
    page_container = ui.Frame(props={"id": "page-container", "layout": "vertical"})

    def on_page_change(page):
        # This function is now much simpler.
        # It just swaps the component in the container.
        ui.clear_layout(page_container.layout())
        if page == 'tasks':
            page_container.add_child(TasksPage())
        elif page == 'settings':
            page_container.add_child(SettingsPage())

    state.subscribe("current_page", on_page_change)
    on_page_change(state.get("current_page")) # Initial page load

    return ui.Frame(
        props={"id": "main-window"},
        children=[
            Navbar(),
            page_container
        ]
    )

# --- 3. Run Application ---

if __name__ == "__main__":
    winup.run(
        main_component_path="tests.taskflow:App",
        title="TaskFlow - WinUp Demo",
        width=450,
        height=600,
        dev=True
    ) 