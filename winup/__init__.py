from .core.window import _winup_app, Window
from .core.component import component
from .core.events import event_bus as events
from .core.hot_reload import hot_reload

from . import ui
from .style import styler as style
from .state import state
from .tools import wintools, profiler

# --- Main API ---

def run(main_component: callable, title="WinUp App", width=800, height=600, icon=None, dev=False):
    """
    The main entry point for a WinUp application.

    This function initializes the application, creates the main window,
    and starts the event loop. It should be called only once.

    Args:
        main_component: A function (ideally a @component) that returns the main widget.
        title, width, height, icon: Standard window properties.
        dev (bool): If True, enables development features like hot reloading.
    """
    # Create the main component widget first
    main_widget = main_component()

    # Create the main window and pass the component to it
    main_window = _winup_app.create_main_window(main_widget, title, width, height, icon)
    
    # Initialize all modules that require a window instance
    style.init_app(_winup_app.app)
    wintools.init_app(main_window)
    
    # Enable hot reloading if in dev mode
    if dev:
        import inspect
        file_to_watch = inspect.getfile(main_component)
        
        def on_reload():
            # This is a simple reload. It replaces the entire central widget.
            new_widget = main_component()
            main_window.setCentralWidget(new_widget)
        
        hot_reload(file_to_watch, on_reload)

    # Run the application event loop
    _winup_app.run()


__all__ = [
    "run", "Window", "hot_reload", "events", 
    "ui", "style", "state", "tools", "profiler",
    "component"
]
