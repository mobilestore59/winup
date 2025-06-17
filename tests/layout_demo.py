import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup

winup.create_window("Layout & Sizing Demo", 600, 400)

# --- Demo ---

# Create some widgets to work with
title = winup.ui.Label("Layout Demo", bold=True, font_size=18)
stretchy_button = winup.ui.Button("I stretch to fill space")
fixed_button = winup.ui.Button("I stay a fixed size")
another_label = winup.ui.Label("Some more text here.")

# Apply the fixed size utility to the button
# This button will now resist stretching horizontally, but can still stretch vertically.
winup.style.set_fixed_size(fixed_button, horizontal=True, vertical=False)


# Create a layout using the new native WinUp layout class
# This is a vertical layout, so widgets will stretch horizontally by default.
main_layout = winup.ui.QVBoxLayout()

# Add our widgets to the layout
main_layout.addWidget(title)
main_layout.addWidget(stretchy_button)
main_layout.addWidget(fixed_button)
main_layout.addWidget(another_label)

# To use a custom layout, we must place it inside a container like a Frame
container = winup.ui.Frame()
container.setLayout(main_layout)

# Add the main container to the window
winup.add_widget(container)


winup.show() 