# SmolPyGUI Documentation:

## Objects

### Button

Declaration: 
`Button(x,y,width,height,texture,onClick,onHover=None,onUnHover=None,stroke=0,scene=0)`

- x | x position (of top left corner) [REQUIRED]
- y | y position (of top left corner) [REQUIRED]
- width | width of the button [REQUIRED]
- height | height of the button [REQUIRED]
- texture | looks of the button, could be color value (ie. `"#ff0000"`, `(255,0,0)`) or `pygame.surface.Surface` object. [REQUIRED]
- onClick | Callback function that activates when button is clicked [REQUIRED]
- onHover | Callback function that activates when the mouse hovers over the button [OPTIONAL]
- onUhHover | Callback function that activates when the mouse stops hovering over the button [OPTIONAL]
- stroke | the stroke width of the button object, 0 being filled [OPTIONAL - DEFAULTS TO `0`]
- scene | The scene the button is drawn and handled in [OPTIONAL - DEFAULTS TO `0`]

Functions:
- .remove() | Removes the object from drawing and event loops.

### DrawRect

Declaration:
`DrawRect(x,y,width,height,texture,stroke,onClick=None,onHover=None,onUnHover=None,scene=0)`

- x | x position (of top left corner) [REQUIRED]
- y | y position (of top left corner) [REQUIRED]
- width | width of the button [REQUIRED]
- height | height of the button [REQUIRED]
- texture | looks of the button, could be color value (ie. `"#ff0000"`, `(255,0,0)`) or `pygame.surface.Surface` object. [REQUIRED]
- stroke | the stroke width of the button object, 0 being filled [OPTIONAL - DEFAULTS TO `0`]
- onClick | Callback function that activates when button is clicked [OPTIONAL]
- onHover | Callback function that activates when the mouse hovers over the button [OPTIONAL]
- onUhHover | Callback function that activates when the mouse stops hovering over the button [OPTIONAL]
- scene | The scene the button is drawn and handled in [OPTIONAL - DEFAULTS TO `0`]

Functions:

- [ScreenObject Functions](#screenobject)
- [EventObject Functions](#eventobject)
- .setOnClick(func:Callable|None) | Sets the onClick callback function to the given value
- .setOnHover(func:Callable|None) | Sets the onHover callback function to the given value
- .setOnUnHover(func:Callable|None) | Sets the onUnHover callback function to the given value

### KeypressEvent

Declaration:
`KeypressEvent(keycode,onKeyDown=None,onKeyUp=None,onKeyHeld=None,scene=0)`

- keycode | The pygame keycode that triggers the event, or `'all'` for all keys [REQUIRED]
- onKeyDown | the callback function that runs when the keycode is pressed down [OPTIONAL]
- onKeyUp | the callback function that runs when the keycode is released [OPTIONAL]
- onKeyHeld | the callback function that runs every tick the keycode is held down [OPTIONAL]

Attributes:

- [EventObject Attributes](#eventobject)

Functions:

- [EventObject Functions](#eventobject)
- .remove() | removes the KeypressEvent from activating permanently

### Text

Declaration:
`Text(x,y,text,size=16,font='courier')`

- x | x position (of top left corner) [REQUIRED]
- y | y position (of top left corner) [REQUIRED]
- text | string value of the text [REQUIRED]
- size | font size of the drawn text [OPTIONAL - DEFAULTS TO `16`]
- font | font name (see [fonts](#font-name-options)) or font file path of the drawn text [OPTIONAL - DEFAULTS TO `'courier'`]

### TextBox

## Base Object Classes

### ScreenObject

Attributes:

- .x | x position of the top left corner of the object
- .y | y position of the top left corner of the object
- .visible | Boolean that determines whether something is visible on screen [Direct Interfacing Not Recomended]
- .scene | scene in which the object is rendered [Direct Interfacing Not Recomended]


Functions:

- .setVisible(value:bool|'toggle') | Sets the visibility of an object (and, in the case of TextBox and TextDisplay, all child objects).

### EventObject

Attributes:

- .active | whether or not the event is handled [Direct Interfacing Not Recomended]
- .scene | what scene the event is handled in [Direct Interfacing Not Recomended]

Functions:

- .setActive(value:bool|'toggle') | Sets the active value of the event to the given boolean or toggles it.

## Other

### Font Name Options
There are four built-in fonts in SmolPyGUI, their names are as follows.

- Courier
- Courier Italic
- Roboto
- Roboto Italic
