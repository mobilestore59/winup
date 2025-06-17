import winup
from winup import ui, profiler

# A simple, repeatable component to test memoization
@winup.memo
def ColorBlock(color):
    return ui.Frame(props={"background-color": color, "min-width": "20px", "min-height": "20px"})

# A function to build a large grid of these components
def build_grid(size=30):
    rows = []
    for i in range(size):
        row_children = []
        for j in range(size):
            # Create a pattern of colors that will repeat
            color = "#AABBCC" if (i + j) % 2 == 0 else "#CCDDEE"
            # Since the colors repeat, @memo should have many cache hits
            row_children.append(ColorBlock(color=color))
        rows.append(ui.Row(children=row_children, props={"spacing": 2}))
    return ui.Column(children=rows, props={"spacing": 2})

# We need a function to apply the profiler decorator to
@profiler.measure(func_name="Grid Creation Time")
def create_the_grid():
    return build_grid()

if __name__ == "__main__":
    print("Building a large component grid to test performance...")
    print("The '@memo' decorator on 'ColorBlock' should cache results.")
    
    # We need a dummy component to pass to run()
    def App():
        return ui.Frame()

    # We run our grid creation function before starting the app to profile it
    grid = create_the_grid()
    
    # The profiler's final results will be printed here
    profiler.print_results()

    print("\nNote the high 'Hit Ratio' in the Memoization Cache.")
    print("This means we avoided re-creating thousands of widgets.")
    
    # We don't need to run the app for this test, as we are just measuring
    # the creation time. You could uncomment the below line to see the grid.
    # winup.run(main_component=lambda: grid, title="Performance Test")