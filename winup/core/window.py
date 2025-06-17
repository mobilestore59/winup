# winup/core/window.py

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from typing import Optional

class Window(QMainWindow):
    """
    Represents a top-level application window that can hold a WinUp component.
    """
    def __init__(self, component: QWidget, title="WinUp", width=800, height=600, icon_path: Optional[str] = None):
        """
        Creates and shows a new window.

        Args:
            component (QWidget): The root WinUp component/widget to display in the window.
            title (str): The window title.
            width (int): The initial width of the window.
            height (int): The initial height of the window.
            icon_path (str, optional): Path to the window icon.
        """
        # Ensure a QApplication instance exists.
        _WinUpApp.get_instance()
        super().__init__()

        self.setWindowTitle(title)
        self.resize(width, height)
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))

        self.setCentralWidget(component)
        self.show()

        # Register the window with the global app manager
        _winup_app.register_window(self)

class _WinUpApp:
    """Internal singleton class to manage the QApplication and windows."""
    _instance = None

    def __init__(self):
        if QApplication.instance():
            self.app = QApplication.instance()
        else:
            self.app = QApplication(sys.argv)
            
        self.windows = [] # Keep track of all open windows
        self._main_window: Optional[Window] = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = _WinUpApp()
        return cls._instance

    def create_main_window(self, component: QWidget, title, width, height, icon):
        """Creates the first, primary window for the application."""
        if self._main_window:
            raise RuntimeError("Main window has already been created.")
            
        self._main_window = Window(component, title, width, height, icon)
        return self._main_window

    def register_window(self, window: QMainWindow):
        """Adds a window to the list of tracked windows."""
        if window not in self.windows:
            self.windows.append(window)

    def run(self):
        """Starts the Qt application event loop."""
        sys.exit(self.app.exec())

# Global instance of the application manager
_winup_app = _WinUpApp.get_instance()
