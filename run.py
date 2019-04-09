# Import ========================= Import ========================= Import
import pygame
import sys
from os.path import join

# Function ======================= Function ======================= Function


# Class ========================== Class ========================== Class
# Menu --------------------------- Menu
class Scene():
    def __init__():
        self.inprocess = True
        self.click_pos = pygame.mouse.get_pos()
        self.blackground = None
        self.theme_song = None

# main menu
class Main_menu(Scene):
    Scene.__init__(self)

# shop
class Shop_menu(Scene):
    Scene.__init__(self)

# คลัง
class Storage_menu(Scene):
    Scene.__init__(self)

# Achievement
class Achievement_manu(Scene):
    Scene.__init__(self)

# แปรรูป
class Process_menu(Scene):


# Player ------------------------- Menu
class Player():
    def __init__(self):
        self.money = 0
        self.player_farm = None

class Farmland():
    def __init__():
        self.size = 4
        
# mechanic class
class Plant():
    def __init__(self):
        self.

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

    while True:
        # Exit game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # MainMenu
        pygame.image.load(join("File","main_menu_blackground.png")).convert_alpha()
        pygame.display.update()
        # control

        

main()