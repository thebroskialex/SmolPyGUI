from SmolPyGUI import initialize, Button, MainLoop

# Initialize GUI
initialize((400, 300))

# Define button callback
def on_button_click():
    print("Button clicked!")

# Create button
Button(150, 120, 100, 50, "#00aa00", on_button_click)

# Run loop
MainLoop()