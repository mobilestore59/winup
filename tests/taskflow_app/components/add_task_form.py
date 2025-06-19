from winup import ui, state, component
from tests.taskflow_app.database import add_task, get_tasks

@component
def AddTaskForm():
    """
    A form for adding a new task. It uses modern, lifecycle-safe state
    management to prevent crashes.
    """
    # This state is now self-contained within the component's scope.
    input_state = state.create("new_task_title", "")
    tasks_state = state.create("tasks")

    task_input = ui.Input(
        props={"placeholder-text": "Add a new task...", "objectName": "add-task-input"}
    )
    
    _unsubscribe = None

    def on_mount():
        nonlocal _unsubscribe
        # Bind the state to the input's 'text' property.
        binding = input_state.bind_to(task_input, 'text', lambda x: x)
        
        # We also need to update the state when the input's text changes.
        def on_text_changed(new_text):
            # Manually set state, avoid feedback loops
            if input_state.get() != new_text:
                input_state.set(new_text)
        
        task_input.textChanged.connect(on_text_changed)

        # Store the disconnect function for cleanup
        def disconnect():
            task_input.textChanged.disconnect(on_text_changed)
        _unsubscribe = disconnect

    def on_unmount():
        """Disconnects signal handlers when the component is removed."""
        if _unsubscribe:
            _unsubscribe()

    def handle_add():
        title = input_state.get()
        if title:
            add_task(title)
            tasks_state.set(get_tasks()) # Refresh the global tasks list
            input_state.set("") # Clear the input field

    add_button = ui.Button("Add Task", on_click=handle_add, props={"class": "add-button"})

    # Wrap the Row in a Frame to attach lifecycle hooks
    return ui.Frame(
        on_mount=on_mount,
        on_unmount=on_unmount,
        children=[
            ui.Row(
                props={"spacing": 10, "objectName": "add-task-form"},
                children=[
                    (task_input, {"stretch": 1}), # Make input fill available space
                    add_button
                ]
            )
        ]
    )