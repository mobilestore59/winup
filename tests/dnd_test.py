import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import winup
from winup import ui, state, traits, component

# --- 1. State Setup ---
# We'll manage two lists of items.
state.create("items_list", [
    {"id": 1, "text": "Item 1"},
    {"id": 2, "text": "Item 2"},
    {"id": 3, "text": "Item 3"},
])
state.create("dropped_items_list", [])

# --- 2. Components ---

@component
def DraggableItem(item: dict, source_list_key: str):
    """A draggable label representing an item."""
    label = ui.Label(
        f"Drag Me: {item['text']}",
        props={
            "padding": "10px",
            "background-color": "#E0E0E0",
            "border-radius": "4px",
            "min-height": "40px",
        }
    )
    # Add the draggable trait with the item's data
    traits.add_trait(label, "draggable", data={"type": "list-item", "item_id": item["id"], "source_list": source_list_key})
    return label

@component
def DropZone(accepts_type: str, list_key: str, title: str):
    """A container that acts as a drop target and displays a list of items."""
    
    container = ui.Column(props={"spacing": 10, "padding": "10px", "background-color": "#F0F0F0", "border-radius": "4px"})

    def handle_drop(data: dict):
        """Called when a valid item is dropped here."""
        source_list_key = data["source_list"]
        item_id = data["item_id"]

        # Prevent dropping an item onto its own list
        if source_list_key == list_key:
            return

        # Find the item in the source list
        source_list_state = state.create(source_list_key)
        source_list = source_list_state.get()
        item_to_move = next((item for item in source_list if item["id"] == item_id), None)
        
        if item_to_move:
            # Remove from source list
            new_source_list = [item for item in source_list if item["id"] != item_id]
            source_list_state.set(new_source_list)
            
            # Add to this list
            target_list_state = state.create(list_key)
            target_list_state.set(target_list_state.get() + [item_to_move])

    # Add the droptarget trait
    traits.add_trait(container, "drop_target", on_drop=handle_drop)

    # Component to render the list contents
    list_view = ui.Column(props={"spacing": 5, "min-height": "100px"})

    def render_list(items):
        ui.clear_layout(list_view.layout())
        if items:
            for item in items:
                # Here we just show a static label, not a draggable one.
                list_view.add_child(ui.Label(f"Dropped: {item['text']}", props={"background-color": "#C8E6C9", "padding": "5px"}))
        else:
            list_view.add_child(ui.Label("Drop items here..."))

    # Subscribe to the list's state
    list_state = state.create(list_key)
    list_state.subscribe(render_list)
    render_list(list_state.get())
    
    return ui.Column(props={"spacing": 5}, children=[ui.Label(title, props={"font-weight": "bold"}), container, list_view])

@component
def App():
    """Main application component."""
    
    # The list of available, draggable items
    items_container = ui.Column(props={"spacing": 5})
    
    def render_source_list(items):
        ui.clear_layout(items_container.layout())
        for item in items:
            items_container.add_child(DraggableItem(item, "items_list"))
            
    source_list_state = state.create("items_list")
    source_list_state.subscribe(render_source_list)
    render_source_list(source_list_state.get())

    return ui.Row(
        props={"spacing": 20, "margin": "20px"},
        children=[
            ui.Column(props={"spacing": 10}, children=[
                ui.Label("Available Items", props={"font-weight": "bold"}),
                items_container
            ]),
            DropZone(accepts_type="list-item", list_key="dropped_items_list", title="Drop Zone"),
        ]
    )

# --- 3. Run Application ---
if __name__ == "__main__":
    # Add the project root to the path for hot reloading to work
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    winup.run(
        main_component_path="tests.dnd_test:App",
        title="Drag and Drop Test",
        dev=True
    )