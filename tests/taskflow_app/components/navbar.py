from winup import ui, state, style, component

@component
def Navbar():
    """The main navigation bar for the application."""
    page_state = state.create("current_page") # Get the existing state object

    def navigate(page):
        page_state.set(page)

    tasks_button = ui.Button("Tasks", on_click=lambda: navigate('tasks'))
    settings_button = ui.Button("Settings", on_click=lambda: navigate('settings'))
    
    # The new, reactive way: Bind the 'class' property to the state.
    # The class will be 'active' or '' automatically.
    page_state.bind_to(tasks_button, 'class', lambda page: 'active' if page == 'tasks' else '')
    page_state.bind_to(settings_button, 'class', lambda page: 'active' if page == 'settings' else '')

    return ui.Frame(
        props={"id": "navbar", "class": "header"},
        children=[
            ui.Label("TaskFlow", props={"class": "brand"}),
            ui.Row(
                props={"spacing": 10, "alignment": "AlignRight"},
                children=[
                    tasks_button,
                    settings_button,
                ]
            )
        ]
    ) 