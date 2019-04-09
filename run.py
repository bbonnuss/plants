# Import ========================= Import ========================= Import
import pygame
import sys
from os.path import join

# Function ======================= Function ======================= Function


# Class ========================== Class ========================== Class
class Scene():
    def __init__():
        self.inprocess = True
        self.click_pos = pygame.mouse.get_pos()
        self.blackground = None


class Main_menu(Scene):
    Scene.__init__(self)


class Shop_menu(Scene):
    Scene.__init__(self)


class Storage_menu(Scene):
    Scene.__init__(self)


class Achievement(Scene):
    Scene.__init__(self)


class 

# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (720,480) # ED
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