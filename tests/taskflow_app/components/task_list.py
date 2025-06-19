from winup import ui, state, component
from .task_item import TaskItem

@component
def TaskList():
    """
    A component that displays a list of tasks and updates automatically
    when the global 'tasks' state changes. It correctly manages its
    state subscription using on_mount and on_unmount hooks.
    """
    tasks_state = state.create("tasks")
    list_container = ui.Column(props={"spacing": 5, "objectName": "task-list-container"})
    
    # This will hold the function to unsubscribe from the state
    _unsubscribe = None

    def render_tasks(tasks):
        """Clears and re-renders the list of task items."""
        try:
            # This is the safest way to check if the widget is still alive.
            # Accessing any Qt property will raise a RuntimeError if the C++
            # part of the object has been deleted.
            if not list_container.layout():
                # If there's no layout, we can't add children.
                # This can happen if the component is created but not yet fully set up.
                return
        except RuntimeError:
            # The widget has been destroyed, so we should do nothing.
            return

        ui.clear_layout(list_container.layout())
        if not tasks:
            list_container.add_child(ui.Label("No tasks yet. Add one!", props={"class": "empty-list-label"}))
        else:
            for task in tasks:
                list_container.add_child(TaskItem(task=task))

    def on_mount():
        """Subscribe to state changes when the component is added to the UI."""
        nonlocal _unsubscribe
        _unsubscribe = tasks_state.subscribe(render_tasks)
        render_tasks(tasks_state.get())

    def on_unmount():
        """Unsubscribe from state changes when the component is removed."""
        if _unsubscribe:
            _unsubscribe()

    # The Frame now acts as the component's root and holds the lifecycle hooks.
    return ui.Frame(
        children=[list_container],
        on_mount=on_mount,
        on_unmount=on_unmount
    ) 