from winup import ui, style

def define_styles():
    style.add_style_dict({
        "live_frame": {
            "background-color": "#eef2f9",
            "border": "2px solid #d0d7e5",
            "border-radius": "10px",
            "padding": "15px"
        }
    })

def LiveComponent():
    """
    This is the component that will be reloaded live.
    Try changing the text or the colors and saving the file!
    """
    # We call this here to ensure styles are applied for the initial load
    define_styles()
    
    return ui.Column(
        children=[
            ui.Label("Hot Reload is Active! 🔥", props={"font-size": "16px", "font-weight": "bold"}),
            ui.Label("This component is now safe from TypeError."),
            ui.Label("Try changing this text and save the file.")
        ],
        props={"class": "live_frame", "spacing": 10}
    ) 
