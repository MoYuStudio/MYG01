
import sys

import pygame
from pygame.locals import *

import moyu_engine.config.data.constants as C

import moyu_engine.config.system.assets_system
import moyu_engine.config.system.tilemap_system
import moyu_engine.config.system.move_system

import moyu_engine.config.window.main_window

def init(): 

    pygame.init()
    pygame.mixer.init()

    SCREEN       = pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)
    SCREEN_TITLE = pygame.display.set_caption(C.window['title'])
    #pygame.display.set_icon(G.tl16)
    CLOCK = pygame.time.Clock()
    pygame.display.flip()

    moyu_engine.config.system.assets_system.AssetsSystem.loader()

    moyu_engine.config.system.tilemap_system.TilemapSystem.builder()
    
    while True:
        moyu_engine.config.system.move_system.MoveSystem.move()

        moyu_engine.config.window.main_window.MainWindow.blit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(C.window['fps'])

def run():
    init()

if __name__ == "__main__":

    pass
