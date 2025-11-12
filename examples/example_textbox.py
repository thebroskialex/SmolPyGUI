from SmolPyGUI import initialize, TextBox, MainLoop

initialize((500, 200))

# Create textbox
def on_enter(text):
    print(f"User entered: {text}")

TextBox(50, 80, 400, 32, onReturn=on_enter)

MainLoop()
