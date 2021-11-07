
import sys
import pygame
from pygame.locals import *

import moyu_engine.config.data.constants as C

import moyu_engine.config.system.tilemap_system

class MainWindow:
    def blit():

        blit_surface = pygame.Surface(C.window['size']).convert_alpha()

        background_surface = pygame.Surface(C.window['size']).convert_alpha()
        tilemap_surface        = pygame.Surface((int(C.window['set_size'][0]/C.window['tilemap_level']),int(C.window['set_size'][1]/C.window['tilemap_level']))).convert_alpha()
        sprite_surface = pygame.Surface((int(C.window['set_size'][0]/C.window['tilemap_level']),int(C.window['set_size'][1]/C.window['tilemap_level']))).convert_alpha()
        gui_surface        = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))

        tilemap_surface.fill((255,55,55,0))
        moyu_engine.config.system.tilemap_system.TilemapSystem.loarder(tilemap_surface,C.window['move'][0],C.window['move'][1])

        
        # for x in range(C.tilemap['boarder']):
        #     for y in range(C.tilemap['boarder']):

        #         if ((C.tilemap['tilemap'])[x][y])[0] == 5:
        #             rect = pygame.Rect((((C.tilemap['tilemap'])[x][y])[6]+C.window['move'][0],((C.tilemap['tilemap'])[x][y])[7]+C.window['move'][1],16,16),width=0)

        #             if C.player_rect.colliderect(rect):
        #                 print('1')
        #                 pygame.draw.rect(sprite_surface,(0,255,0),rect)

        #             else:
        #                 print('2')

        sprite_surface.blit(C.assets['player1-s'][-(0)-1],(C.window['set_size'][0]/2-8,C.window['set_size'][1]/2-8))

        tilemap_surfaceFin = pygame.transform.scale(tilemap_surface,(C.window['size']))
        sprite_surfaceFin = pygame.transform.scale(sprite_surface,(C.window['size']))

        blit_surface.blit(background_surface, (0, 0))
        blit_surface.blit(tilemap_surfaceFin, (0, 0))
        blit_surface.blit(sprite_surfaceFin, (0, 0))
        
        C.screen.blit(blit_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == K_UP or event.key == K_w:
                    C.window['move_switch']['up']   = True
                    
                if event.key == K_DOWN or event.key == K_s:
                    C.window['move_switch']['down'] = True

                if event.key == K_LEFT or event.key == K_a:
                    C.window['move_switch']['left'] = True

                if event.key == K_RIGHT or event.key == K_d:
                    C.window['move_switch']['right'] = True

                if event.key == K_q:
                    C.window['zoom_switch']['in']   = True

                if event.key == K_e:
                    C.window['zoom_switch']['out']  = True

            if event.type == pygame.KEYUP:

                if event.key == K_UP or event.key == K_w:
                    C.window['move_switch']['up']   = False

                if event.key == K_DOWN or event.key == K_s:
                    C.window['move_switch']['down'] = False

                if event.key == K_LEFT or event.key == K_a:
                    C.window['move_switch']['left'] = False

                if event.key == K_RIGHT or event.key == K_d:
                    C.window['move_switch']['right'] = False

                if event.key == K_q:
                    C.window['zoom_switch']['in']   = False

                if event.key == K_e:
                    C.window['zoom_switch']['out'] = False
