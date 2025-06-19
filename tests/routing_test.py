# tests/routing_test.py
import winup
from winup import ui

# Since the router files might not have been created automatically,
# we need to handle the import gracefully.

from winup.router import Router, RouterView, RouterLink

# 1. Define your page components
@winup.component
def HomePage():
    print("Rendering Home Page")

    def on_mount():
        print("✅ HomePage MOUNTED")

    def on_unmount():
        print("❌ HomePage UNMOUNTED")

    return ui.Label(
        "Welcome to the Home Page!", 
        props={"font-size": "18px"},
        on_mount=on_mount,
        on_unmount=on_unmount
    )

@winup.component
def ProfilePage():
    print("Rendering Profile Page")

    def on_mount():
        print("✅ ProfilePage MOUNTED")

    def on_unmount():
        print("❌ ProfilePage UNMOUNTED")
        
    return ui.Label(
        "This is your user profile.", 
        props={"font-size": "18px"},
        on_mount=on_mount,
        on_unmount=on_unmount
    )

@winup.component
def SettingsPage():
    print("Rendering Settings Page")

    def on_mount():
        print("✅ SettingsPage MOUNTED")

    def on_unmount():
        print("❌ SettingsPage UNMOUNTED")

    return ui.Column(
        children=[
            ui.Label("Settings", props={"font-size": "18px"}),
            ui.Switch(text="Enable Experimental Features")
        ],
        on_mount=on_mount,
        on_unmount=on_unmount
    )

# 2. Create a router instance with your routes
app_router = Router({
    "/": HomePage,
    "/profile": ProfilePage,
    "/settings": SettingsPage,
})

# 3. Build the main application layout
@winup.component
def App():
    return ui.Column(
        props={"spacing": 15, "margin": "10px"},
        children=[
            # Navigation links
            ui.Row(
                props={"spacing": 20, "alignment": "AlignLeft"},
                children=[
                    RouterLink(router=app_router, to="/", text="Home"),
                    RouterLink(router=app_router, to="/profile", text="Profile"),
                    RouterLink(router=app_router, to="/settings", text="Settings")
                ]
            ),
            # Add a separator
            ui.Frame(props={"min-height": "1px", "background-color": "#dedede", "margin": "10px 0"}),
            
            # The RouterView will render the current page component
            ui.Frame(
                props={"padding": "10px", "layout": "vertical"},
                children=[
                    RouterView(router=app_router)
                ]
            )
        ]
    )

if __name__ == "__main__":
    if not Router:
        print("Cannot run test because router components are missing.")
    else:
        # Add the project root to the path for hot reloading to work
        import sys
        import os
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)

        winup.run(
            main_component_path="tests.routing_test:App",
            title="Routing Test",
            dev=True
        ) 