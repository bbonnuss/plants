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
        # background
        self.main_bg = pygame.image.load(join('assets','image','stupid_bg.png')).convert()
        self.farm_bg = pygame.image.load(join('assets','image','farm_bg.png')).convert()
        
        self.dry_farm = pygame.image.load(join('assets','image','dry_farm.png')).convert()
        self.wet_farm = pygame.image.load(join('assets','image','wet_farm.png')).convert()
        # crops growing state
        self.wheat_state1 = None
        self.wheat_state2 = None
        self.wheat_state3 = None
        self.wheat_state4 = None
        self.cucumber_state1 = None
        self.cucumber_state2 = None
        self.cucumber_state3 = None
        self.cucumber_state4 = None
        self.tomato_state1 = None
        self.tomato_state2 = None
        self.tomato_state3 = None
        self.tomato_state4 = None
        self.potato_state1 = None
        self.potato_state2 = None
        self.potato_state3 = None
        self.potato_state4 = None
        self.redcabbage_state1 = None
        self.redcabbage_state2 = None
        self.redcabbage_state3 = None
        self.redcabbage_state4 = None
        self.orange_state1 = None
        self.orange_state2 = None
        self.orange_state3 = None
        self.orange_state4 = None
        self.mango_state1 = None
        self.mango_state2 = None
        self.mango_state3 = None
        self.mango_state4 = None
        self.apple_state1 = None
        self.apple_state2 = None
        self.apple_state3 = None
        self.apple_state4 = None
        self.melon_state1 = None
        self.melon_state2 = None
        self.melon_state3 = None
        self.melon_state4 = None
        self.grape_state1 = None
        self.grape_state2 = None
        self.grape_state3 = None
        self.grape_state4 = None
        

# Menu --------------------------- Menu
# หน้าฟาร์มของผู้เล่น
class Player_farm():
    def __init__(self):
        self.player = Player()
        self.inv = self.player.inventory.get_inv()
        self.money = self.player.money
        self.farmplot = self.player.farmplot
        self.load_time = 0
        self.time = self.load_time + pygame.time.get_ticks()

        self.shop_button = ((430, 20),(580,140))
        self.storage_button = ((35,320),(90,385))
        self.watering_button = ((35,205),(90,270))
        self.mainmenu_button = ((390,500),(480,570))
        self.save_button = ((0,0),(0,0))
        self.saveexit_button = ((0,0),(0,0))
        
        self.farmplot_position = [[(145,180),(310,300)],    # ซ้ายบน
                                [(520,170),(690,290)],      # ขวาบน
                                [(160,380),(340,480)],      # ล่างซ้าย
                                [(540,360),(690,470)]]      # ล่างขวา
        
    
    def run(self):
        print ('Runing at Player_farm')
        global loaded_image
        global loaded_sound
        # loop per second 
        clock = pygame.time.Clock()

        # clock
        enter_farm_time = pygame.time.get_ticks()

        # วาดพื้นหลัง
        self.draw_bg()
        seeding = False
        watering = False
        run = True
        while run:

            # loop per second 
            clock.tick(40)

            # debuging display
            if seeding:
                print (pygame.mouse.get_pos(),'STATUS = SEEDIGN')
            elif watering:
                #print (pygame.mouse.get_pos(),'STATUS = WATERING')
                pass
            else:
                pass
                #print (pygame.mouse.get_pos(),'STATUS = None')

            # clock update (clock is millisec)
            self.time = self.load_time + (pygame.time.get_ticks() - enter_farm_time)
            
            # set farmland dry again
            plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
            for plot in plot_list:
                stats = self.check_crops_status(plot)
                if stats[2] is not None:
                    if stats[1] and (stats[2] < self.time): # ถ้าฟาร์มชื้น และ เกินเวลาคงเหลือ
                        self.set_dry(plot)
                        self.draw_farmland(plot, False)
                        print (plot, ' Dry !!!!')
            
            # set crops growing to next state

            # growth system

            # input - output
            for event in pygame.event.get():

                # pointer
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    clickup = True
                else:
                    clickup = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # exit
                if event.type == pygame.QUIT:
                    return 'exit'
                
                # Botton ------------------------- Botton
                

                # ปุ่ม ออกไป main_menu]
                if is_hit_box(mouse_pos,self.mainmenu_button[0], self.mainmenu_button[1]):
                    print ('Player_farm : main_menu')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if clickdown:
                        loaded_sound.click.play()
                        return 'main'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม รดน้ำ 
                if is_hit_box(mouse_pos,self.watering_button[0], self.watering_button[1]):
                    print ('Player_farm : watering')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if clickdown:
                        loaded_sound.click.play()
                        watering = not watering
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()
                
                # ปุ่ม คลัง
                if is_hit_box(mouse_pos,self.storage_button[0], self.storage_button[1]):
                    print ('Player_farm : storage')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if clickdown:
                        loaded_sound.click.play()
                        storage = Storage_menu(self.inv, self.money)
                        self.inv, self.money = storage.run()
                        self.draw_bg()
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()
                
                # ปุ่ม ร้านค้า
                if is_hit_box(mouse_pos,self.shop_button[0], self.shop_button[1]):
                    print ('Player_farm : shop')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if clickdown:
                        loaded_sound.click.play()
                        shop = Shop_menu(self.inv, self.money)
                        self.inv, self.money = shop.run()
                        self.draw_bg()
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # farmplot zone ----------------- farmplot zone
                # top left
                if is_hit_box(mouse_pos, self.farmplot_position[0][0], self.farmplot_position[0][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[0], mouse_pos)
                    if clickdown and (index != None) and watering:
                        self.set_wet('1'+str(index))
                        self.draw_farmland('1'+str(index), True)
                        print (self.check_crops_status('1'+str(index)))
                    if clickdown and (index != None) and seeding:
                        self.set_crops('1'+str(index), seed)
                        
                # top right
                if is_hit_box(mouse_pos, self.farmplot_position[1][0], self.farmplot_position[1][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[1], mouse_pos)
                    if clickdown and (index != None):
                        if watering:
                            loaded_sound.click.play()
                            self.set_wet('2'+str(index))
                            self.draw_farmland('2'+str(index), True)
                            print (self.check_crops_status('2'+str(index)))
                        else:
                            print (self.check_crops_status('2'+str(index)))
                
                # down left
                if is_hit_box(mouse_pos, self.farmplot_position[2][0], self.farmplot_position[2][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[2], mouse_pos)
                    if clickdown and (index != None):
                        if watering:
                            loaded_sound.click.play()
                            self.set_wet('3'+str(index))
                            self.draw_farmland('3'+str(index), True)
                            print (self.check_crops_status('3'+str(index)))
                        else:    
                            print (self.check_crops_status('3'+str(index)))
                
                # down right
                if is_hit_box(mouse_pos, self.farmplot_position[3][0], self.farmplot_position[3][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[3], mouse_pos)
                    if clickdown and (index != None):
                        if watering:
                            loaded_sound.click.play()
                            self.set_wet('4'+str(index))
                            self.draw_farmland('4'+str(index), True)
                            print (self.check_crops_status('4'+str(index)))
                        else:
                            print (self.check_crops_status('4'+str(index)))
    def set_crops(self, plot, seed):
        pass
            
    def set_dry(self, plot):
        if plot[1] == 'a':
            land = 0
        elif plot[1] == 'b':
            land = 1
        elif plot[1] == 'c':
            land = 2
        elif plot[1] == 'd':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].watering = False
        self.farmplot[int(plot[0]) - 1].farmland[land].dry_time = None
    
    def set_wet(self, plot):
        if plot[1] == 'a':
            land = 0
        elif plot[1] == 'b':
            land = 1
        elif plot[1] == 'c':
            land = 2
        elif plot[1] == 'd':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].watering = True
        self.farmplot[int(plot[0]) - 1].farmland[land].dry_time = self.time + 3000

    def check_crops_status(self, plot):
        # method นี้ return [ชื่อ, สถานะการรดน้ำ, เวลาฟาร์มแห้ง, state ปัจจุบัน]
        if plot[1] == 'a':
            land = 0
        elif plot[1] == 'b':
            land = 1
        elif plot[1] == 'c':
            land = 2
        elif plot[1] == 'd':
            land = 3
        else:
            land = int(plot[1])

        name = self.farmplot[int(plot[0]) - 1].farmland[land].crop.name
        watering = self.farmplot[int(plot[0]) - 1].farmland[land].watering
        dry_time = self.farmplot[int(plot[0]) - 1].farmland[land].dry_time
        if name is None:
            state = None
        else:
            state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.now_state
        return [name, watering, dry_time, state]

    def farmplot_check_crops(self, farm, mouse_pos):
        # method นี้ return ตำแหน่งของต้นไม้ที่ถูกเม้าส์ชี้ใน farm ที่ input เข้ามาเป้น parameter
        # โดนที่ ถ้าเป็น ถ้าต้นa:return 0, ต้นb:return 1, ......
        
        # farm = [(145,180),(310,300)]
        if is_hit_box(mouse_pos,farm[0], farm[1]):
            # assign valuable
            start_point = farm[0]
            mid_point = (farm[0][0]+farm[1][0])/2,(farm[0][1]+farm[1][1])/2# (เฉลี่ย x,เฉลี่ย y)
            final_point = farm[1]

            # farm  a
            a = start_point # (start x ,start y)
            b = mid_point # (mid x ,mid y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม a มาแสดงผล
                return 0

            # farm  b
            a = (mid_point[0], start_point[1]) # (mid x ,start y)
            b = (final_point[0], mid_point[1]) # (final x, mid y) 
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม b มาแสดงผล
                return 1

            # farm  c
            a = (start_point[0], mid_point[1]) # (start x, mid y) 
            b = (mid_point[0], final_point[1]) # (mid x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม c มาแสดงผล
                return 2

            # farm  d
            a = mid_point # (mid x ,mid y)
            b = final_point #(final x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม d มาแสดงผล
                return 3
            return None
    

    def draw_bg(self):
        global loaded_image
        global loaded_sound
        # background 
        window.blit(loaded_image.farm_bg, (0, 0))
        
        # farmland
        a = self.farmplot_position[0][0][0]
        b = self.farmplot_position[0][0][1]
        x = self.farmplot_position[0][1][0]
        y = self.farmplot_position[0][1][1]

        farm_scale = int(((a+x)/2)-a) , int(((b+y)/2)-b)
        pic = pygame.transform.scale(loaded_image.dry_farm, farm_scale)
        for plot in self.farmplot_position:
            window.blit(pic, (plot[0]))
            window.blit(pic, (plot[0][0]+farm_scale[0] , plot[0][1]))
            window.blit(pic, (plot[0][0], plot[0][1]+farm_scale[1]))
            window.blit(pic, (plot[0][0]+farm_scale[0], plot[0][1]+farm_scale[1]))


        # ปุ่มรดน้ำ
        pygame.draw.rect(window, (0,0,150),[35, 205, 55, 65], 3)
        # ปุ่มยุ้งฉาง
        pygame.draw.rect(window, (150,0,150),[35, 320, 55, 65], 3)
        # ปุ่มร้านค้า
        pygame.draw.rect(window, (0,150,150),[430, 20, 150, 120], 3)
        # ปุ่มออกเกม
        pygame.draw.rect(window, (150,150,0),[390,500, 90, 70], 3)
        
        pygame.display.update()

    def draw_farmland(self, plot, watering=False):
        global loaded_image
        global loaded_sound
        # farmland
        if plot[0] == '1' or plot[0] == 'a':
            index = 0
        elif plot[0] == '2' or plot[0] == 'b':
            index = 1
        elif plot[0] == '3' or plot[0] == 'c':
            index = 2
        elif plot[0] == '4' or plot[0] == 'd':
            index = 3
        a = self.farmplot_position[index][0][0]
        b = self.farmplot_position[index][0][1]
        x = self.farmplot_position[index][1][0]
        y = self.farmplot_position[index][1][1]

        farm_scale = int(((a+x)/2)-a) , int(((b+y)/2)-b)
        if watering:
            farmland_image = pygame.transform.scale(loaded_image.wet_farm, farm_scale)
        else:
            farmland_image = pygame.transform.scale(loaded_image.dry_farm, farm_scale)
        print ('DRAWFARMLAND ', plot)
        if plot[1] == 'a' or plot[1] == '0':
            window.blit(farmland_image, (self.farmplot_position[index][0]))
            print 
        elif plot[1] == 'b' or plot[1] == '1':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0] , self.farmplot_position[index][0][1]))
        elif plot[1] == 'c' or plot[1] == '2':
            window.blit(farmland_image, (self.farmplot_position[index][0][0], self.farmplot_position[index][0][1]+farm_scale[1]))
        elif plot[1] == 'd' or plot[1] == '3':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0], self.farmplot_position[index][0][1]+farm_scale[1]))
    
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
        # drawing page ------------------- drawing page
        # background 
        window.blit(loaded_image.main_bg, (0, 0))
        # newgame botton
        pygame.draw.rect(window, (150,0,150),[220, 100, 380, 100], 3)
        # continue botton
        pygame.draw.rect(window, (0,150,150),[220, 200, 380, 100], 3)
        # credit botton
        pygame.draw.rect(window, (150,150,0),[220, 300, 380, 100], 3)
        # exit botton
        pygame.draw.rect(window, (150,0,0),[220, 400, 380, 100], 3)

        pygame.display.update()

        clock = pygame.time.Clock()
        run = True
        while run:
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
                        loaded_sound.click.play()
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
                        loaded_sound.click.play()
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
                        loaded_sound.click.play()
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
                        loaded_sound.click.play()
                        return 'exit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

# newgame
class Newgame_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global loaded_image
        global loaded_sound
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
        self.farmplot = [Farmplot(), Farmplot(), Farmplot(), Farmplot()]

class Inventory():
    def __init__(self):
        self.inventory = {'wheat': 0, 'wheat_seed': 0, 
                    'cucumber': 0, 'cucumber_seed': 0, 
                    'tomato': 0, 'tomato_seed': 0,
                    'potato': 0,  'potato_seed': 0,
                    'redcabbage': 0, 'redcabbage_seed':0,
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

class Farmplot():
    def __init__(self):
        self.farmland = [Farmland(), Farmland(), Farmland(), Farmland()]

class Farmland():
    def __init__(self):
        self.crop = Empty()
        self.watering = False
        self.dry_time = None
        

# Crops -------------------------- Crops
class Wheat():
    def __init__(self):
        self.name = 'Wheat'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.wheat_state1
        self.crops_state2 = loaded_image.wheat_state2
        self.crops_state3 = loaded_image.wheat_state3
        self.crops_state4 = loaded_image.wheat_state4
        self.sale_price = 10
        self.seed_price = 5

class Cucumber():
    def __init__(self):
        self.name = 'Cucumber'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.cucumber_state1
        self.crops_state2 = loaded_image.cucumber_state2
        self.crops_state3 = loaded_image.cucumber_state3
        self.crops_state4 = loaded_image.cucumber_state4
        self.sale_price = 30
        self.seed_price = 10

class Tomato():
    def __init__(self):
        self.name = 'Tomato'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.tomato_state1
        self.crops_state2 = loaded_image.tomato_state2
        self.crops_state3 = loaded_image.tomato_state3
        self.crops_state4 = loaded_image.tomato_state4
        self.sale_price = 50
        self.seed_price = 15

class Potato():
    def __init__(self):
        self.name = 'Potato'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.potato_state1
        self.crops_state2 = loaded_image.potato_state2
        self.crops_state3 = loaded_image.potato_state3
        self.crops_state4 = loaded_image.potato_state4
        self.sale_price = 70
        self.seed_price = 20

class Redcabbage():
    def __init__(self):
        self.name = 'Redcabbage'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.redcabbage_state1
        self.crops_state2 = loaded_image.redcabbage_state2
        self.crops_state3 = loaded_image.redcabbage_state3
        self.crops_state4 = loaded_image.redcabbage_state4
        self.sale_price = 100
        self.seed_price = 25

class Orange():
    def __init__(self):
        self.name = 'Orange'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.orange_state1
        self.crops_state2 = loaded_image.orange_state2
        self.crops_state3 = loaded_image.orange_state3
        self.crops_state4 = loaded_image.orange_state4
        self.sale_price = 50
        self.seed_price = 30

class Mango():
    def __init__(self):
        self.name = 'Mango'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.mango_state1
        self.crops_state2 = loaded_image.mango_state2
        self.crops_state3 = loaded_image.mango_state3
        self.crops_state4 = loaded_image.mango_state4
        self.sale_price = 150
        self.seed_price = 40

class Apple():
    def __init__(self):
        self.name = 'Apple'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.apple_state1
        self.crops_state2 = loaded_image.apple_state2
        self.crops_state3 = loaded_image.apple_state3
        self.crops_state4 = loaded_image.apple_state4
        self.sale_price = 350
        self.seed_price = 50

class Melon():
    def __init__(self):
        self.name = 'Melon'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.melon_state1
        self.crops_state2 = loaded_image.melon_state2
        self.crops_state3 = loaded_image.melon_state3
        self.crops_state4 = loaded_image.melon_state4
        self.sale_price = 400
        self.seed_price = 60

class Grape():
    def __init__(self):
        self.name = 'Grape'
        self.growing_time = 1 # growing_time per 1 state (sec)
        self.now_state = 1
        self.crops_state1 = loaded_image.grape_state1
        self.crops_state2 = loaded_image.grape_state2
        self.crops_state3 = loaded_image.grape_state3
        self.crops_state4 = loaded_image.grape_state4
        self.sale_price = 500
        self.seed_price = 70

class Empty():
    def __init__(self):
        self.name = None
        


# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing Vegetables")


window.fill((255,255,255))
pygame.display.update()
loaded_image = Image_()
loaded_sound = Sound_()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():
    global loaded_image
    global loaded_sound
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
