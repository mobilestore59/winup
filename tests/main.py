import sys
import os

# Add the project root to the path to allow importing 'winup'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui

# Import our custom component
from components.card import Card

def App():
    """The main application component that holds all other UI elements."""
    # Use the Card component to create different sections of the UI
    info_card = Card(
        title="Information",
        children=[
            ui.Label("This is a reusable card component."),
            ui.Link("It can contain any other widget.", "https://google.com", 1)
        ]
    )

    actions_card = Card(
        title="Actions",
        children=[
            ui.Button("Click me!", on_click=lambda: print("Clicked!"))
        ]
    )

    # Use a layout to organize the cards
    return ui.Column(
        props={"spacing": 15, "margin": "20px"},
        children=[
            info_card,
            actions_card
        ]
    )

if __name__ == "__main__":
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
    
    # Run the application using the modern syntax
    winup.run(
        main_component_path="main:App",
        title="Component-Based UI",
        width=700,
        height=600
    )
