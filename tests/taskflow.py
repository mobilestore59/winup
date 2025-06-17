import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui
from taskflow_app.themes import light_theme, dark_theme
from taskflow_app.database import TaskDatabase
from taskflow_app.components.navbar import Navbar
from taskflow_app.pages.tasks_page import TasksPage
from taskflow_app.pages.settings_page import SettingsPage

@winup.component
def App():
    """The main component for the TaskFlow application."""
    
    # --- Database and State Initialization ---
    db = TaskDatabase()
    winup.state.set('db', db)
    winup.state.set('theme', 'light')
    winup.state.set('current_page', 'tasks')
    winup.state.set('tasks', db.load_tasks())

    # --- Page Container (Deck) ---
    # The Deck widget shows only one child at a time.
    page_container = ui.Deck()
    tasks_page = TasksPage()
    settings_page = SettingsPage()
    page_container.addWidget(tasks_page)
    page_container.addWidget(settings_page)

    # --- Reactive Logic ---

    def switch_theme(theme_name):
        """Applies the selected theme dictionary to the app."""
        theme_dict = dark_theme if theme_name == 'dark' else light_theme
        winup.style.add_style_dict(theme_dict)

    def switch_page(page_name):
        """Switches the visible page in the Deck."""
        if page_name == 'tasks':
            page_container.setCurrentWidget(tasks_page)
        elif page_name == 'settings':
            page_container.setCurrentWidget(settings_page)

    # Subscribe our functions to state changes
    winup.state.subscribe('theme', switch_theme)
    winup.state.subscribe('current_page', switch_page)

    # Initialize the default theme and page
    switch_theme(winup.state.get('theme'))
    switch_page(winup.state.get('current_page'))

    # The root component is a Column containing the Navbar and the page container
    return ui.Column(
        children=[
            Navbar(),
            page_container
        ]
    )

# --- Run App ---
if __name__ == "__main__":
    winup.run(
        main_component=App, 
        title="TaskFlow - A WinUp Showcase", 
        width=800, 
        height=600
    ) 