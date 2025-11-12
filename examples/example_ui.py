from SmolPyGUI import initialize, Button, TextBox, MainLoop

initialize((600, 400))

# Define callbacks
def greet_user():
    print("Welcome to SmolPyGUI!")

def on_input(text):
    print(f"Input received: {text}")

# Add GUI elements
Button(250, 150, 100, 60, "#1e90ff", greet_user)
TextBox(150, 80, 300, 32, onReturn=on_input)

MainLoop()
