from winup import component, ui, state, style

@component
def TaskItem(task: dict):
    """
    A component representing a single task item.
    It handles its own 'Done' action.
    """
    def on_complete():
        # Update the database
        state.get("db").mark_task_done(task['id'])
        # Update the state by removing this task from the list
        new_tasks = [t for t in state.get('tasks', []) if t['id'] != task['id']]
        state.set('tasks', new_tasks)
    
    task_label = ui.Label(task['text'])
    complete_button = ui.Button("Done", on_click=on_complete)
    
    task_item_row = ui.Row(children=[task_label, complete_button])
    style.add_style(task_item_row, "card")

    return task_item_row 