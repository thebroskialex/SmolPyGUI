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
