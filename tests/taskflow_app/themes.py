# Universal styles that apply to both themes
base_styles = {
    "QMainWindow": {
        "font-family": "Segoe UI"
    },
    "QPushButton": {
        "padding": "8px 15px",
        "border-radius": "4px",
        "font-size": "14px",
        "border": "1px solid transparent"
    },
    "QLabel": {
        "font-size": "14px"
    },
    "QLineEdit": {
        "padding": "8px",
        "border-radius": "4px",
        "font-size": "14px",
        "border": "1px solid"
    },
    "#navbar": {
        "background-color": "transparent",
        "border-bottom": "1px solid",
    },
    "#navbar QPushButton": {
        "border": "none",
        "padding": "10px",
        "font-weight": "bold",
        "border-bottom": "2px solid transparent",
    },
    "#navbar QPushButton[class~='active']": {
        "border-bottom-color": "#007BFF"
    },
    "Frame[class~='card']": {
        "border-radius": "6px",
        "border": "1px solid",
    },
    "QLineEdit[class~='valid']": {
        "border-color": "#28a745"
    },
    "QLineEdit[class~='invalid']": {
        "border-color": "#dc3545"
    }
}

light_theme = {
    **base_styles,
    "QMainWindow": {
        **base_styles["QMainWindow"],
        "background-color": "#ffffff",
    },
    "QLabel": {
        **base_styles["QLabel"],
        "color": "#212529"
    },
    "QLineEdit": {
        **base_styles["QLineEdit"],
        "border-color": "#ced4da",
        "background-color": "#ffffff",
        "color": "#495057"
    },
    "QPushButton": {
        **base_styles["QPushButton"],
        "background-color": "#f8f9fa",
        "color": "#343a40",
        "border-color": "#ced4da"
    },
    "QPushButton[class~='primary']": {
        "background-color": "#007bff",
        "color": "white",
        "border-color": "#007bff"
    },
    "#navbar": {
        **base_styles["#navbar"],
        "border-bottom-color": "#dee2e6"
    },
    "Frame[class~='card']": {
        **base_styles["Frame[class~='card']"],
        "border-color": "#dee2e6",
        "background-color": "#f8f9fa"
    }
}

dark_theme = {
    **base_styles,
    "QMainWindow": {
        **base_styles["QMainWindow"],
        "background-color": "#212529",
    },
    "QLabel": {
        **base_styles["QLabel"],
        "color": "#f8f9fa"
    },
    "QLineEdit": {
        **base_styles["QLineEdit"],
        "border-color": "#495057",
        "background-color": "#343a40",
        "color": "#f8f9fa"
    },
    "QPushButton": {
        **base_styles["QPushButton"],
        "background-color": "#343a40",
        "color": "#f8f9fa",
        "border-color": "#495057"
    },
    "QPushButton[class~='primary']": {
        "background-color": "#007bff",
        "color": "white",
        "border-color": "#007bff"
    },
    "#navbar": {
        **base_styles["#navbar"],
        "border-bottom-color": "#343a40"
    },
    "Frame[class~='card']": {
        **base_styles["Frame[class~='card']"],
        "border-color": "#495057",
        "background-color": "#343a40"
    }
} 