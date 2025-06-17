# WinUp 🚀

**A ridiculously Pythonic and powerful framework for building beautiful desktop applications.**

WinUp is a modern UI framework for Python that wraps the power of PySide6 (Qt) in a simple, declarative, and developer-friendly API. It's designed to let you build applications faster, write cleaner code, and enjoy the development process.

---

## Why WinUp? (Instead of raw PySide6 or Tkinter)

Desktop development in Python can feel clunky. WinUp was built to fix that.

| Feature                 | WinUp Way ✨                                                                   | Raw PySide6 / Tkinter Way 😟                                                                |
| ----------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Layouts**             | `ui.Column(children=[...])`, `ui.Row(children=[...])`                          | `QVBoxLayout()`, `QHBoxLayout()`, `layout.addWidget()`, `pack()`, `grid()`                  |
| **Styling**             | `props={"background-color": "blue", "font-size": "16px"}`                      | Manual QSS strings, `widget.setStyleSheet(...)`, complex style objects.                     |
| **State Management**    | `state.bind(widget, "prop", "key")`                                            | Manual callback functions, getters/setters, `StringVar()`, boilerplate everywhere.          |
| **Two-Way Binding**     | `state.bind_two_way(input_widget, "key")`                                      | Non-existent. Requires manual `on_change` handlers to update state and UI.                  |
| **Developer Tools**     | **Built-in Hot Reloading**, code profiler, and window tools out of the box.    | Non-existent. Restart the entire app for every single UI change.                            |
| **Code Structure**      | Reusable, self-contained components with `@component`.                         | Often leads to large, monolithic classes or procedural scripts.                             |

**In short, WinUp provides the "killer features" of modern web frameworks (like React or Vue) for the desktop, saving you time and letting you focus on what matters: your application's logic.**

---

## Core Features

*   **Declarative & Pythonic UI:** Build complex layouts with simple `Row` and `Column` objects instead of clunky box layouts.
*   **Component-Based Architecture:** Use the `@component` decorator to create modular and reusable UI widgets from simple functions.
*   **Powerful Styling System:** Style your widgets with simple Python dictionaries using `props`. Create global "CSS-like" classes with `style.add_style_dict`.
*   **Reactive State Management:**
    *   **One-Way Binding:** Automatically update your UI when your data changes with `state.bind()`.
    *   **Two-Way Binding:** Effortlessly sync input widgets with your state using `state.bind_two_way()`.
    *   **Subscriptions:** Trigger any function in response to state changes with `state.subscribe()`.
*   **Developer-Friendly Tooling:**
    *   **Hot Reloading:** See your UI changes instantly without restarting your app.
    *   **Profiler:** Easily measure the performance of any function with the `@profiler.measure()` decorator.
    *   **Window Tools:** Center, flash, or manage your application window with ease.
*   **Flexible Data Layer:** Includes simple, consistent connectors for SQLite, PostgreSQL, MySQL, MongoDB, and Firebase.

---

## Installation

```bash
pip install winup watchdog
```
*The `watchdog` library is required for the Hot Reloading feature.*

---

## Getting Started: Hello, WinUp!

Creating an application is as simple as defining a main component and running it.

```python
# hello_world.py
import winup
from winup import ui

# The @component decorator is optional for the main component, but good practice.
@winup.component
def App():
    """This is our main application component."""
    return ui.Column(
        props={
            "alignment": "AlignCenter", 
            "spacing": 20
        },
        children=[
            ui.Label("👋 Hello, WinUp!", props={"font-size": "24px"}),
            ui.Button("Click Me!", on_click=lambda: print("Button clicked!"))
        ]
    )

if __name__ == "__main__":
    winup.run(main_component=App, title="My First WinUp App")
```

---

## Core Concepts

### UI & Layouts

WinUp abstracts away Qt's manual layout system. You build UIs by composing `Row` and `Column` components.

```python
def App():
    return ui.Column(  # Arranges children vertically
        children=[
            ui.Label("Top"),
            ui.Row(    # Arranges children horizontally
                children=[
                    ui.Button("Left"),
                    ui.Button("Right")
                ],
                props={"spacing": 10}
            ),
            ui.Label("Bottom")
        ],
        props={"spacing": 15, "margin": "20px"}
    )
```

### Styling

You can style any widget by passing a `props` dictionary. Props can be CSS-like properties, or special keywords like `class` and `id` for use with a global stylesheet.

```python
# Define global styles
winup.style.add_style_dict({
    ".btn-primary": {
        "background-color": "#007bff",
        "color": "white",
        "border-radius": "5px",
        "padding": "10px"
    },
    ".btn-primary:hover": {
        "background-color": "#0056b3"
    }
})

# Use the class in a component
def App():
    return ui.Button("Primary Button", props={"class": "btn-primary"})
```

### State Management

WinUp's global `state` object is the single source of truth for your application's data.

**1. One-Way Binding (`bind`)**

The UI property updates automatically when `state.set()` is called.

```python
# one_way_demo.py
import winup
from winup import ui

winup.state.set("counter", 0)

def App():
    # The label's 'text' property will be kept in sync with the 'counter' state key.
    label = ui.Label(f"Initial Value: {winup.state.get('counter')}")
    winup.state.bind(label, "text", "counter")

    def increment():
        winup.state.set("counter", winup.state.get("counter") + 1)

    return ui.Column(children=[
        label,
        ui.Button("Increment", on_click=increment)
    ])
```

**2. Two-Way Binding (`bind_two_way`)**

The UI updates the state, and the state updates the UI. This is perfect for forms.

```python
# two_way_demo.py
import winup
from winup import ui

winup.state.set("username", "Guest")

def App():
    # This input is two-way bound to 'username'. Typing in the field
    # immediately updates the state.
    name_input = ui.Input()
    winup.state.bind_two_way(name_input, "username")
    
    # This label is one-way bound and will update as you type.
    greeting = ui.Label()
    winup.state.bind(greeting, "text", "username")

    return ui.Column(children=[ui.Label("Enter your name:"), name_input, greeting])
```

**3. Subscriptions (`subscribe`)**

For more complex reactions to state changes, like formatting data or triggering other logic, use `subscribe`.

```python
# subscribe_demo.py
import winup
from winup import ui

winup.state.set("username", "Guest")

def App():
    greeting = ui.Label()

    # This function runs every time the 'username' state changes.
    def update_greeting(new_name):
        greeting.set_text(f"Hello, {new_name.upper()}!")
    
    winup.state.subscribe("username", update_greeting)
    
    # We still need a way to change the state.
    name_input = ui.Input()
    winup.state.bind_two_way(name_input, "username")

    return ui.Column(children=[name_input, greeting])
```

### Developer Tools

**Hot Reloading:**
To enable hot reloading, you manually start a watcher that calls a reload function. This gives you precise control over what gets reloaded.

```python
# hot_reload_example.py
import winup
from winup import ui
from winup.core import hot_reload

# 1. Define your component(s) in a separate file (e.g., components.py)
#
# --- components.py ---
# from winup import ui
# def MyComponent():
#     return ui.Label("Version 1 of my component")
# ---------------------

# 2. In your main app file, create a placeholder and a reload function
app_container = ui.Frame() # A container to hold the component

def reload_ui():
    """This function clears the container and re-imports the component."""
    hot_reload.clear_layout(app_container.layout())
    # The reloader invalidates Python's import cache
    from components import MyComponent 
    app_container.add_child(MyComponent())
    print("UI Reloaded!")

if __name__ == "__main__":
    # 3. Start the hot reloader before running the app
    # It will watch 'components.py' and call 'reload_ui' when it changes.
    reloader = hot_reload.FileChangeReloader('components.py', reload_ui)
    reloader.start()

    # 4. Run the app with the container, and load the initial UI
    reload_ui() # Initial load
    winup.run(main_component=lambda: app_container, title="Hot Reload App")
```
*This setup allows you to see UI changes instantly just by saving your component file.*

**Profiler:**
Simply add the `@profiler.measure()` decorator to any function to measure its execution time. Results are printed to the console when the application closes.

```python
from winup.tools import profiler

@profiler.measure
def some_expensive_function():
    # ... code to measure ...
    import time
    time.sleep(1)
```

---

## Contributing

WinUp is an open-source project. Contributions are welcome!

## License

This project is licensed under the Apache 2.0 License. 