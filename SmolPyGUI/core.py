"""
SmolPyGUI

Version 1.6

Made with Pygame, many thanks to the Pygame team!
"""


import pygame
from typing import Literal, Callable, NoReturn, Any
from time import time, time_ns, sleep
from math import floor
from importlib import resources
pygame.init()


class NotInitializedError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Button():
    def __init__(self, x:int, y:int, width:int, height:int, texture:pygame.Color|pygame.surface.Surface, onClick:Callable, onHover:Callable=None, onUnHover:Callable=None, stroke:int=0, scene:int=0):
        """
        Basic constructor for Button objects, defines a rectangular button with width, height, x and y position, texture, a click function, and optionally a stroke value and a scene assignment.
        """
        self.visible = True
        self.active = True
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.texture=texture
        self.onClick=onClick
        self.onHover=onHover
        self.onUnHover = onUnHover
        self.hovered = False
        self.stroke = stroke
        self.scene=scene
        events.buttons.append(self)
        if(not onHover == None):
            events.hovers.append(self)
        draw.rects.append(self)

    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            events.buttons.remove(self)
            draw.rects.remove(self)
            if(not self.onHover == None):
                events.hovers.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class Scene():
    def __init__(self, alias, backgroundColor):
        self.screen = pygame.surface.Surface((globals.width, globals.height))
        self.name = alias
        self.bg = backgroundColor
        scenes.scenes.update({alias:self})

    def remove(self) -> int|bool:
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            scenes.scenes.pop(self.name)
        except (KeyError, ValueError): return False
        else: return True

class Sound():
    def __init__(self, sndPath:str, alias:str|Literal["music"]):
        self.snd = globals.audioPlayer.Sound(sndPath)
        if(alias):
            self.name = alias
            audio.sounds.update({alias:self})

class KeypressEvent():
    def __init__(self, keycode:int|Literal['all'], onKeyDown:Callable=None, onKeyHeld:Callable=None, onKeyUp:Callable=None, scene:int|str=0):
        self.key = keycode
        self.onDown = onKeyDown
        self.onHeld = onKeyHeld
        self.onUp = onKeyUp
        self.scene=scene
        self.active=True
        if(isinstance(keycode,int)):
            events.keys.append(self)
        elif(keycode == "all"):
            events.keysAll.append(self)

    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            if(self.key == 'all'):
                events.keysAll.append(self)
            else:
                events.keys.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class MouseEvent():
    def __init__(self, mode:Literal["move","rightDown","rightUp","leftDown","leftUp","midDown","midUp","scrollUp","scrollDown"],onEvent:Callable,active:bool=True):
        self.onEvent = onEvent
        self.active = active
        events.mouse[mode].append(self)

class DrawRect():
    def __init__(self, x:int, y:int, width:int, height:int, texture:pygame.Color|pygame.surface.Surface, stroke:int=0,scene:int|str=0):
        self.visible = True
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.texture=texture
        self.stroke=stroke
        self.scene=scene
        draw.rects.append(self)

    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            draw.rects.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class Text():
    def __init__(self, x:int, y:int, text:str, size:int=16, font:Literal['Courier','Courier Italic','Roboto','Roboto Italic']|str='courier', color:pygame.Color="#000000", scene:int|str=0):
        if(font.lower() in ['Courier','Courier Italic','Roboto','Roboto Italic']):
            self.font = getFont(font, size)
        else:
            self.font = pygame.font.Font(font, size)
        self.visible=True
        self.x=x
        self.y=y
        self.size=size
        self.text=text
        self.color=color
        self.scene=scene
        draw.texts.append(self)

    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            draw.texts.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class TextBoxInputState():
    def __init__(self):
        self.active = False

class TextBox():
    def __init__(self, x:int, y:int, width:int, size:int, font:Literal['Courier','Courier Italic','Roboto','Roboto Italic']='courier', bg="#ffffff", bgActive="#9999ff",outline="#444444", textColor="#000000", onUpdate:Callable[[str],Any]=lambda x: None, onReturn:Callable[[str],Any]=lambda x: None, onClick:Callable=lambda: None, onHover:Callable=None, onUnHover:Callable=None, scene:int|str=0):
        """Basic constructor for a TextBox object, the onUpdate and onReturn callback methods are supplied with the current TextBox text content when called."""
        self.x = x
        self.y = y
        self.fontName = font
        self.font = getFont(font,size)
        self.charWid = self.font.size("M")[0]
        self.width = width
        self.height = self.font.size("M")[1]
        self.size = size
        self.value = ""
        self.drawVal = ""
        self.bg = bg
        self.bgActive = bgActive
        self.outline = outline
        self.textColor = textColor
        self.active = True
        self.onUpdate = onUpdate
        self.onInput = onReturn
        self.onClick = onClick
        self.onHover = onHover
        self.onUnHover = onUnHover
        self.hovered = False
        self.scene = scene
        self.button = Button(self.x, self.y, self.width, self.height, self.bg, lambda box=self:box.inputStart() if box.active else None, scene=scene)
        self.outBox = DrawRect(self.x, self.y, self.width, self.height, self.outline, 4, scene=scene)
        self.text = Text(self.x+5,self.y,self.value,self.size,self.fontName,self.textColor, scene=scene)
        self.indic = DrawRect(self.x+10, self.y+5, 2, self.height-10, self.bg, 0, scene=scene)
        self.textboxinput = None
        if(not self.onHover == None):
            events.hovers.append(self)

    def inputStart(self):
        self.button.texture = self.bgActive
        self.onClick()
        self.textboxinput = KeypressEvent('all',self.processKey)

    def processKey(self,_,e):
        if(e.key == pygame.K_RETURN):
            self.onInput(self.value)
            self.button.texture = self.bg
            self.textboxinput.remove()
            self.textboxinput = None
        elif(e.key == pygame.K_BACKSPACE):
            self.value = self.value[:-1]
        else:
            self.value += e.unicode
        if(len(self.value)*(self.charWid)>(self.width)):
            self.drawVal = self.value[-int(self.width//(self.charWid)):]
        else:
            self.drawVal = self.value
        self.text.text = self.drawVal
        self.indic.x = (len(self.drawVal))*(self.charWid)
        self.onUpdate(self.value)

    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            self.button.remove()
            self.outBox.remove()
            self.indic.remove()
            self.text.remove()
        except (KeyError, ValueError): return False
        else: return True

class TextDisplayTypeWriteState():
    def __init__(self):
        self.active = False
        self.full_text = ''
        self.charsPerType = 0
        self.nextTick = 0
        self.speed = 0

class TextDisplay():
    def __init__(self, x:int, y:int, width:int, lines:int, size:int, font:Literal['Courier','Courier Italic','Roboto','Roboto Italic']='courier', value:str="", bg:pygame.Color|pygame.surface.Surface="#ffffff",outline:pygame.Color="#444444", textColor:pygame.Color="#000000",align:Literal["left","center"]="left",onClick:Callable=None,scene:int|str=0):
        self.x = x
        self.y = y
        self.fontName = font
        self.charWid = self.font.size("M")[0]
        self.width = width
        self.widthInChars = floor(width/self.charWid)
        self.charHgt = size*1.25
        self.height = self.font.size("M")[1]*lines*2
        self.lines = lines
        self.size = size
        self.drawVal = ""
        self.align = align
        self.bg = bg
        self.outline = outline
        self.textColor = textColor
        self.scene = scene
        self.typewriteState = TextDisplayTypeWriteState()
        self.onClick = onClick
        self.active = True
        if(not self.onClick==None):
            events.buttons.append(self)
        self.box = DrawRect(self.x, self.y, self.width, self.height, self.bg, scene=scene) if bg else False
        self.outBox = DrawRect(self.x, self.y, self.width, self.height, self.outline, 4, scene=scene) if outline else False
        events.tickingObjects.append(self)
        self.text = []
        self.update(value, 'reset')

    @staticmethod
    def getCharsToLineEnd(wid,posS):
        posL = posS%wid
        posL = wid if posL==0 else posL
        return(wid-posL)

    def resetText(self) -> NoReturn:
        offs=0
        for nC,c in enumerate(self.drawVal):
            if(c == "\n"):
                Val = list(self.drawVal)
                Val.remove("\n")
                chrs = self.getCharsToLineEnd(self.widthInChars,nC+offs)
                Val.insert(nC+offs," "*chrs)
                offs+=chrs-1
                self.drawVal = "".join(Val)
        [i.remove() for i in self.text]
        self.text = []
        self.text = [Text(self.x+5,self.y+(self.charHgt*(i%self.widthInChars)),self.drawVal[self.widthInChars*(i%self.widthInChars):self.widthInChars+(self.widthInChars*(i%self.widthInChars))],self.size,self.fontName,self.textColor, scene=self.scene) for i in range(self.lines) if i%self.widthInChars < self.lines]
        #for i in range(len(self.drawVal)):
        #    if i%self.widthInChars < self.lines:
        #        yVal = self.y+(self.charHgt*(i%self.widthInChars))
        #        tVal=self.drawVal[self.widthInChars*(i%self.widthInChars):self.widthInChars+(self.widthInChars*(i%self.widthInChars))]
        #        self.text.append(Text(self.x+5,yVal,tVal,self.size,self.textColor, scene=self.scene))
        if(self.align == "center"):
            for t in self.text:
                wid = len(t.text)*self.charWid
                t.x = self.x + (self.width-wid)/2
        elif(self.align == "right"):
            for t in self.text:
                wid = len(t.text)*self.charWid
                t.x = self.x + (self.width-wid)

    def update(self, Text:str, mode:Literal["reset","append","prepend"]="reset") -> NoReturn:
        """
        Changes the TextDisplay object's text to one of three options (based on `mode` argument):
        - reset | previousText = Text
        - append | previousText += Text
        - prepend | previousText = Text + previousText
        """
        mode = mode.lower()
        if(mode == "reset"):
            self.drawVal = Text
            self.resetText()
        elif(mode == "append"):
            self.drawVal += Text
            self.resetText()
        elif(mode == "prepend"):
            self.drawVal = Text + self.drawVal
            self.resetText()
        else:
            raise ValueError(f"TextDisplay.update mode argument must be \"reset\", \"append\", or \"prepend\", not {mode}")
   
    def typeWrite(self, text:str, chars:int=2,speed:int=25,mode:Literal['reset','append']='reset'):
        """
        Writes text to the TextDisplay object with a fun animation!
        Writes `chars` characters per `speed` ticks.
        """
        if(mode == 'reset'):
            self.update("", 'reset')
        self.typewriteState.active = True
        self.typewriteState.full_text = text
        self.typewriteState.charsPerType = chars
        self.typewriteState.speed = speed
        self.typewriteState.nextTick = pygame.time.get_ticks()+speed
    
    def remove(self):
        """
        Basic removal function, removes the object from execution order
        Returns False if an error occured, return True otherwise
        """
        try:
            self.box.remove()
            self.outBox.remove()
            events.tickingObjects.remove(self)
            [i.remove() for i in self.text]
        except:
            return False
        else:
            return True
    
    def tick(self):
        if(self.typewriteState.active == True):
            current = pygame.time.get_ticks()
            if(len(self.drawVal)>=len(self.typewriteState.full_text)):
                self.typewriteState.active = False
                return
            if(current >= self.typewriteState.nextTick):
                self.drawVal+=self.typewriteState.full_text[len(self.drawVal):len(self.drawVal)+self.typewriteState.charsPerType]
                self.resetText()
                self.typewriteState.nextTick = current + self.typewriteState.speed



class globals:
    renderer = None
    screen = None
    scene = None
    width = None
    height = None
    clock = pygame.time.Clock()
    framerate = 0
    runtimeFuncs = []
    init = False
    audioPlayer = pygame.mixer

class audio:
    sounds = {}

    def playSound(snd:Sound|str):
        if(isinstance(snd, str)):
            snd = Sound(str, False)
        if(snd.name == "music" or snd.name == "bgMusic"):
            snd.snd.play(1)
            return
        snd.snd.play()

class scenes:
    scenes:dict[str|int,Scene] = {0:globals.scene}

    def switchScene(scene):
        if(isinstance(scene, Scene)):
            scene = scene.name
        globals.scene = scenes.scenes[scene]
        globals.screen = scenes.scenes[scene].screen
        

class events:
    buttons:list[Button] = []
    keys:list[KeypressEvent] = []
    keysAll:list[KeypressEvent] = []
    hovers:list[Button] = []
    tickingObjects:list = []
    mouse:dict[str,list[MouseEvent]] = {
        "move":[],
        "leftUp":[],
        "leftDown":[],
        "rightUp":[],
        "rightDown":[],
        "midUp":[],
        "midDown":[],
        "scrollUp":[],
        "scrollDown":[]
    }

    @staticmethod
    def clickEvents():
        mouse = pygame.mouse.get_pos()
        for button in events.buttons:
            if button.x <= mouse[0] <= button.x+button.width and button.y <= mouse[1] <= button.y+button.height and globals.scene.name == button.scene and button.active:
                button.onClick()

    @staticmethod
    def mouseEvents(event):
        eventType = event.type
        mouse = pygame.mouse.get_pos()
        if(eventType == pygame.MOUSEBUTTONDOWN):
            if(event.button == pygame.BUTTON_LEFT):
                events.clickEvents()
                for leftDown in events.mouse['leftDown']:
                    if(leftDown.active):
                        leftDown.onEvent(mouse)
            elif(event.button == pygame.BUTTON_MIDDLE):
                for midDown in events.mouse['midDown']:
                    if(midDown.active):
                        midDown.onEvent(mouse)
            elif(event.button == pygame.BUTTON_RIGHT):
                for rightDown in events.mouse['rightDown']:
                    if(rightDown.active):
                        rightDown.onEvent(mouse)
            elif(event.button == pygame.BUTTON_WHEELUP):
                for scrollUp in events.mouse['scrollUp']:
                    if(scrollUp.active):
                        scrollUp.onEvent()
            elif(event.button == pygame.BUTTON_WHEELDOWN):
                for scrollDown in events.mouse['scrollDown']:
                    if(scrollDown.active):
                        scrollDown.onEvent()
        elif(eventType == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                for leftUp in events.mouse['leftUp']:
                    if(leftUp.active):
                        leftUp.onEvent()
            elif(event.button == 2):
                for midUp in events.mouse['midUp']:
                    if(midUp.active):
                        midUp.onEvent()
            elif(event.button == 3):
                for rightUp in events.mouse['rightUp']:
                    if(rightUp.active):
                        rightUp.onEvent()
        elif(eventType == pygame.MOUSEMOTION):
            for mouseMove in events.mouse['move']:
                    if(mouseMove.active):
                        mouseMove.onEvent(mouse)

    @staticmethod
    def hoverEvents():
        mouse = pygame.mouse.get_pos()
        for button in events.hovers:
            if not button.hovered and (button.x <= mouse[0] <= button.x+button.width and button.y <= mouse[1] <= button.y+button.height) and globals.scene.name == button.scene and button.active:
                button.onHover()
                button.hovered = True
            elif button.hovered and not (button.x <= mouse[0] <= button.x+button.width and button.y <= mouse[1] <= button.y+button.height):
                button.hovered = False
                if(not button.onUnHover == None):
                    button.onUnHover()

    @staticmethod
    def keyHoldEvents():
        keyspressed = pygame.key.get_pressed()
        for key in events.keys:
            if(keyspressed[key.key] and globals.scene.name == key.scene and key.active and not key.onHeld == None):
                key.onHeld()

    @staticmethod
    def keyUpDownEvents(event:pygame.event.Event):
        if(event.type == pygame.KEYDOWN):
            for keyA in events.keysAll:
                keyA.onDown(event.key,event)
            for key in events.keys:
                if(event.key == key.key and globals.scene.name == key.scene and key.active and not key.onDown == None):
                    key.onDown()
        elif(event.type == pygame.KEYUP):
            for key in events.keys:
                if(event.key == key.key and globals.scene.name == key.scene and key.active and not key.onUp == None):
                    key.onUp()

    @staticmethod
    def processTickEvents():
        events.keyHoldEvents()
        events.hoverEvents()

class draw:
    rects:list[DrawRect|Button] = []
    texts:list[Text] = []

    @staticmethod
    def drawRects():
        for rec in draw.rects:
            if(rec.visible and rec.scene == globals.scene.name):
                if(isinstance(rec.texture, pygame.surface.Surface)):
                    globals.screen.blit(rec.texture, (rec.x,rec.y), (0,0,rec.width,rec.height))
                else:
                    pygame.draw.rect(globals.screen, rec.texture, (rec.x,rec.y,rec.width,rec.height),rec.stroke)

    @staticmethod
    def drawTexts():
        for tex in draw.texts:
            if(tex.visible and tex.scene == globals.scene.name):
                globals.screen.blit(tex.font.render(tex.text, True, tex.color), (tex.x,tex.y))

    @staticmethod
    def drawAll():
        globals.screen.fill(globals.scene.bg)
        draw.drawRects()
        draw.drawTexts()
        globals.renderer.blit(globals.screen, (0,0))
        pygame.display.flip()

def getFont(name:Literal['Courier','Courier Italic','Roboto','Roboto Italic'],size:int):
    font_map = {
        "courier": "fonts/CourierPrime-Regular.ttf",
        "courier italic": "fonts/CourierPrime-Italic.ttf",
        "roboto": "fonts/RobotoMono-Regular.ttf",
        "roboto italic": "fonts/RobotoMono-Italic.ttf"
    }
    filename = font_map.get(name.lower())
    if not filename:
        raise ValueError(f"Unknown font: {name}")
    with resources.path("SmolPyGUI", filename) as p:
        return pygame.font.Font(p,size)

def initialize(size:tuple[int,int]=(600,600), framerate:int=60, screenFlags:int=0, runtimeFuncs:list[Callable]=[]):
    """
    This function initializes the program and screen
    """
    if(not globals.init):
        globals.framerate = framerate
        globals.runtimeFuncs = runtimeFuncs
        globals.renderer = pygame.display.set_mode(size, screenFlags)
        globals.width = size[0]
        globals.height = size[1]
        globals.scene = Scene(0, "#ffffff")
        globals.screen = globals.scene.screen
        globals.init = True

def TICK(modes:list[Literal['all','draw','input','audio','user','object']]):
    inp = False
    drw = False
    aud = False
    usr = False
    obj = False
    if('all' in modes):
        inp = True
        drw = True
        aud = True
        usr = True
        obj = True
    if('input' in modes):
        inp = True
    if("draw" in modes):
        drw = True
    if("audio" in modes):
        aud = True
    if("user" in  modes):
        usr = True
    if("object" in modes):
        obj = True
    for e in pygame.event.get():
        if(e.type == 256):
            raise SystemExit
        elif((e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP or e.type == pygame.MOUSEMOTION) and inp):
            events.mouseEvents(e)
        elif e.type == pygame.KEYDOWN or e.type == pygame.KEYUP and inp:
            events.keyUpDownEvents(e)
    if(inp):
        events.processTickEvents()
    if(usr):
        for func in globals.runtimeFuncs:
            func()
    if(obj):
        for object in events.tickingObjects:
            object.tick()
    if(drw):
        draw.drawAll()

def MainLoop():
    """
    The core function of your program. Functions similarly to tk.Tk().MainLoop().
    Begins the main function loop and runs it at a steady `framerate`, supplied as the first argument into this function, while also running any extra functions (`funcs` kwargs) each tick.

    - framrate | `int`
    - **funcs | `Callable`

    NOTE: no further lines can be run after this function is called.
    """
    if(not globals.init):
        raise NotInitializedError("The initialize() function was not called before the MainLoop function.")
    while True:
        TICK(['all']) 