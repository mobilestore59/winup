from winup import ui

def LiveComponent():
    """
    This is the component that will be reloaded live.
    Try changing the text or the colors and saving the file!
    """
    return ui.Column(
        children=[
            ui.Label("Hot Reload is Magic! ✨", props={"font-size": "20px", "font-weight": "bold"}),
            ui.Label("Hi niggas", props={"font-size": "20px", "font-weight": "bold"}),
            ui.Button("Button does nothing, but it reloads!", props={"margin-top": "10px"})
        ],
        props={"class": "live-frame", "spacing": 10}
    ) 
