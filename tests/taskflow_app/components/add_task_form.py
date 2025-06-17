from winup import component, ui, state

@component
def AddTaskForm():
    """A form component for adding new tasks."""
    
    new_task_input = ui.Input(placeholder="What needs to be done?")
    
    def add_new_task():
        text = new_task_input.text()
        if not text:
            return
        
        # Add to DB and update state
        db = state.get("db")
        if db:
            new_task = db.add_task(text)
            current_tasks = state.get('tasks', [])
            state.set('tasks', current_tasks + [new_task])
        
        new_task_input.setText("")

    add_task_button = ui.Button(
        "Add Task", 
        on_click=add_new_task, 
        props={"class": "primary"}
    )
    
    return ui.Column(
        children=[
            ui.Label("New Task", props={"font-weight": "bold", "font-size": "18px"}),
            new_task_input,
            add_task_button
        ],
        props={"class": "card"}
    ) 