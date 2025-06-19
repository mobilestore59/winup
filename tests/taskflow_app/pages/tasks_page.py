from winup import ui, component
from tests.taskflow_app.components.task_list import TaskList
from tests.taskflow_app.components.add_task_form import AddTaskForm

# --- Main Page Component ---

@component
def TasksPage():
    """
    The main page for displaying and managing tasks.
    It's now a simple layout component, as the children manage their own state.
    """
    
    return ui.Column(
        props={"spacing": 15, "class": "page", "objectName": "tasks-page"},
        children=[
            ui.Label("My Tasks", props={"class": "h1"}),
            AddTaskForm(),
            TaskList(),
        ]
    ) 