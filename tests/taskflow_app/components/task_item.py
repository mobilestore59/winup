from winup import ui, state, component
from tests.taskflow_app.database import delete_task, toggle_task_status, get_tasks

@component
def TaskItem(task):
    """
    A single task item component.
    It manages its own state for deletion and completion toggle.
    """
    tasks_state = state.create("tasks")

    def handle_delete():
        delete_task(task.id)
        tasks_state.set(get_tasks())

    def handle_toggle(is_checked):
        toggle_task_status(task.id, is_checked)
        tasks_state.set(get_tasks())

    # Use a dynamic class for styling based on status
    item_class = "task-item-completed" if task.completed else "task-item"
    
    return ui.Row(
        props={"class": item_class, "objectName": f"task-item-{task.id}", "spacing": 10},
        children=[
            ui.Switch(
                checked=task.completed,
                on_toggle=handle_toggle
            ),
            # Add stretch to the label to make it fill available space
            (ui.Label(task.title, props={"class": "task-title"}), {"stretch": 1}),
            ui.Button(
                "Delete",
                on_click=handle_delete,
                props={"class": "delete-btn"}
            ),
        ]
    ) 