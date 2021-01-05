import pygame
from menu import MainMenu
from menu import Menu
import ctypes
import random
from pygame import mixer


class Game():
    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running, self.playing, self.option, self.SAD = True, False, False, False
        self.add, self.sub, self.count, self.sads = False, False, False, False
        self.UP_KEY, self.OPTION, self.START, self.BACK, self.SAD = False, False, False, False, False
        self.ADDM, self.SUBM, self.COUNTM = False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.FULLSCREEN)
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.DARK = (0,0, 0), (255, 255, 255), (245, 245, 245)
        self.curr_menu = MainMenu(self)
        self.image = pygame.image.load('Menu3.jpg').convert()
        self.size = (self.DISPLAY_W, self.DISPLAY_H)
        self.surface = pygame.Surface(self.size)
        self.image = pygame.transform.scale(self.image, (self.DISPLAY_W, self.DISPLAY_H), self.surface)
        self.dis = Menu(self)
        self.mouse = pygame.mouse.get_pos()
        self.stored_volume = []
        self.stored_curr_volume = []
        self.addimage = pygame.image.load('add_background.jpg').convert()
        self.addimage = pygame.transform.scale(self.addimage, (self.DISPLAY_W, self.DISPLAY_H))

        self.subimage = pygame.image.load('sub_background.jpg').convert()
        self.subimage = pygame.transform.scale(self.subimage, (self.DISPLAY_W, self.DISPLAY_H))

        self.catimage = pygame.image.load('Cyat.png')
        self.catimage = pygame.transform.scale(self.catimage, (250,250))
        self.x, self.y = self.window.get_size()
        self.score = 0

        self.apple = pygame.image.load('apple.png')
        self.apple = pygame.transform.scale(self.apple, (60,60))

        # set icon, title of game
        icon = pygame.image.load("cat_icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Kitten Math")

        self.sad_pic = pygame.image.load("sad.jpg").convert()
        self.sad_pic = pygame.transform.scale(self.sad_pic, (self.DISPLAY_W, self.DISPLAY_H))

        self.count_pic = pygame.image.load('count.jpg').convert()
        self.count_pic = pygame.transform.scale(self.count_pic, (self.DISPLAY_W, self.DISPLAY_H))

        # initialize music
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Survive the Fall.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)


    def game_loop(self):
        #print(f"{self.x}. {self.y}")
        while self.playing:
            self.check_events()
            self.curr_menu.check_input()
            if self.BACK:
                self.playing = False
            self.display.fill(self.BLACK)
            text1 = self.dis.create_text("Addition")
            text2 = self.dis.create_text("Subtraction")
            text3 = self.dis.create_text("Count")
            text4 = self.dis.create_text("Back")
            text5 = self.dis.create_text("Game Menu")
            self.window.blit(self.image, (0,0))
            self.mouse = pygame.mouse.get_pos()
            if 782 <= self.mouse[0] <= 1137 and 600 <= self.mouse[1] <= 669:
                self.dis.renderText(text1, self.DISPLAY_W, self.DISPLAY_H + 200, self.WHITE, 100)
            else:
                self.dis.renderText(text1, self.DISPLAY_W, self.DISPLAY_H + 200, self.DARK, 100)

            if 690 <= self.mouse[0] <= 1128 and 699 <= self.mouse[1] <= 769:
                self.dis.renderText(text2, self.DISPLAY_W, self.DISPLAY_H + 400, self.WHITE, 100)
            else:
                self.dis.renderText(text2, self.DISPLAY_W, self.DISPLAY_H + 400, self.DARK, 100)

            if 828 <= self.mouse[0] <= 1091 and 803 <= self.mouse[1] <= 871:
                self.dis.renderText(text3, self.DISPLAY_W, self.DISPLAY_H + 600, self.WHITE, 100)
            else:
                self.dis.renderText(text3, self.DISPLAY_W, self.DISPLAY_H + 600, self.DARK, 100)
            self.dis.renderText(text4, 575, 295, self.WHITE, 70)
            self.dis.renderText(text5, self.DISPLAY_W, self.DISPLAY_H - 100, self.WHITE, 100)
            pygame.display.flip()
            self.clock.tick(60)
            print(self.mouse)
            self.reset_keys()



    def option_loop(self):
        if not self.stored_volume:
            self.stored_volume.insert(0, 50)

        if not self.stored_curr_volume:
            self.stored_curr_volume.insert(0, 0.5)

        volume = int(self.stored_volume[0])  # human readable volume

        while self.option:
            print(self.mouse)
            self.check_events()
            self.curr_menu.check_input()
            if self.BACK:
                self.option = False
            self.display.fill(self.BLACK)
            volume_txt = self.dis.create_text("Volume: " + str(volume))
            back_txt = self.dis.create_text("Back")
            volume_plus = self.dis.create_text("+")
            volume_minus = self.dis.create_text("-")
            self.window.blit(self.image, (0, 0))
            """ all volume options are here """
            self.mouse = pygame.mouse.get_pos()
            self.dis.renderText(volume_txt, self.DISPLAY_W - 500, self.DISPLAY_H, self.WHITE, 50)
            if 900 <= self.mouse[0] <= 1000 and 500 <= self.mouse[1] <= 560:
                self.dis.renderText(volume_minus, self.DISPLAY_W, self.DISPLAY_H, self.WHITE, 50)
            else:
                self.dis.renderText(volume_minus, self.DISPLAY_W, self.DISPLAY_H, self.DARK, 50)

            if 1180 <= self.mouse[0] <= 1250 and 500 <= self.mouse[1] <= 560:
                self.dis.renderText(volume_plus, self.DISPLAY_W + 500, self.DISPLAY_H, self.WHITE, 50)
            else:
                self.dis.renderText(volume_plus, self.DISPLAY_W + 500, self.DISPLAY_H, self.DARK, 50)
            self.dis.renderText(back_txt, 575, 295, self.WHITE, 50)
            pygame.display.flip()
            self.clock.tick(60)
            self.reset_keys()
            """ testing local event scope for option_loop """
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # min button
                    if 198 <= self.mouse[0] <= 392 and 105 <= self.mouse[1] <= 180 and self.option:
                        self.option = False
                    if 900 <= self.mouse[0] <= 1000 and 500 <= self.mouse[1] <= 560:
                        if volume > 0:
                            volume -= 5
                        else:
                            volume = 0
                        self.stored_volume[0] = volume
                        curr_volume = volume / 1000
                        pygame.mixer.music.set_volume(curr_volume)
                        self.stored_curr_volume[0] = curr_volume

                    # plus button
                    if 1180 <= self.mouse[0] <= 1250 and 500 <= self.mouse[1] <= 560:
                        if volume < 100:
                            volume += 5
                        else:
                            volume = 100
                        print(volume)
                        self.stored_volume[0] = volume
                        curr_volume = volume / 1000
                        pygame.mixer.music.set_volume(curr_volume)
                        self.stored_curr_volume[0] = curr_volume





    def add_loop(self):
        lives = 3
        tries = 2
        scores = 0
        hot_streak = 0
        answer = 0
        rand1 = random.randint(1, 5)
        rand2 = random.randint(1, 5)
        total = rand1 + rand2
        correct = False

        if self.add:
            self.display.fill(self.BLACK)
            self.window.blit(self.addimage, (0, 0))
            self.display_left_kittens(rand1)
            self.display_right_kittens(rand2)
            text8 = self.dis.create_text("Tries:[   ]")
            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)

        while self.add:
            self.mouse = pygame.mouse.get_pos()
            print(self.mouse)
            self.check_events()
            self.curr_menu.check_input()
            self.live_add(lives)
            text8 = self.dis.create_text("Tries:[   ]")
            if self.BACK:
                self.add = False
                self.playing = True
            text4 = self.dis.create_text("<-Back")
            text5 = self.dis.create_text("ADD")
            text6 = self.dis.create_text("SUBMIT")
            text7 = self.dis.create_text("REMOVE")
            if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                self.dis.renderText(text4, 200, 60, self.WHITE, 70)
            else:
                self.dis.renderText(text4, 200, 60, self.DARK, 70)
            if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text5, 3000, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text5, 3000, 1580, self.DARK, 70)
            if 770 <= self.mouse[0] <= 1068 and 798 <= self.mouse[1] <= 849:
                self.dis.renderText(text6, 1840, 1650, self.WHITE, 70)
            else:
                self.dis.renderText(text6, 1840, 1650, self.DARK, 70)
            if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text7, 3550, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text7, 3550, 1580, self.DARK, 70)
            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
            self.dis.renderText(str(tries), 3675, 200, self.WHITE, 70)
            self.reset_keys()
            pygame.display.flip()
            self.clock.tick(60)
            self.mouse = pygame.mouse.get_pos()
            if lives != 0:
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                            scores = 0
                            self.score = scores
                            correct = False
                            if tries < 2:
                                tries = 2
                            answer = 0
                            lives = 3
                            hot_streak = 0
                            self.add = False
                            self.playing = True
                        if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                            if answer < 10:
                                answer += 1
                            self.addition_reset(answer)
                            self.display_left_kittens(rand1)
                            self.display_right_kittens(rand2)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                            if answer > 0:
                                answer -= 1
                            self.addition_reset(answer)
                            self.display_left_kittens(rand1)
                            self.display_right_kittens(rand2)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 770  <= self.mouse[0] <= 1068 and 798  <= self.mouse[1] <= 849:
                            if answer == total:
                                correct = True
                                if hot_streak < 5:
                                    scores+=10
                                    self.score = scores
                                    hot_streak += 1
                                elif hot_streak >= 5:
                                    scores += 20
                                    self.score = scores
                                yay = mixer.Sound('coin sound.mp3')
                                yay.set_volume(self.stored_curr_volume[0])
                                yay.play()
                            elif answer != total:
                                tries -= 1
                                self.window.blit(self.addimage, (0, 0))
                                self.display_left_kittens(rand1)
                                self.display_right_kittens(rand2)
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                                if tries == 0:
                                    lives -= 1
                                hot_streak = 0
                                oof = mixer.Sound('oof.mp3')
                                oof.set_volume(self.stored_curr_volume[0])
                                oof.play()
                            if tries == 0 or correct:
                                correct = False
                                tries = 2
                                answer = 0
                                rand1 = random.randint(1, 5)  # generate new left hand side number
                                rand2 = random.randint(1, 5)  # generate new right hand side number
                                total = rand1 + rand2
                                self.addition_reset(answer)
                                self.display_left_kittens(rand1)
                                self.display_right_kittens(rand2)
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
            elif lives == 0:
                self.sads = True
                self.add = False
                temp = self.sad_cat()
                if temp:
                    self.add = True
                    self.sads = False
                    lives = 3
                    correct = False
                    tries = 2
                    answer = 0
                    self.score = 0
                    scores = 0
                    rand1 = random.randint(1, 5)  # generate new left hand side number
                    rand2 = random.randint(1, 5)  # generate new right hand side number
                    total = rand1 + rand2
                    self.addition_reset(answer)
                    self.display_left_kittens(rand1)
                    self.display_right_kittens(rand2)
                    self.dis.renderText(text8, 3500, 200, self.WHITE, 70)



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 693 <= self.mouse[0] <= 1223 and 600 <= self.mouse[1] <= 672 and not self.playing: 
                    self.START = True
                    pygame.display.flip()

                if 782 <= self.mouse[0] <= 1137 and 600 <= self.mouse[1] <= 669 and self.playing:
                    self.ADDM = True

                if 690 <= self.mouse[0] <= 1128 and 699 <= self.mouse[1] <= 769 and self.playing:
                    self.SUBM = True

                if 828 <= self.mouse[0] <= 1091 and 803 <= self.mouse[1] <= 871 and self.playing:
                    self.COUNTM = True

                if 198 <= self.mouse[0] <= 392 and 105 <= self.mouse[1] <= 180 and self.playing:
                    self.BACK = True

                elif 198 <= self.mouse[0] <= 392 and 105 <= self.mouse[1] <= 180 and self.option:
                    self.BACK = True

                elif 27 <= self.mouse[0] <= 172 and 1  <= self.mouse[1] <= 52 and self.add:
                    self.BACK = True

                if 861 <= self.mouse[0] <= 1057 and 803 <= self.mouse[1] <= 871 and self.playing:
                    pass

                elif 861 <= self.mouse[0] <= 1057 and 803 <= self.mouse[1] <= 871 and not self.playing:
                    self.running, self.playing = False, False

                if 818 <= self.mouse[0] <= 1103 and 700 <= self.mouse[1] <= 793 and not self.playing:
                    self.OPTION = True

            self.mouse = pygame.mouse.get_pos()


    def reset_keys(self):
        self.UP_KEY, self.OPTION, self.START, self.BACK, self.SAD = False, False, False, False, False
        self.ADDM, self.SUBM, self.COUNTM = False, False, False

    def display_right_kittens(self, num):
        for i in range(num):
            if i < 5:
                self.window.blit(self.catimage, [710, 110 + 120 * i])
            else:
                self.window.blit(self.catimage, [910, 110 + 120 * (i % 5)])

    def display_left_kittens(self, num):
        for i in range(num):
            if i < 5:
                self.window.blit(self.catimage, [125, 110 + 120 * i])

            else:
                self.window.blit(self.catimage, [280, 110 + 120 * (i % 5)])

    def addition_reset(self, answer):
        self.window.blit(self.addimage, (0, 0))
        for i in range(answer):
            if i < 5:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 530, 110 + 120 * i])

            elif 5 <= i < 10:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 390, 110 + 120 * (i % 5)])
            """elif 10 <= i < 15:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 300, 110 + 120 * (i % 5)])

            else:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 225, 110 + 120 * (i % 5)])"""

    def sub_loop(self):
        lives = 3
        tries = 2
        scores = 0
        hot_streak = 0
        answer = 0
        rand1 = random.randint(1, 10)
        rand2 = random.randint(1, 10)
        while rand1 < rand2 and rand1 - rand2 != 0:
            rand1 = random.randint(1, 10)
            rand2 = random.randint(1, 10)
        total = rand1 - rand2
        correct = False

        if self.sub:
            self.display.fill(self.BLACK)
            self.window.blit(self.subimage, (0, 0))
            self.display_left_kittens(rand1)
            self.display_right_kittens(rand2)
            text8 = self.dis.create_text("Tries:[   ]")
            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)

        while self.sub:
            self.mouse = pygame.mouse.get_pos()
            print(self.mouse)
            self.check_events()
            self.curr_menu.check_input()
            self.live_add(lives)

            if self.BACK:
                self.sub = False
                self.playing = True
            text8 = self.dis.create_text("Tries:[   ]")
            text4 = self.dis.create_text("<-Back")
            text5 = self.dis.create_text("ADD")
            text6 = self.dis.create_text("SUBMIT")
            text7 = self.dis.create_text("REMOVE")

            if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                self.dis.renderText(text4, 200, 60, self.WHITE, 70)
            else:
                self.dis.renderText(text4, 200, 60, self.DARK, 70)
            if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text5, 3000, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text5, 3000, 1580, self.DARK, 70)
            if 770 <= self.mouse[0] <= 1068 and 798 <= self.mouse[1] <= 849:
                self.dis.renderText(text6, 1840, 1650, self.WHITE, 70)
            else:
                self.dis.renderText(text6, 1840, 1650, self.DARK, 70)
            if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text7, 3550, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text7, 3550, 1580, self.DARK, 70)
            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
            self.dis.renderText(str(tries), 3675, 200, self.WHITE, 70)
            self.reset_keys()
            pygame.display.flip()
            self.clock.tick(60)
            self.mouse = pygame.mouse.get_pos()
            if lives != 0:
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                            scores = 0
                            self.score = scores
                            correct = False
                            tries = 2
                            answer = 0
                            lives = 3
                            hot_streak = 0
                            self.BACK = True
                        if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                            if answer < 10:
                                answer += 1
                            self.sub_reset(answer)
                            self.display_left_kittens(rand1)
                            self.display_right_kittens(rand2)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                            if answer > 0:
                                answer -= 1
                            self.sub_reset(answer)
                            self.display_left_kittens(rand1)
                            self.display_right_kittens(rand2)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 770 <= self.mouse[0] <= 1068 and 798 <= self.mouse[1] <= 849:
                            if answer == total:
                                correct = True
                                if hot_streak < 5:
                                    scores += 10
                                    self.score = scores
                                    hot_streak += 1
                                elif hot_streak >= 5:
                                    scores += 20
                                    self.score = scores
                                yay = mixer.Sound('coin sound.mp3')
                                yay.set_volume(self.stored_curr_volume[0])
                                yay.play()
                            elif answer != total:
                                tries -= 1
                                self.window.blit(self.subimage, (0, 0))
                                self.display_left_kittens(rand1)
                                self.display_right_kittens(rand2)
                                text8 = self.dis.create_text("Tries:[   ]")
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                                if tries == 0:
                                    lives -= 1
                                hot_streak = 0
                                oof = mixer.Sound('oof.mp3')
                                oof.set_volume(self.stored_curr_volume[0])
                                oof.play()
                            if tries == 0 or correct:
                                correct = False
                                tries = 2
                                answer = 0
                                rand1 = random.randint(1, 10)  # generate new left hand side number
                                rand2 = random.randint(1, 10)  # generate new right hand side number
                                while rand1 < rand2 and rand1 - rand2 != 0:
                                    rand1 = random.randint(1, 10)
                                    rand2 = random.randint(1, 10)
                                total = rand1 - rand2
                                self.sub_reset(answer)
                                self.display_left_kittens(rand1)
                                self.display_right_kittens(rand2)
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
            elif lives == 0:
                self.sads = True
                self.sub = False
                temp = self.sad_cat()
                if temp:
                    self.sub = True
                    self.sads = False
                    self.score = 0
                    scores = 0
                    lives = 3
                    correct = False
                    tries = 2
                    answer = 0
                    rand1 = random.randint(1, 10)  # generate new left hand side number
                    rand2 = random.randint(1, 10)  # generate new right hand side number
                    while rand1 < rand2 and rand1 - rand2 != 0:
                        rand1 = random.randint(1, 10)
                        rand2 = random.randint(1, 10)
                    total = rand1 - rand2
                    self.sub_reset(answer)
                    self.display_left_kittens(rand1)
                    self.display_right_kittens(rand2)
                    self.dis.renderText(text8, 3500, 200, self.WHITE, 70)



    def sub_reset(self, answer):
        self.window.blit(self.subimage, (0, 0))
        for i in range(answer):
            if i < 5:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 530, 110 + 120 * i])

            elif 5 <= i < 10:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 390, 110 + 120 * (i % 5)])
            """elif 10 <= i < 15:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 370, 125 + 120 * (i % 5)])

            else:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 285, 125 + 120 * (i % 5)])"""

    def live_add(self, lives):
        for i in range(lives):
            self.window.blit(self.apple, [1600 + 120 * i, self.DISPLAY_H - 1060])


    def sad_cat(self):
        while self.sads:
            if self.BACK:
                self.sads = False
                self.playing = True
                return False
            self.mouse = pygame.mouse.get_pos()
            print(self.mouse)
            self.check_events()
            self.curr_menu.check_input()
            text1 = self.dis.create_text("Try Again")
            text2 = self.dis.create_text("Game Menu")
            text3 = self.dis.create_text("The game is over. Great Effort!")
            self.window.blit(self.sad_pic, (0,0))
            self.dis.renderText(text3, self.DISPLAY_W / 2 + 850, self.DISPLAY_H / 2 - 90, self.WHITE, 120)
            if 1234 <= self.mouse[0] <= 1728 and 675 <= self.mouse[1] <= 786:
                self.dis.renderText(text1, self.DISPLAY_W / 2 + 2000, self.DISPLAY_H / 2 + 900, self.WHITE, 120)
            else:
                self.dis.renderText(text1, self.DISPLAY_W / 2 + 2000, self.DISPLAY_H / 2 + 900, self.DARK, 120)
            if 15 <= self.mouse[0] <= 582 and 675 <= self.mouse[1] <= 756:
                self.dis.renderText(text2, 600, self.DISPLAY_H / 2 + 900, self.WHITE, 120)
            else:
                self.dis.renderText(text2, 600, self.DISPLAY_H / 2 + 900, self.DARK, 120)
            self.mouse = pygame.mouse.get_pos()
            self.reset_keys()
            pygame.display.flip()
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 15 <= self.mouse[0] <= 583 and 675 <= self.mouse[1] <= 756:
                        self.BACK = True
                    if 1234 <= self.mouse[0] <= 1728 and 675 <= self.mouse[1] <= 786:
                        self.sads = False
                        self.playing = False
                        return True


    def count_loop(self):
        lives = 3
        tries = 2
        scores = 0
        hot_streak = 0
        answer = 0
        rand1 = random.randint(1, 10)
        total = rand1
        correct = False

        if self.count:
            self.display.fill(self.BLACK)
            self.window.blit(self.count_pic, (0, 0))
            self.display_left_kittens(rand1)
            text8 = self.dis.create_text("Tries:[   ]")
            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)


        while self.count:
            self.mouse = pygame.mouse.get_pos()
            print(self.mouse)
            self.check_events()
            self.curr_menu.check_input()
            self.live_add(lives)
            if self.BACK:
                self.count = False
                self.playing = True

            text4 = self.dis.create_text("<-Back")
            text5 = self.dis.create_text("ADD")
            text6 = self.dis.create_text("SUBMIT")
            text7 = self.dis.create_text("REMOVE")

            if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                self.dis.renderText(text4, 200, 60, self.WHITE, 70)
            else:
                self.dis.renderText(text4, 200, 60, self.DARK, 70)
            if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text5, 3000, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text5, 3000, 1580, self.DARK, 70)
            if 770 <= self.mouse[0] <= 1068 and 798 <= self.mouse[1] <= 849:
                self.dis.renderText(text6, 1840, 1650, self.WHITE, 70)
            else:
                self.dis.renderText(text6, 1840, 1650, self.DARK, 70)
            if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                self.dis.renderText(text7, 3550, 1580, self.WHITE, 70)
            else:
                self.dis.renderText(text7, 3550, 1580, self.DARK, 70)
            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
            self.dis.renderText(str(tries), 3675, 200, self.WHITE, 70)
            self.reset_keys()
            pygame.display.flip()
            self.clock.tick(60)
            self.mouse = pygame.mouse.get_pos()
            if lives != 0:
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if 0 <= self.mouse[0] <= 200 and 0 <= self.mouse[1] <= 53:
                            scores = 0
                            self.score = scores
                            correct = False
                            tries = 2
                            answer = 0
                            lives = 3
                            hot_streak = 0
                            self.count = False
                            self.playing = True
                        if 1436 <= self.mouse[0] <= 1563 and 761 <= self.mouse[1] <= 813:
                            if answer < 10:
                                answer += 1
                            self.count_reset(answer)
                            self.display_left_kittens(rand1)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            text8 = self.dis.create_text("Tries:[   ]")
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 1628 <= self.mouse[0] <= 1919 and 761 <= self.mouse[1] <= 813:
                            if answer > 0:
                                answer -= 1
                            self.count_reset(answer)
                            self.display_left_kittens(rand1)
                            self.dis.renderText(str(self.score), 2200, 115, self.WHITE, 70)
                            text8 = self.dis.create_text("Tries:[   ]")
                            self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                        if 770  <= self.mouse[0] <= 1068 and 798  <= self.mouse[1] <= 849:
                            if answer == total:
                                correct = True
                                if hot_streak < 5:
                                    scores+=10
                                    self.score = scores
                                    hot_streak += 1
                                elif hot_streak >= 5:
                                    scores += 20
                                    self.score = scores
                                yay = mixer.Sound('coin sound.mp3')
                                yay.set_volume(self.stored_curr_volume[0])
                                yay.play()
                            elif answer != total:
                                tries -= 1
                                self.window.blit(self.count_pic, (0, 0))
                                self.display_left_kittens(rand1)
                                text8 = self.dis.create_text("Tries:[   ]")
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
                                if tries == 0:
                                    lives -= 1
                                hot_streak = 0
                                oof = mixer.Sound('oof.mp3')
                                oof.set_volume(self.stored_curr_volume[0])
                                oof.play()
                            if tries == 0 or correct:
                                correct = False
                                tries = 2
                                answer = 0
                                rand1 = random.randint(1, 10)  # generate new left hand side number
                                total = rand1
                                self.count_reset(answer)
                                self.display_left_kittens(rand1)
                                text8 = self.dis.create_text("Tries:[   ]")
                                self.dis.renderText(text8, 3500, 200, self.WHITE, 70)
            elif lives == 0:
                self.sads = True
                self.count = False
                temp = self.sad_cat()
                if temp:
                    self.count = True
                    self.sads = False
                    self.score = 0
                    scores = 0
                    lives = 3
                    correct = False
                    tries = 2
                    answer = 0
                    rand1 = random.randint(1, 10)  # generate new left hand side number
                    total = rand1
                    self.count_reset(answer)
                    self.display_left_kittens(rand1)
                    text8 = self.dis.create_text("Tries:[   ]")
                    self.dis.renderText(text8, 3500, 200, self.WHITE, 70)

    def count_reset(self, answer):
        self.window.blit(self.count_pic, (0, 0))
        for i in range(answer):
            if i < 5:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 530, 110 + 120 * i])

            elif 5 <= i < 10:
                kitty = pygame.image.load("Cyat.png")
                kitty = pygame.transform.scale(kitty, (250,250))
                self.window.blit(kitty, [self.DISPLAY_W - 390, 110 + 120 * (i % 5)])
