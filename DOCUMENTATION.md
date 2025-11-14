# SmolPyGUI Full Documentation

SmolPyGUI is a lightweight and minimalistic GUI framework built on top of **Pygame**. 
It provides intuitive tools for creating simple graphical interfaces in Python programs or games without the complexity of larger frameworks.

This documentation explains every object, function, and system included in SmolPyGUI, how to use them, and how they interact.

Optional function arguments are marked with a ⎊ symbol, default values are marked as "⎊=Value".

---

## Getting Started

### Initialization

Before using any SmolPyGUI object, you must initialize the system with:

```python
smolpygui.initialize(size=(800, 600), framerate=60)
```

**Arguments:**
- `size` — window resolution as `(width, height)`. ⎊=(600,600)
- `framerate` — the refresh rate of your GUI (in ticks per second). ⎊=60
- `screenFlags` — optional Pygame display flags. ⎊
- `runtimeFuncs` — optional list of functions to run every frame. ⎊

This sets up the main window, creates the default scene (aliased as `0`), and prepares rendering.

---

### Main Loop

Once everything is created, call:

```python
smolpygui.MainLoop()
```

This begins the GUI loop and continues running until the user closes the window. 
Any updates, draws, or input events are handled automatically each tick.

Alternatively, you can manually control updates using:

```python
smolpygui.TICK(['all'])
```

This runs one frame of updates. The list argument can contain:
- `'draw'` — updates drawing.
- `'input'` — processes mouse and keyboard input.
- `'audio'` — Does literally nothing, sorry.
- `'object'` — updates object ticks.
- `'user'` — runs your custom runtime functions.
- `'all'` — runs all the above.

---

## Scenes

### Scene

Declaration:
`Scene(alias, backgroundColor)`

Creates a scene container for rendering and events. Scenes separate UI contexts, allowing screen transitions.

**Arguments:**
- `alias` — a unique name or number for the scene.
- `backgroundColor` — background color, can be a hex string (`"#000000"`) or RGB tuple. 

**Functions:**
- `.remove()` — Removes the scene from memory and scene registry.

### Switching Scenes

Use:
```python
scenes.switchScene(scene, fadeDur=0.5, hold=0.2)
```

- `scene` — the target Scene object or its alias. 
- `fadeDur` — duration of fade-in/out in seconds. ⎊=0
- `hold` — time to hold the black screen before fade-in. ⎊=0

The fade effect blocks all input while active.

---

## Objects

### Button

Declaration: 
`Button(x, y, width, height, texture, onClick, onHover=None, onUnHover=None, stroke=0, scene=0)`

- `x` — x position of the top-left corner   
- `y` — y position of the top-left corner   
- `width` — button width   
- `height` — button height   
- `texture` — color (e.g. `"#ff0000"`) or `pygame.Surface` object 
- `onClick` — callback executed when clicked   
- `onHover` — callback when the mouse hovers   ⎊
- `onUnHover` — callback when the mouse leaves hover  ⎊ 
- `stroke` — border thickness (0 = filled)   ⎊=0
- `scene` — scene alias   ⎊=0

**Functions:**
- `.setOnClick(func)` — sets a click callback.
- - `func` — callback executed when clicked, or None
- `.setOnHover(func)` — sets a hover callback.
- - `func` — callback executed when hovered over, or None
- `.setOnUnHover(func)` — sets an unhover callback.
- - `func` — callback executed when unhovered, or None
- `.remove()` — removes the object from the event and draw lists.

---

### DrawRect

Declaration:  
`DrawRect(x, y, width, height, texture, stroke=0, onClick=None, onHover=None, onUnHover=None, scene=0)`

Same arguments as `Button`, but this object is more general-purpose (can be static or interactive).
- `onClick` — ⎊

**Functions:**
- `.setOnClick(func)` — sets a click callback.
- - `func` — callback executed when clicked, or None
- `.setOnHover(func)` — sets a hover callback.
- - `func` — callback executed when hovered over, or None
- `.setOnUnHover(func)` — sets an unhover callback.
- - `func` — callback executed when unhovered, or None
- `.remove()` — removes the rectangle from rendering and events.

---

### Text

Declaration:  
`Text(x, y, text, size=16, font='courier', color="#000000", scene=0)`

Displays text at the given position.

**Arguments:**
- `x`, `y` — top-left corner coordinates. 
- `text` — string content. 
- `size` — font size. 
- `font` — one of `'Courier'`, `'Courier Italic'`, `'Roboto'`, `'Roboto Italic'`, or a path to a font file. ⎊='courier'
- `color` — text color. ⎊='#000000'
- `scene` — scene alias. ⎊=0

**Functions:**
- `.remove()` — removes the text from rendering.

---

### TextBox

Declaration:  
`TextBox(x, y, width, size, font='courier', bg="#ffffff", bgActive="#9999ff", outline="#444444", textColor="#000000", onUpdate=lambda x: None, onReturn=lambda x: None, onClick=lambda: None, onHover=None, onUnHover=None, scene=0)`

A text input box that accepts keyboard input.

**Arguments:**
- `x`, `y`, `width` — position and width. 
- `size` — font size. 
- `font` — built-in or custom font. ⎊='courier'
- `bg` — inactive background color. ⎊="#ffffff"
- `bgActive` — active background color. ⎊="#9999ff"
- `outline` — border color. ⎊="#000000"
- `textColor` — color of entered text. ⎊="#000000"
- `onUpdate(text)` — called every time text updates. ⎊  
- `onReturn(text)` — called when the Return key is pressed. ⎊
- `onClick()` — called when the box is clicked. ⎊
- `onHover()`, `onUnHover()` — optional hover events. ⎊
- `scene` — scene alias. ⎊=0

**Functions:**
- `.setVisible(value)` — shows/hides the text box. 
  - `value` — A boolean value to set the visibility to or the string "toggle" to toggle it ⎊='toggle'
- `.remove()` — removes all internal elements (text, outline, etc.).

---

### TextDisplay

Declaration:  
`TextDisplay(x, y, width, lines, size, font='courier', value="", bg="#ffffff", outline="#444444", textColor="#000000", align='left', onClick=None, scene=0)`

Displays multiline text with optional typing animation.

**Functions:**
- `.update(text, mode='reset')` — sets text. `mode` can be `'reset'`, `'append'`, or `'prepend'`. 
- `.typeWrite(text, chars=2, speed=25, mode='reset')` — animates text appearing. 
- `.setVisible(value)` — toggles visibility. 
- `.remove()` — removes the display and its children.

---

## Base Object Classes

### ScreenObject

Common properties for all visual elements.

**Attributes:**
- `.x` — x coordinate. 
- `.y` — y coordinate. 
- `.visible` — visibility flag. 
- `.scene` — the scene name or index. 

**Functions:**
- `.setVisible(value)` — sets visibility or toggles when `'toggle'` is passed.

### EventObject

Base for all event-reactive elements.

**Attributes:**
- `.active` — whether the event is processed. 
- `.scene` — which scene handles it. 

**Functions:**
- `.setActive(value)` — toggles or sets active state.

---

## Event Handling

### KeypressEvent

Declaration:  
`KeypressEvent(keycode, onKeyDown=None, onKeyUp=None, onKeyHeld=None, scene=0)`

Listens for key events.

**Arguments:**
- `keycode` — Pygame key constant or `'all'`. 
- `onKeyDown()` — callback on press. 
- `onKeyUp()` — callback on release. 
- `onKeyHeld()` — callback called every tick while held.

**Functions:**
- `.setOnDown(func)`  
- `.setOnUp(func)`  
- `.setOnHeld(func)`  
- `.remove()`

### MouseEvent

Declaration:  
`MouseEvent(mode, onEvent, scene=0)`

**Modes:** `'move'`, `'leftDown'`, `'leftUp'`, `'rightDown'`, `'rightUp'`, `'midDown'`, `'midUp'`, `'scrollUp'`, `'scrollDown'`.

**Functions:**
- `.remove()` — unregisters the event.

---

## Audio

### Sound

Declaration:  
`Sound(path, alias)`

Loads a sound or background music.

**Arguments:**
- `path` — file path to the sound file. 
- `alias` — identifier string or `"music"` / `"bgmusic"` for continuous playback.

### audio Module

**Functions:**
- `audio.playSound(sound_or_alias)` — plays a sound. 
- `audio.stopSound(sound_or_alias)` — stops playback.

---

## Globals

The `globals` module stores current engine state.

**Attributes:**
- `.renderer` — main Pygame display surface. 
- `.screen` — active scene surface. 
- `.scene` — current active Scene. 
- `.width`, `.height` — window size. 
- `.framerate` — target tick rate. 
- `.runtimeFuncs` — list of user functions executed each tick. 

---

## Drawing System

The `draw` module manages rendering.

**Functions:**
- `draw.drawRects()` — renders all rectangles and buttons. 
- `draw.drawTexts()` — renders all text elements. 
- `draw.drawAll()` — clears screen, draws everything, and updates display. 
- `draw.drawNoRender()` — same as `drawAll()` but does not flip the display buffer.

---

## Utility Functions

### getFont

Declaration:  
`getFont(name, size)`

Returns a Pygame `Font` object from one of SmolPyGUI’s built-in font names.

**Built-in options:**
- Courier
- Courier Italic
- Roboto
- Roboto Italic

---

## Example Usage

```python
import SmolPyGUI as smol

def say_hello():
    print("Hello, world!")

smol.initialize((640, 480), framerate=60)

# Create a button
btn = smol.Button(100, 100, 150, 50, "#22cc88", say_hello)

# Add text
txt = smol.Text(100, 50, "Click the button!")

# Run
smol.MainLoop()
```