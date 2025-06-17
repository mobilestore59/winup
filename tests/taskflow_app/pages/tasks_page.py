from winup import component, ui

@component
def TasksPage():
    """
    The main page for displaying and managing tasks.
    """
    # Imports are here to avoid circular dependencies if they grow complex
    from ..components.add_task_form import AddTaskForm
    from ..components.task_list import TaskList
    
    # Each major section of the page is its own component or styled frame
    add_task_card = AddTaskForm()
    
    tasks_list_card = ui.Column(
        children=[
            ui.Label("To-Do", props={"font-weight": "bold", "font-size": "18px"}),
            TaskList()
        ],
        props={"class": "card"}
    )

    return ui.Column(children=[add_task_card, tasks_list_card], props={"spacing": 20}) 