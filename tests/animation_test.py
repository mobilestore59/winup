import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, component
# Import the fx module directly since __init__.py creation failed
from winup.animate import fade_in, fade_out, animate

@component
def App():
    """Main application component for testing animations."""

    animated_label = ui.Label(
        "I will fade in and out!",
        props={
            "padding": "20px",
            "background-color": "#ADD8E6",
            "border-radius": "5px",
            "font-size": "16px",
        }
    )

    def handle_fade_out():
        print("Fading out...")
        fade_out(animated_label, duration=500, on_finish=lambda: print("Fade out finished."))

    def handle_fade_in():
        print("Fading in...")
        # The fade_in function automatically calls widget.show()
        fade_in(animated_label, duration=500, on_finish=lambda: print("Fade in finished."))

    return ui.Column(
        props={"spacing": 20, "margin": "20px", "alignment": "AlignCenter"},
        children=[
            animated_label,
            ui.Row(
                props={"spacing": 10},
                children=[
                    ui.Button("Fade Out", on_click=handle_fade_out),
                    ui.Button("Fade In", on_click=handle_fade_in),
                ]
            )
        ]
    )

# --- Run Application ---
if __name__ == "__main__":
    winup.run(
        main_component_path="tests.animation_test:App",
        title="Animation Test",
        dev=True
    ) 