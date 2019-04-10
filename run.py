# Import ========================= Import ========================= Import
import pygame
import sys
from os.path import join

# Function ======================= Function ======================= Function
# เช็คว่าตำแหน่งเมาส์ โดนปุ่มไหม
def is_hit_box(position,box_a,box_b):
    # position คือ ตำแหน่งเมาส์ (tuple 2 element)(จุด x,y)
    # box_a คือ จุดมุมซ้ายบนของปุ่ม (tuple 2 element)(จุด x,y)
    # box_b คือ จุดมุมขวาล่างของปุ่ม (tuple 2 element)(จุด x,y)

    if box_a[0] < position[0] < box_b[0] : # ถ้า x อยู่ระหว่างนั้น
        if box_a[1] < position[1] < box_b[1] :
            return True
    
    return False


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
        
# shop
class Shop_menu(Scene):
    def __init__(self):
        Scene.__init__(self)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    # USING SAVE FUNCTION
                    # save():
                    return not run
                
        return run

# คลัง
class Storage_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    # USING SAVE FUNCTION
                    # save():
                    return not run
                
        return run

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
                    return not run
        return run

# Achievement
class Achievement_manu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run
                
        return run

# newgame
class Newgame_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run
                
        return run
    
# loadgame
class Load_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run

        return run

# credit
class Credit_menu(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run
                
        return run


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self):
        self.money = 0
        self.player_farm = None
        self.inventory = Inventory()

class Inventory():
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


# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
game_window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing Vegetables")


game_window.fill((255,255,255))
pygame.display.update()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        # loop per second 
        clock.tick(30)
        
        # Exit game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Main_menu -------------- Main_menu
            mouse_pos = pygame.mouse.get_pos()
            #print (mouse_pos)
            #print (event)

            # ปุ่ม newgame
            newgame_a = (220,100)
            newgame_b = (500,200)
            if is_hit_box(mouse_pos,newgame_a, newgame_b):
                print ('Main_menu : Newgame')
                # เรืองแสง (ถ้าว่างค่อยทำ)
                growing = None

                if event.type == pygame.MOUSEBUTTONUP:
                    new_game = Newgame_menu()
                    run = new_game.run()

            # ปุ่ม continue
            continue_a = (220,200)
            continue_b = (500,300)
            if is_hit_box(mouse_pos,continue_a, continue_b):
                print ('Main_menu  : Continue')
                # เรืองแสง (ถ้าว่างค่อยทำ)
                growing = None

                if event.type == pygame.MOUSEBUTTONUP:
                    load_menu = Load_menu()
                    run = load_menu.run()

            # ปุ่ม credit
            credit_a = (220,300)
            credit_b = (500,400)
            if is_hit_box(mouse_pos,credit_a, credit_b):
                print ('Main_menu  : Credit')
                # เรืองแสง (ถ้าว่างค่อยทำ)
                growing = None

                if event.type == pygame.MOUSEBUTTONUP:
                    credit = Credit_menu()
                    run = credit.run()

            # ปุ่ม exit
            quit_a = (220,400)
            quit_b = (500,500)
            if is_hit_box(mouse_pos,quit_a, quit_b):
                print ('Main_menu  : Exit')
                # เรืองแสง (ถ้าว่างค่อยทำ)
                growing = None

                if event.type == pygame.MOUSEBUTTONUP:
                    run = False




        
# RUN !
main()
pygame.quit()
