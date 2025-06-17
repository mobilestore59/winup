import winup
from winup import ui
# We need to import the default button to subclass it.
from winup.ui.widgets.button import Button as DefaultButton

# 1. Create a custom widget class.
# This button has a unique, hardcoded style to make it visually distinct.
class CustomButton(DefaultButton):
    def __init__(self, text: str, on_click: callable = None, **kwargs):
        # Define a custom style that will identify our button
        custom_props = {
            "background-color": "#FFC107", # Amber
            "color": "black",
            "font-size": "14px",
            "font-weight": "bold",
            "border-radius": "8px",
            "pgadding": "10px 15px",
        }
        
        # We'll allow users to override our custom style with their own props
        if 'props' in kwargs:
            custom_props.update(kwargs.pop('props'))
        
        super().__init__(text=text, on_click=on_click, props=custom_props, **kwargs)

# 2. Define the component for the secondary window.
def SecondaryComponent():
    """The UI for our pop-up window."""
    return ui.Column(
        props={"alignment": "AlignCenter", "spacing": 15, "margin": "10px"},
        children=[
            ui.Label("This is a secondary window!"),
            # This button will ALSO be a CustomButton because the widget was registered globally.
            ui.Button("Another Custom Button") 
        ]
    )

# 3. Define the function that creates and shows the secondary window.
def open_secondary_window():
    """This function is called when the main button is clicked."""
    print("Event triggered: Opening secondary window...")
    # Use the new winup.Window class to create a new, independent window.
    # This doesn't block the main window.
    winup.Window(
        component=SecondaryComponent(),
        title="Side Window",
        width=350,
        height=200
    )

# 4. Define the main application component.
def MainApp():
    """The UI for the primary window."""
    return ui.Column(
        props={"alignment": "AlignCenter", "spacing": 20, "margin": "20px"},
        children=[
            ui.Label("Widget Extensibility & Multi-Window Test", props={"font-size": "16px"}),
            # Because we registered our custom widget, this will create a CustomButton.
            ui.Button("Open Secondary Window", on_click=open_secondary_window)
        ]
    )

if __name__ == "__main__":
    # Before running the app, we register our custom class to override the default "Button".
    # From this point on, any call to ui.Button() will create an instance of CustomButton.
    print("Registering `CustomButton` to override the default `Button`.")
    ui.register_widget("Button", CustomButton)
    
    # Run the main application as usual.
    winup.run(
        main_component=MainApp,
        title="Advanced Features Test"
    ) 