"""
Centralized factory and registry for all UI widgets in WinUp.
This allows developers to override default widgets with their own custom implementations.
"""

from PySide6.QtWidgets import QWidget
from functools import partial
from winup.style.styler import merge_props

# Default widget implementations
from .widgets.button import Button as DefaultButton
from .widgets.calendar import Calendar as DefaultCalendar
from .widgets.deck import Deck as DefaultDeck
from .widgets.frame import Frame as DefaultFrame
from .widgets.image import Image as DefaultImage
from .widgets.input import Input as DefaultInput
from .widgets.label import Label as DefaultLabel
from .widgets.link import Link as DefaultLink
from .widgets.progress_bar import ProgressBar as DefaultProgressBar
from .widgets.slider import Slider as DefaultSlider
from .widgets.textarea import Textarea as DefaultTextarea
from .layouts import Column as DefaultColumn, Row as DefaultRow, Stack as DefaultStack, Grid as DefaultGrid
from .widgets.combobox import ComboBox as DefaultComboBox
from .widgets.switch import Switch as DefaultSwitch
from .widgets.tabview import TabView as DefaultTabView
from .widgets.scroll_view import ScrollView as DefaultScrollView

# The central registry for widget classes
_WIDGET_REGISTRY = {
    "Button": DefaultButton,
    "Calendar": DefaultCalendar,
    "Deck": DefaultDeck,
    "Frame": DefaultFrame,
    "Image": DefaultImage,
    "Input": DefaultInput,
    "Label": DefaultLabel,
    "Link": DefaultLink,
    "ProgressBar": DefaultProgressBar,
    "ScrollView": DefaultScrollView,
    "Slider": DefaultSlider,
    "Switch": DefaultSwitch,
    "TabView": DefaultTabView,
    "Textarea": DefaultTextarea,
    "ComboBox": DefaultComboBox,
    "Column": DefaultColumn,
    "Row": DefaultRow,
    "Stack": DefaultStack,
    "Grid": DefaultGrid,
}

def register_widget(name: str, widget_class: type):
    """
    Registers a custom widget class to be used by the framework.
    This will override the default widget with the same name.

    Args:
        name: The name of the widget to override (e.g., "Button").
        widget_class: The new class to be used for this widget.
    """
    _WIDGET_REGISTRY[name] = widget_class
    print(f"Custom widget '{name}' registered.")

def create_widget(name: str, *args, **kwargs):
    """
    Creates an instance of a widget from the registry.
    It intercepts lifecycle hooks and attaches them to the widget instance
    instead of passing them to the constructor.

    Args:
        name: The name of the widget to create (e.g., "Button").
        *args, **kwargs: Arguments to pass to the widget's constructor.

    Returns:
        An instance of the registered widget.
        
    Raises:
        ValueError: If the widget name is not found in the registry.
    """
    widget_class = _WIDGET_REGISTRY.get(name)
    if not widget_class:
        raise ValueError(f"Widget type '{name}' not found in registry. Have you registered it?")
    
    # Intercept lifecycle hooks before they are passed to the widget's constructor.
    on_mount_handler = kwargs.pop("on_mount", None)
    on_unmount_handler = kwargs.pop("on_unmount", None)

    # Create the widget with the remaining safe kwargs.
    widget_instance = widget_class(*args, **kwargs)
    
    # Attach the hooks to the instance itself for the component decorator to find.
    if on_mount_handler:
        widget_instance._winup_on_mount = on_mount_handler
    if on_unmount_handler:
        widget_instance._winup_on_unmount = on_unmount_handler
        
    return widget_instance

def create_component(base_widget_func: callable, default_props: dict):
    """
    Creates a reusable component function from a base widget and default properties.

    Args:
        base_widget_func: The base widget factory function (e.g., ui.Button).
        default_props: A dictionary of props to apply by default.

    Returns:
        A new component function that can be used like any other ui element.
    """
    def new_component_func(*args, **kwargs):
        # Pop 'props' from kwargs, or use an empty dict
        instance_props = kwargs.pop("props", {})
        
        # Merge the default props with the instance-specific props
        final_props = merge_props(default_props, instance_props)
        
        # Pass the merged props to the base widget
        return base_widget_func(*args, props=final_props, **kwargs)

    return new_component_func 