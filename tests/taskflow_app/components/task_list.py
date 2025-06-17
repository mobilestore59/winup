from winup import component, ui, state
from .task_item import TaskItem

@component
def TaskList():
    """A component that efficiently renders the list of tasks."""
    
    tasks_container = ui.Column()
    
    # A dictionary to keep track of the widgets associated with each task ID
    task_widgets = {}

    def render_tasks(tasks: list):
        current_ids = {task['id'] for task in tasks}
        rendered_ids = set(task_widgets.keys())
        
        # Remove tasks that are no longer in the state
        for task_id in rendered_ids - current_ids:
            widget = task_widgets.pop(task_id)
            widget.deleteLater()
            
        # Add new tasks that are not yet rendered
        for task in tasks:
            if task['id'] not in rendered_ids:
                widget = TaskItem(task=task)
                tasks_container.layout().addWidget(widget)
                task_widgets[task['id']] = widget

    state.subscribe('tasks', render_tasks)
    
    return tasks_container 