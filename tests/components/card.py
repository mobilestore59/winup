from winup import component, ui

@component
def Card(title: str, children: list = []):
    """
    A simple card component with a title and a container for child widgets.
    This version uses only pure WinUp APIs.
    """
    # Create the title label
    title_label = ui.Label(text=title, bold=True, font_size=16)

    # The list of all widgets to be placed in the card
    all_children = [title_label] + children

    # The Frame widget handles its own layout and children
    return ui.Frame(
        color="#f8f9fa",
        radius=8,
        direction="column",
        children=all_children
    ) 