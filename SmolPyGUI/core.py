"""
SmolPyGUI

Version 1.5

Made with Pygame, many thanks to the Pygame team!
"""


import pygame
from typing import Literal, Callable, NoReturn, Any
from time import time, time_ns, sleep
pygame.init()

class Button():
    def __init__(self, x:int, y:int, width:int, height:int, texture:pygame.Color|pygame.surface.Surface, onClick:Callable, onHover:Callable=None, stroke:int=0, scene:int=0):
        """
        Basic constructor for Button objects, defines a rectangular button with width, height, x and y position, texture, a click function, and optionally a stroke value and a scene assignment.
        """
        self.visible = True
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.texture=texture
        self.onClick=onClick
        self.onHover=onHover
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
        Basic removal function, removes the object from execution order\n
        Returns False if an error occured, return True otherwise
        """
        try:
            scenes.scenes.pop(self.name)
        except (KeyError, ValueError): return False
        else: return True

class Sound():
    def __init__(self, sndPath:str, alias):
        self.snd = globals.audioPlayer.Sound(sndPath)
        if(alias):
            self.name = alias
            audio.sounds.update({alias:self})

class KeypressEvent():
    def __init__(self, keycode, onKeyDown:Callable, scene:int|str=0):
        self.key = keycode
        self.method = onKeyDown
        self.scene=scene
        events.keys.append(self)

    def remove(self):
        """
        Basic removal function, removes the object from execution order\n
        Returns False if an error occured, return True otherwise
        """
        try:
            events.keys.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class MouseEvent():
    def __init__(self, mode:Literal["move","rightDown","rightUp","leftDown","leftUp","midDown","midUp","scroll"],onEvent:Callable,active:bool=True):
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
        Basic removal function, removes the object from execution order\n
        Returns False if an error occured, return True otherwise
        """
        try:
            draw.rects.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class Text():
    def __init__(self, x:int, y:int, text:str, size:int=16, color:pygame.Color="#000000", scene:int|str=0):
        self.font = pygame.font.SysFont("Courier", size, True)
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
        Basic removal function, removes the object from execution order\n
        Returns False if an error occured, return True otherwise
        """
        try:
            draw.texts.remove(self)
        except (KeyError, ValueError): return False
        else: return True

class TextBox():
    def __init__(self, x:int, y:int, width:int, size:int, bg="#ffffff", bgActive="#9999ff",outline="#444444", textColor="#000000", onUpdate:Callable[[str],Any]=lambda x: None, onReturn:Callable[[str],Any]=lambda x: None, onClick:Callable=lambda: None, onHover:Callable=None, scene:int|str=0):
        self.x = x
        self.y = y
        self.charWid = size*0.6
        self.width = self.charWid*width
        self.height = size*1.25
        self.size = size
        self.value = ""
        self.drawVal = ""
        self.bg = bg
        self.bgActive = bgActive
        self.outline = outline
        self.textColor = textColor
        self.onUpdate = onUpdate
        self.onInput = onReturn
        self.onClick = onClick
        self.onHover = onHover
        self.button = Button(self.x, self.y, self.width, self.height, self.bg, lambda box=self:box.inputStart(), scene=scene)
        self.outBox = DrawRect(self.x, self.y, self.width, self.height, self.outline, 4, scene=scene)
        self.text = Text(self.x+5,self.y,self.value,self.size,self.textColor, scene=scene)
        self.indic = DrawRect(self.x+10, self.y+5, 2, self.height-10, self.bg, 0, scene=scene)
        if(not self.onHover == None):
            events.hovers.append(self)

    def inputStart(self):
        self.button.texture = self.bgActive
        self.onClick()
        while True:
            for e in pygame.event.get():
                if e.type == 256:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if(e.key == pygame.K_RETURN):
                        self.onInput(self.value)
                        self.button.texture = self.bg
                        return
                    elif(e.key == pygame.K_BACKSPACE):
                        self.value = self.value[:-1]
                    else:
                        self.value += e.unicode
                    if(len(self.value)*(0.7*self.size)>(self.width)):
                        self.drawVal = self.value[-int(self.width//(self.size*0.7)):]
                    else:
                        self.drawVal = self.value
                    self.text.text = self.drawVal
                    self.indic.x = (1+len(self.drawVal))*(0.6*self.size)
                    self.onUpdate(self.value)
            draw.drawAll()

    def remove(self):
        """
        Basic removal function, removes the object from execution order\n
        Returns False if an error occured, return True otherwise
        """
        try:
            self.button.remove()
            self.outBox.remove()
            self.indic.remove()
            self.text.remove()
        except (KeyError, ValueError): return False
        else: return True

class TextBoxTypeWriteState():
    def __init__(self):
        self.active = False
        self.full_text = ''
        self.charsPerType = 0
        self.nextTick = 0
        self.speed = 0

class TextDisplay():
    def __init__(self, x:int, y:int, width:int, lines:int, size:int, value:str="", bg:pygame.Color|pygame.surface.Surface="#ffffff",outline:pygame.Color="#444444", textColor:pygame.Color="#000000",scene:int|str=0):
        self.x = x
        self.y = y
        self.charWid = size*0.6
        self.width = self.charWid*width
        self.widthInChars = width
        self.charHgt = size*1.25
        self.height = size*1.25*lines
        self.lines = lines
        self.size = size
        self.drawVal = value
        self.bg = bg
        self.outline = outline
        self.textColor = textColor
        self.scene = scene
        self.typewriteState = TextBoxTypeWriteState()
        self.box = DrawRect(self.x, self.y, self.width, self.height, self.bg, scene=scene) if bg else False
        self.outBox = DrawRect(self.x, self.y, self.width, self.height, self.outline, 4, scene=scene) if outline else False
        events.tickingObjects.append(self)
        self.text = [Text(self.x+5,self.y+(self.charHgt*(i%width)),self.drawVal[width*(i%width):width+(width*(i%width))],self.size,self.textColor, scene=scene) for i in range(len(value)) if i%width < self.lines]
    
    def resetText(self) -> NoReturn:
        """
        Clears the TextDisplay object
        """
        [i.remove() for i in self.text]
        self.text = [Text(self.x+5,self.y+(self.charHgt*(i%self.widthInChars)),self.drawVal[self.widthInChars*(i%self.widthInChars):self.widthInChars+(self.widthInChars*(i%self.widthInChars))],self.size,self.textColor, scene=self.scene) for i in range(len(self.drawVal)) if i%self.widthInChars < self.lines]
    
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
   
    def typeWrite(self, text:str, chars:int=2,speed:int=25):
        """
        Writes text to the TextDisplay object with a fun animation!
        Writes `chars` characters per `speed` ticks.
        """
        self.update("", 'reset')
        self.typewriteState.active = True
        self.typewriteState.full_text = text
        self.typewriteState.charsPerType = chars
        self.typewriteState.speed = speed
        self.typewriteState.nextTick = pygame.time.get_ticks()+speed
    
    def remove(self):
        """
        Basic removal function, removes the object from execution order\n
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
    hovers:list[Button] = []
    tickingObjects:list = []
    mouse:dict[str,list[MouseEvent]] = {
        "move":[],
        "leftUp":[],
        "leftDown":[],
        "rightUp":[],
        "rightDown":[],
        "midUp":[],
        "midDown":[]
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
            if(event.button == 1):
                events.clickEvents()
                for leftDown in events.mouse['leftDown']:
                    leftDown.onEvent(mouse)
            elif(event.button == 2):
                for midDown in events.mouse['midDown']:
                    midDown.onEvent(mouse)
            elif(event.button == 3):
                for rightDown in events.mouse['rightDown']:
                    rightDown.onEvent(mouse)
            elif(event.button == 4):
                for scrollUp in events.mouse['scrollUp']:
                    scrollUp.onEvent()
            elif(event.button == 5):
                for scrollDown in events.mouse['scrollDown']:
                    scrollDown.onEvent
        elif(eventType == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                for leftUp in events.mouse['leftUp']:
                    leftUp.onEvent()
            elif(event.button == 2):
                for midUp in events.mouse['midUp']:
                    midUp.onEvent()
            elif(event.button == 3):
                for rightUp in events.mouse['rightUp']:
                    rightUp.onEvent()
        elif(eventType == pygame.MOUSEMOTION):
            for mouseMove in events.mouse['move']:
                mouseMove.onEvent(mouse)

    @staticmethod
    def hoverEvents():
        mouse = pygame.mouse.get_pos()
        for button in events.hovers:
            if (button.x <= mouse[0] <= button.x+button.width and button.y <= mouse[1] <= button.y+button.height) and globals.scene.name == button.scene:
                button.onHover()

    @staticmethod
    def keyEvents():
        keyspressed = pygame.key.get_pressed()
        for key in events.keys:
            if(keyspressed[key.key] and globals.scene.name == key.scene):
                key.method()

    @staticmethod
    def processTickEvents():
        events.keyEvents()
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

def initialize(size:tuple[int,int]=(600,600), framerate:int=60, screenFlags:int=0, runtimeFuncs:list[Callable]=[]):
    """
    This function initializes the full 
    """
    if(not globals.init):
        globals.framerate = framerate
        globals.runtimeFuncs = runtimeFuncs
        globals.renderer = pygame.display.set_mode(size, screenFlags)
        globals.width = size[0]
        globals.height = size[1]
        globals.scene = Scene(0, "#ffffff")
        globals.screen = globals.scene.screen

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
        elif((e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEMOTION) and inp):
            events.mouseEvents(e)
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

def MainLoop(framerate:int=60, **funcs:Callable):
    """
    The core function of your program. Functions similarly to tk.Tk().MainLoop(), but in a more pythonic way.
    Begins the main function loop and runs it at a steady `framerate`, supplied as the first argument into this function, while also running any extra functions (`funcs` kwargs) each tick.

    - framrate | `int`
    - **funcs | `Callable`

    NOTE: no further lines can be run after this function is called.
    """
    if(not globals.init):
        globals.framerate = framerate
        globals.runtimeFuncs = funcs
    while True:
        TICK(['all'])