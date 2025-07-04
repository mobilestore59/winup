from .base import Trait
from PySide6.QtWidgets import QWidget
from ..style import styler as style_manager

class HoverEffectTrait(Trait):
    """
    Applies a set of styles when the mouse hovers over the widget.
    Relies on the styler to re-render the widget's style.
    """
    def apply(self, widget: QWidget):
        super().apply(widget)
        self.hover_style = self.options.get("style", {})
        self._original_enterEvent = widget.enterEvent
        self._original_leaveEvent = widget.leaveEvent
        widget.enterEvent = self._enterEvent
        widget.leaveEvent = self._leaveEvent

    def _enterEvent(self, event):
        style_manager.set_dynamic_property(self.widget, "hover", True)
        if self._original_enterEvent:
            self._original_enterEvent(event)

    def _leaveEvent(self, event):
        style_manager.set_dynamic_property(self.widget, "hover", False)
        if self._original_leaveEvent:
            self._original_leaveEvent(event)

    def remove(self):
        self.widget.enterEvent = self._original_enterEvent
        self.widget.leaveEvent = self._original_leaveEvent
        super().remove()

class HighlightableTrait(Trait):
    """
    Adds a 'highlighted' state that can be toggled, applying a specific style.
    """
    def apply(self, widget: QWidget):
        super().apply(widget)
        self.highlighted = False

    def toggle(self, highlighted: bool):
        self.highlighted = highlighted
        style_manager.set_dynamic_property(self.widget, "highlighted", self.highlighted)

    def remove(self):
        self.toggle(False) # Ensure highlight is removed
        super().remove() 