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
    
# newgame
class Newgame_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        while True:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

# loadgame
class Load_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        while True:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

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
                    # USING SAVE FUNCTION
                    # save()
                    return "quit"

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
                    # USING SAVE FUNCTION
                    # save()
                    return "quit"

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
                    # USING SAVE FUNCTION
                    # save()
                    return "quit"

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
                    return "quit"

# credit
class Credit_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self):
        self.money = 0
        self.player_farm = None
        self.inventory = Inventory()

class Inventory(self):
    def __init__(self):
        # ผัก
        self.wheat = 0
        self.wheat_seed = 0
        self.cucumber = 0
        self.cucumber_seed = 0
        self.tomato = 0
        self.tomato_seed = 0
        self.potato = 0
        self.potato_seed = 0
        self.purplecabbage = 0
        self.purplecabbage_seed = 0
        # ผลไม้
        self.orange = 0
        self.orange_seed = 0
        self.mango = 0
        self.mango_seed = 0
        self.apple = 0
        self.apple_seed = 0
        self.melon = 0
        self.melon_seed = 0
        self.grape = 0
        self.grape_seed = 0
        # แปรรูป
        self.wheat_processed = 0
        self.cucumber_processed = 0
        self.tomato_processed = 0
        self.potato_processed = 0
        self.purplecabbage_processed = 0
        
        self.orange_processed = 0
        self.mango_processed = 0
        self.apple_processed = 0
        self.melon_processed = 0
        self.grape_processed = 0

class Farmland():
    def __init__(self):
        self.size = 4

        
class Plant():
    def __init__(self):
        self.type = None

class 
# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (720,480)
game_window = pygame.display.set_mode(resolution)
game_name = "Cute, Ginger, Cat-ting Stealing  Vegetables"
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing Vegetables")


game_window.fill((255,255,255))
pygame.display.update()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():

    selected = "main_menu"
    clock = pygame.time.Clock()
    run = True
    while run:
        # fps 
        clock.tick(30)
        
        # Exit game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Main_menu -------------- Main_menu
        

        
        # selection
        if selected == "new_game":
            new_game = Newgame_menu()
            selected = new_game.run()

        if selected == "continue":
            load_menu = Load_menu()
            selected = load_menu.run()

        if selected == "credit":
            credit = Credit_menu()
            selected = credit.run()

        if selected == "quit":
            run = False




        
# RUN !
main()
pygame.quit()
