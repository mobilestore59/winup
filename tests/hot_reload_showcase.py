import sys
import os
import importlib

# Ensure the 'winup' package is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui

# We need to manually import the module we want to hot-reload
import live_component

@winup.component
def App():
    
    # --- State for the reloaded component ---
    # We use a simple container to hold the component
    component_container = ui.Frame(props={"padding": 0})
    # We must set a layout on the frame for add/remove to work
    component_container.set_layout(ui.VBox(props={"padding": 0, "margin": 0}))

    def reload_component():
        """
        This function is the core of the hot-reload logic.
        It re-imports the module and replaces the widget in our container.
        """
        try:
            # 1. Reload the entire module
            importlib.reload(live_component)
            
            # This is where we fix the styler warning. By calling this *after*
            # the app is running and during a reload, we ensure the styler is ready.
            live_component.define_styles()

            # 2. Get the new component constructor
            NewComponent = live_component.LiveComponent
            
            # 3. Clear the container
            # We get the layout we set on the frame and remove its widget
            layout = component_container.layout()
            if layout.count() > 0:
                old_widget = layout.takeAt(0).widget()
                if old_widget is not None:
                    old_widget.deleteLater()
            
            # 4. Add the new instance
            layout.addWidget(NewComponent())
            print("Hot Reload: UI updated successfully.")

        except Exception as e:
            print(f"Error during hot reload: {e}")
            import traceback
            traceback.print_exc()

    # Set up the hot reloader to watch the 'live_component.py' file
    file_to_watch = os.path.abspath(live_component.__file__)
    winup.hot_reload(file_to_watch, reload_component)
    
    # Initial load of the component
    reload_component()

    return ui.Column(
        children=[
            ui.Label("Hot Reload Showcase", props={"font-size": "24px", "font-weight": "bold"}),
            ui.Label("➡️ Edit and save 'tests/live_component.py' to see the magic!"),
            component_container
        ],
        props={"alignment": "AlignTop", "spacing": 15, "margin": "20px"}
    )

if __name__ == "__main__":
    # We use the new `run` function. The `dev` flag is no longer needed here
    # as we are setting up the hot_reload manually for more control.
    winup.run(main_component=App, title="Hot Reload Showcase", width=600, height=400)