# Import ========================= Import ========================= Import
import pygame
import sys
from os.path import join

# Function ======================= Function ======================= Function


# Class ========================== Class ========================== Class
# resouce_manager ---------------- resouce_manager
class Sound():
    def __init__(self):
        self.main_theme = None

class Image():
    def __init__(self):
        self.main_bg = None
        
        
# Menu --------------------------- Menu
class Scene():
    def __init__(self):
        self.inprocess = True
        self.click_pos = pygame.mouse.get_pos()

# main menu
class Main_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
    
# newgame
class newgame_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        while True:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

# loadgame
class Load_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        while True:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

# shop
class Shop_menu(Scene):
    def __init__(self):
        Scene.__init__(self)

    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

# คลัง
class Storage_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

# Achievement
class Achievement_manu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

# แปรรูป
class Process_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self):
        self.money = 0
        self.player_farm = None

class Farmland():
    def __init__(self):
        self.size = 4
        
class Plant():
    def __init__(self):
        self.type = None

# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (720,480)
game_window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing  Vegetables ")

# Menu Page=
#bg = pygame.image.load(os.path.join('Game', 'bg.png'))
game_window.fill((255,255,255))
pygame.display.update()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():

    selected = "main_menu"
    clock = pygame.time.Clock()
    run = True
    while run:
        print ('main')
        # fps 
        clock.tick(30)
        
        # Exit game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        
        # selection
        if selected == "main_menu":
            main_menu = Main_menu()
            main_menu.run()

        if selected == "new_game":
            new_game = Newgame_menu
            new_game.run()

        if selected == "continue":
            load_menu = Load_menu()
            load_menu.run()

        if selected == "credit":
            credit = None
            credit.run()

        if selected == "exit":
            run = False




        
# RUN !
main()
pygame.quit()
