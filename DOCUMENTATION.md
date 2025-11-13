# SmolPyGUI Documentation:

## Objects

### Button

Declaration: 
`Button(x,y,width,height,texture,onClick,onHover=None,onUnHover=None)`

- x | x position (of top left corner) [REQUIRED]
- y | y position (of top left corner) [REQUIRED]
- width | width of the button [REQUIRED]
- height | height of the button [REQUIRED]
- texture | looks of the button, could be color value (ie. `"#ff0000"`, `(255,0,0)`) or `pygame.surface.Surface` object. [REQUIRED]
- onClick | Callback function that activates when button is clicked [REQUIRED]
- onHover | Callback function that activates when the mouse hovers over the button [OPTIONAL]
- onUhHover | Callback function that activates when the mouse stops hovering over the button [OPTIONAL]

Functions:
- .remove() | Removes the object from drawing and event loops.

### DrawRect

Declaration:
`DrawRect(x,y,width,height,texture,onClick=None,onHover=None,onUnHover=None)`

### Text

Declaration:
`Text(x,y,text,size=16,font='courier')`

- x | x position (of top left corner) [REQUIRED]
- y | y position (of top left corner) [REQUIRED]
- text | string value of the text [REQUIRED]
- size | font size of the drawn text [OPTIONAL - DEFAULTS TO `16`]
- font | font name (see [fonts](#font-name-options)) or font file path of the drawn text [OPTIONAL - DEFAULTS TO `'courier'`]

### TextBox

## Other

### Font Name Options
There are four built-in fonts in SmolPyGUI, their names are as follows.

- Courier
- Courier Italic
- Roboto
- Roboto Italic
