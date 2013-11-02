import os, sys
import pygame
from pygame.locals import *

class PyManMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def LoadSprites(self):
        self.testpic = TestPic()
        self.sprites = pygame.sprite.RenderPlain((self.testpic))

    def MainLoop(self):
        while 1:
            for event in pygame.event.get():
                self.sprites.draw(self.screen)
                pygame.display.flip()
                if event.type == pygame.QUIT:
                    sys.exit()

class TestPic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("testpic.jpg",-1)
        self.pellets = 0
    
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()

print("Hello World!")
