import sys
import os

# Add the project root to the path to allow importing 'winup'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

# Import our custom component
from components.card import Card

winup.create_window("Component-Based UI", 700, 600)

# --- Style Definitions ---
# Define a dictionary of styles to be applied across the application
style_dict = {
    # General style for all buttons
    "QPushButton": {
        "font-size": "14px",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid #ccc"
    },
    # A reusable "class" style for primary action buttons
    "QPushButton[class~='primary']": {
        "background-color": "#007BFF",
        "color": "white",
        "font-weight": "bold",
        "border": "none"
    },
    # A specific style for a single button with an ID
    "#special-button": {
        "background-color": "#28a745",
        "border": "2px dashed #1e7e34"
    }
}
# Add the style dictionary to the application
winup.style.add_style_dict(style_dict)
# --- End Style Definitions ---


# --- Render Components ---

# Use the Card component to create different sections of the UI
info_card = Card(
    title="Information",
    children=[
        winup.ui.Label("This is a reusable card component."),
        winup.ui.Link("It can contain any other widget.", "https://google.com")
    ]
)

actions_card = Card(
    title="Actions",
    children=[
        winup.ui.Button("Click me!", on_click=lambda: print("Clicked!"))
    ]
)

# Add the component instances to the main layout
winup.add_widget(info_card)
winup.add_widget(actions_card)


winup.show()
