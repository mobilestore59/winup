from winup import component, ui, state, style

@component
def Navbar():
    """The main navigation bar for the application."""
    
    tasks_button = ui.Button("Tasks", on_click=lambda: state.set('current_page', 'tasks'))
    settings_button = ui.Button("Settings", on_click=lambda: state.set('current_page', 'settings'))

    def set_active_button(page):
        style.toggle_class(tasks_button, 'active', page == 'tasks')
        style.toggle_class(settings_button, 'active', page == 'settings')

    state.subscribe('current_page', set_active_button)
    
    navbar = ui.Row(children=[tasks_button, settings_button])
    style.set_id(navbar, "navbar")
    
    return navbar 