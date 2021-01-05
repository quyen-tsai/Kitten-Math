import pygame
import sys
from pygame.locals import *
#from back_ground import Background

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        #self.image = pygame.image.load('Menu3.jpg').convert()
        #self.image = pygame.transform.scale(self.image, (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def create_text(self, text):
        text = text
        return text

    """def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)"""

    def blit_screen(self):
        self.game.window.blit(self.game.image, (0, 0))
        self.game.reset_keys()

    def renderText(self, text, width, height, color, size):
        font = pygame.font.Font('Whale.ttf', size)
        textsurface = font.render(text, False, color)
        textrect = textsurface.get_rect()
        textrect.centerx = width / 2
        textrect.centery = height / 2
        self.game.window.blit(textsurface, textrect)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        text1 = self.create_text("Main Menu")
        text2 = self.create_text("Start Game")
        text3 = self.create_text("Option")
        text4 = self.create_text("Quit")
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            #self.draw_cursor()
            self.blit_screen()
            self.game.mouse = pygame.mouse.get_pos()
            self.renderText(text1, self.game.DISPLAY_W, self.game.DISPLAY_H - 100, self.game.WHITE, 100)
            if 693 <= self.game.mouse[0] <= 1223 and 600 <= self.game.mouse[1] <= 672:
                self.renderText(text2, self.game.DISPLAY_W, self.game.DISPLAY_H + 200, self.game.WHITE, 100)
            else:
                self.renderText(text2, self.game.DISPLAY_W, self.game.DISPLAY_H + 200, self.game.DARK, 100)

            if 861 <= self.game.mouse[0] <= 1057 and 803 <= self.game.mouse[1] <= 871:
                self.renderText(text4, self.game.DISPLAY_W, self.game.DISPLAY_H + 600, self.game.WHITE, 100)
            else:
                self.renderText(text4, self.game.DISPLAY_W, self.game.DISPLAY_H + 600, self.game.DARK, 100)

            if 818 <= self.game.mouse[0] <= 1103 and 700 <= self.game.mouse[1] <= 793:
                self.renderText(text3, self.game.DISPLAY_W, self.game.DISPLAY_H + 400, self.game.WHITE, 100)
            else:
                self.renderText(text3, self.game.DISPLAY_W, self.game.DISPLAY_H + 400, self.game.DARK, 100)
            pygame.display.flip()
            self.game.clock.tick(60)




    """def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop =(self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop =(self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop =(self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state """

    def check_input(self):
        #self.move_cursor()
        if self.game.START:
            self.game.playing = True
            self.game.option = False
        if self.game.ADDM:
            self.game.playing = False
            self.game.add = True
            self.game.sub = False
            self.game.count = False
        if self.game.SUBM:
            self.game.playing = False
            self.game.add = False
            self.game.sub = True
            self.game.count = False
        if self.game.COUNTM:
            self.game.playing = False
            self.game.add = False
            self.game.sub = False
            self.game.count = True
        elif self.game.OPTION:
            self.game.option = True
            self.game.playing = False
        elif self.state == 'Quit':
            self.game.playing = False
        elif self.game.SAD:
            self.game.sads = True
        self.run_display = False




    #def check_input(self)

