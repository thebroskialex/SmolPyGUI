SmolPyGUI is a little personal project that I decided I would upload to PyPI. 
Below are some examples of usage.

A Simple Hello World
```python
from SmolPyGUI import initialize, Button, MainLoop

initialize((500,500)) #makes a 500x500 window

Button(300,300,100,100,"#ff0000",lambda: print("Hello World!")) #makes a 100x100 red button at 300,300 that prints "Hello World!"

MainLoop() #starts the program
```
