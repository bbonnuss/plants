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
class Sound_():
    def __init__(self):
        self.main_theme = None
        self.change_page = pygame.mixer.Sound(join('assets','sound','change_page.wav'))
        self.click = pygame.mixer.Sound(join('assets','sound','change_page.wav'))

class Image_():
    def __init__(self):
        self.main_bg = pygame.image.load(join('assets','image','stupid_bg.png')).convert()
        self.farm_bg = pygame.image.load(join('assets','image','farm_bg.png')).convert()
        

# Menu --------------------------- Menu
# หน้าฟาร์มของผู้เล่น
class Player_farm():
    def __init__(self):
        self.player = Player()
        self.inv = self.player.inventory.get_inv()
        self.money = self.player.money
        self.farmland = self.player.farmland

        self.shop_button = ((430, 20),(580,140))
        self.storage_button = ((35,320),(90,385))
        self.watering_button = ((35,205),(90,270))
        self.mainmenu_button = ((390,500),(480,570))
        self.save_button = ((0,0),(0,0))
        self.saveexit_button = ((0,0),(0,0))
        
        self.farmland_position = [[(145,180),(310,300)],    # ซ้ายบน
                                [(520,170),(690,290)],      # ขวาบน
                                [(160,180),(340,480)],      # ล่างซ้าย
                                [(540,360),(690,470)]]      # ล่างขวา
        
    
    def run(self):
        print ('Runing at Player_farm')

        # loop per second 
        clock = pygame.time.Clock()

        run = True
        while run:

            self.draw_bg()

            # loop per second 
            clock.tick(30)
        
            # input - output
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'

                # Botton ------------------------- Botton
                mouse_pos = pygame.mouse.get_pos()
                print( mouse_pos)

                # ปุ่ม ออกไป main_menu]
                if is_hit_box(mouse_pos,self.mainmenu_button[0], self.mainmenu_button[1]):
                    print ('Player_farm : main_menu')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        return 'main'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม รดน้ำ 
                if is_hit_box(mouse_pos,self.watering_button[0], self.watering_button[1]):
                    print ('Player_farm : watering')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        # รดน้ำอ่ะ (คาดว่าจะสร้างเป็น method ขึ้นมาหลังจากกดปุ่ม)
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()
                
                # ปุ่ม คลัง
                if is_hit_box(mouse_pos,self.storage_button[0], self.storage_button[1]):
                    print ('Player_farm : storage')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        storage = Storage_menu(self.inv, self.money)
                        self.inv, self.money = storage.run()
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()
                
                # ปุ่ม ร้านค้า
                if is_hit_box(mouse_pos,self.shop_button[0], self.shop_button[1]):
                    print ('Player_farm : shop')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        shop = Shop_menu(self.inv, self.money)
                        self.inv, self.money = shop.run()
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()
    
    def watering(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return self.inv, self.money
                
                # click to watering
                mouse_pos = pygame.mouse.get_pos()


    def button(self):
        
        pass
    
    def draw_bg(self):
        # background 
        window.blit(Image_().farm_bg, (0, 0))

        # ปุ่มรดน้ำ
        pygame.draw.rect(window, (0,0,150),[35, 205, 55, 65], 3)
        # ปุ่มยุ้งฉาง
        pygame.draw.rect(window, (150,0,150),[35, 320, 55, 65], 3)
        # ปุ่มร้านค้า
        pygame.draw.rect(window, (0,150,150),[430, 20, 150, 120], 3)
        # ปุ่มออกเกม
        pygame.draw.rect(window, (150,150,0),[390,500, 90, 70], 3)

        pygame.display.update()

# shop
class Shop_menu():
    def __init__(self,inventory, money):
        self.inventory = inventory
        self.money = money

    def run(self):
        window.fill((0,0,0))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return self.inventory, self.money
        
        # คืนค่า self.inventory, self.money เมื่อผู้เล่นออกจากร้านด้วย
        return self.inventory, self.money

# คลัง
class Storage_menu():
    def __init__(self,inventory, money):
        self.inventory = inventory
        self.money = money

    def run(self):
        window.fill((255,255,255))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                   return self.inventory, self.money

        # คืนค่า self.inventory, self.money เมื่อผู้เล่นออกจากคลังด้วย
        return self.inventory, self.money

# แปรรูป
class Process_menu():
    def __init__(self,inventory, money):
        self.inventory = inventory
        self.money = money
    
    def run(self):
        window.fill((255,255,255))
        pygame.display.update()
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.inventory, self.money
        
        # คืนค่า self.inventory, self.money เมื่อผู้เล่นออกจากหน้าแปรรูปด้วย
        return self.inventory, self.money

# Achievement
class Achievement_manu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                
# main menu
class Main_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        print ('Runing at Main_menu')
        
        # loop per second 
        clock = pygame.time.Clock()
        run = True
        while run:
            # drawing page ------------------- drawing page
            # background 
            window.blit(Image_().main_bg, (0, 0))

            # newgame botton
            pygame.draw.rect(window, (150,0,150),[220, 100, 380, 100], 3)
            # continue botton
            pygame.draw.rect(window, (0,150,150),[220, 200, 380, 100], 3)
            # credit botton
            pygame.draw.rect(window, (150,150,0),[220, 300, 380, 100], 3)
            # exit botton
            pygame.draw.rect(window, (150,0,0),[220, 400, 380, 100], 3)

            pygame.display.update()

            # loop per second 
            clock.tick(30)
        
            # input - output
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'

                # Botton ------------------------- Botton
                mouse_pos = pygame.mouse.get_pos()

                # ปุ่ม newgame
                newgame_a = (220,100)
                newgame_b = (500,200)
                if is_hit_box(mouse_pos,newgame_a, newgame_b):
                    print ('Main_menu : newgame')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        return 'newgame'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม continue
                continue_a = (220,200)
                continue_b = (500,300)
                if is_hit_box(mouse_pos,continue_a, continue_b):
                    print ('Main_menu : continue')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        return 'load'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม credit
                credit_a = (220,300)
                credit_b = (500,400)
                if is_hit_box(mouse_pos,credit_a, credit_b):
                    print ('Main_menu : credit')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        return 'credit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม exit
                quit_a = (220,400)
                quit_b = (500,500)
                if is_hit_box(mouse_pos,quit_a, quit_b):
                    print ('Main_menu : exit')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        Sound_().click.play()
                        return 'exit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

# newgame
class Newgame_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        print ('Runing at Newgame_menu')
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
                
            return 'player_farm'
    
# loadgame
class Load_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        print ('Runing at Load_menu')
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
    
            return 'player_farm'

# credit
class Credit_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        print ('Runing at Credit_menu')
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.MOUSEBUTTONUP:
                    return 'main'


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self):
        self.money = 0
        self.inventory = Inventory()
        self.farmland = None

class Inventory():
    def __init__(self):
        self.inventory = {'wheat': 0, 'wheat_seed': 0, 
                    'cucumber': 0, 'cucumber_seed': 0, 
                    'tomato': 0, 'tomato_seed': 0,
                    'potato': 0,  'potato_seed': 0,
                    'orange': 0, 'orange_seed': 0,
                    'mango': 0, 'mango_seed': 0,
                    'apple': 0, 'apple_seed': 0, 
                    'melon': 0, 'melon_seed': 0, 
                    'grape': 0, 'grape_seed': 0,
                    'pug_process': 0,'fruit_process': 0 }
    
    # add item to Inventory
    def add(self, name, amout):
        self.inventory[name] += amout
    
    # remove item from Inventory
    def remove(self, name, amout):
        self.inventory[name] -= amout
    
    def get_inv(self):
        return self.inventory
    
    # get Inventory (dict type) อันนี้ให้ใช้กับ storage เพื่อแสดงผล
    def get_inv_only_have(self):
        item_name = list(filter(lambda x : self.inventory[x] > 0, self.inventory))
        inv = dict()
        for key in item_name:
            inv[key] = self.inventory[key]
        return inv


# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing Vegetables")


window.fill((255,255,255))
pygame.display.update()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():
    print ('Runing at Main()')
    selected = 'main'
    run = True
    while run:
        if selected == 'main':
            main = Main_menu()
            selected = main.run()
        
        if selected == 'newgame':
            newgame = Newgame_menu()
            selected = newgame.run()
        
        if selected == 'load':
            load = Load_menu()
            selected = load.run()
        
        if selected == 'credit':
            credit = Credit_menu()
            selected = credit.run()
        
        if selected == 'player_farm':
            player_farm = Player_farm()
            selected = player_farm.run()
        
        if selected == 'acheivement':
            acheivement = Achievement_manu()
            selected = acheivement.run()

        if selected == 'exit':
            run = False
            
        

# RUN !
main()

# EXIT !
pygame.quit()
