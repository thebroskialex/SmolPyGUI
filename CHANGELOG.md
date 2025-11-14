# 1.64.2.post1

Tiny TINY update, just fixed some naming issues in the Button class and removed some unused imports.

---

# 1.64.2

Minor update 1.64.2, adds some QoL features.

## ScreenObject
Added ScreenObject base class that all drawn objects inherit from. <sup>[\[1\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#screenobject)</sup>

Added .setVisible() function to all ScreenObject inherited classes, allowing for easier changing of visibility. <sup>[\[1\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#screenobject)</sup>

## EventObject
Added EventObject base class that all event callers inherit from. <sup>[\[2\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#eventobject)</sup>

## DrawRect
Added functions to DrawRect declaration <sup>[\[3\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#drawrect)</sup>

## Scenes
Added optional fade out/in for scene transition <sup>[\[4\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#scene)</sup>

## Utility Functions
Added draw.drawNoRender() function which draws everything onto global.screen without blitting it onto the rendered window. <sup>[\[5\]](https://www.github.com/thebroskialex/SmolPyGUI/blob/main/DOCUMENTATION.md#drawing-system)

## Bug fixes
Fixed bug where, when using the KeypressEvent.remove() method, the KeypressEvent would duplicate itself

---

# 1.64.1

Bug fix patch 1.64.0. Fixes bugs that were present, some fatally bad.

## Text
Fixed bug where all font inputs would result in the program looking for a file with that name

## Text Box
Fixed bug where the typing indicator would start at x of 0 instead of the left of the text box

Fixed bug where the text would overflow out of the text box at many font sizes

---

# 1.64

A major update, 1.64! Adds some pretty cool features, listed below.

## SmolPyGUI/fonts/
Added directory and 4 .ttf files for the font options
 
## Text
Added font options to Text, TextBox, and TextDisplay objects.

## TextBox
Changed the way TextBox objects handle input

Made the typing location indicator have a more accurate position

## TextDisplay
Added `mode` argument to TextDisplay.typeWrite

## getFont
Added `getFont()` function for accessing the SmolPyGUI/fonts/ folder.

## KeypressEvent
Added "all" keycode option

## 

---

# 1.62

## TextBox
Changed the width parameter to pixel width rather than by character amount

## TextDisplay
Changed the width parameter to pixel width rather than by character amount

Added text alignments
- Left
- Right
- Center

Fixed errors with text wrapping.

## README

Added example screenshots
