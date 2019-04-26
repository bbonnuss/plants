# Import ========================= Import ========================= Import
import pygame
#import sys
from math import ceil
from os.path import join
from numpy.random import choice

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

def rpc(player, bot):
    # player คือ อาวุธของ player เป็นไปได้ '0', '2', '5'
    # bot คือ อาวุธของ bot เป็นไปได้ '0', '2', '5'
    if player == '0':
        if bot == '0':
            return 'draw'
        if bot == '2':
            return 'win'
        if bot == '5':    
            return 'lose'
    elif player == '2':
        if bot == '0':
            return 'lose'
        if bot == '2':
            return 'draw'
        if bot == '5': 
            return 'win'   
    elif player == '5':
        if bot == '0':
            return 'win'
        if bot == '2':
            return 'lose'
        if bot == '5':   
            return 'draw' 

    return None

def money_str(money,comma=True, len_=13):
    money = str(money)
    while len(money) < len_:
        money = ' '+ money
    if not comma:
        return money
    # ใส่คอมม่าให้ด้วย
    count = 0
    result = []
    for index in range(-1, -(len(money)),-1):
        money[index]
        if (count == 3) and (money[index] != ' '):
            count = 0
            result.insert(0, ',')
        result.insert(0, money[index])
        count += 1
    return ''.join(result)

# Class ========================== Class ========================== Class
# resouce_manager ---------------- resouce_manager
class Sound_():
    def __init__(self):
        #pygame.display.set_caption("FARMER & THIEF : "+"Loading..."+"sound")
        self.main_theme = None
        self.farm_theme = pygame.mixer.Sound(join('assets','sound','Get_Outside_farm.wav'))
        self.shop_theme = pygame.mixer.Sound(join('assets','sound','Mr_Turtle_shop.wav'))
        self.storage_theme = pygame.mixer.Sound(join('assets','sound','Path_to_Follow_shop_storage.wav'))

        self.change_page = pygame.mixer.Sound(join('assets','sound','change_page.wav'))
        self.click = pygame.mixer.Sound(join('assets','sound','change_page.wav'))
        self.lose1 = pygame.mixer.Sound(join('assets','sound','lose1.wav'))
        self.lose2 = pygame.mixer.Sound(join('assets','sound','lose2.wav'))
        self.draw = pygame.mixer.Sound(join('assets','sound','draw.wav'))
        self.coin = pygame.mixer.Sound(join('assets','sound','coin.wav'))
        self.win = pygame.mixer.Sound(join('assets','sound','win.wav'))
        self.watering = pygame.mixer.Sound(join('assets','sound','watering.wav'))
        self.theif_notice = pygame.mixer.Sound(join('assets','sound','theif_notice.wav'))
        self.planting = pygame.mixer.Sound(join('assets','sound','planting.wav'))
        self.minigame_start = pygame.mixer.Sound(join('assets','sound','minigame_starting.wav'))
   

class Image_():
    def __init__(self):
        #pygame.display.set_caption("FARMER & THIEF : "+"Loading..."+"image")
        # background
        self.main_bg = pygame.image.load(join('assets','image','main_bg.png')).convert_alpha()
        self.farm_bg = pygame.image.load(join('assets','image','farmbg.png')).convert_alpha()
        self.bot_bg = pygame.image.load(join('assets','image','bg_nowatering.png')).convert_alpha()
        self.minigame_bg = pygame.image.load(join('assets','image','minigame_bg.png')).convert_alpha()
        self.win_bg = pygame.image.load(join('assets','image','win_bg.png')).convert_alpha()
        self.win_defend_bg = pygame.image.load(join('assets','image','win_defend_bg.png')).convert_alpha()
        self.draw_bg = pygame.image.load(join('assets','image','draw_bg.png')).convert_alpha()
        self.lose_bg = pygame.image.load(join('assets','image','lose_bg.png')).convert_alpha()
        self.storage_bg = pygame.image.load(join('assets','image','storage_bg.png')).convert_alpha()
        self.storage_bg_p1 = pygame.image.load(join('assets','image','storage_bg_p1.png')).convert_alpha()
        self.storage_bg_p2 = pygame.image.load(join('assets','image','storage_bg_p2.png')).convert_alpha()
        self.storage_bg_p3 = pygame.image.load(join('assets','image','storage_bg_p3.png')).convert_alpha()
        self.shop_bg = pygame.image.load(join('assets','image','shop_bg.png')).convert_alpha()
        
        self.dry_farm = pygame.image.load(join('assets','image','dry_farm.png')).convert_alpha()
        self.wet_farm = pygame.image.load(join('assets','image','wet_farm.png')).convert_alpha()
        # crops growing state
        self.wheat_state1_wet = pygame.image.load(join('assets','image','wheat2_wet.png')).convert_alpha()
        self.wheat_state2_wet = pygame.image.load(join('assets','image','wheat2_wet.png')).convert_alpha()
        self.wheat_state3_wet = pygame.image.load(join('assets','image','wheat3_wet.png')).convert_alpha()
        self.wheat_state4_wet = pygame.image.load(join('assets','image','wheat4_wet.png')).convert_alpha()
        self.cucumber_state1_wet = pygame.image.load(join('assets','image','cucumber2_wet.png')).convert_alpha()
        self.cucumber_state2_wet = pygame.image.load(join('assets','image','cucumber2_wet.png')).convert_alpha()
        self.cucumber_state3_wet = pygame.image.load(join('assets','image','cucumber3_wet.png')).convert_alpha()
        self.cucumber_state4_wet = pygame.image.load(join('assets','image','cucumber4_wet.png')).convert_alpha()
        self.tomato_state1_wet = pygame.image.load(join('assets','image','tomato2_wet.png')).convert_alpha()
        self.tomato_state2_wet = pygame.image.load(join('assets','image','tomato2_wet.png')).convert_alpha()
        self.tomato_state3_wet = pygame.image.load(join('assets','image','tomato3_wet.png')).convert_alpha()
        self.tomato_state4_wet = pygame.image.load(join('assets','image','tomato4_wet.png')).convert_alpha()
        self.potato_state1_wet = pygame.image.load(join('assets','image','potato2_wet.png')).convert_alpha()
        self.potato_state2_wet = pygame.image.load(join('assets','image','potato2_wet.png')).convert_alpha()
        self.potato_state3_wet = pygame.image.load(join('assets','image','potato3_wet.png')).convert_alpha()
        self.potato_state4_wet = pygame.image.load(join('assets','image','potato4_wet.png')).convert_alpha()
        self.redcabbage_state1_wet = pygame.image.load(join('assets','image','redcabbage2_wet.png')).convert_alpha()
        self.redcabbage_state2_wet = pygame.image.load(join('assets','image','redcabbage2_wet.png')).convert_alpha()
        self.redcabbage_state3_wet = pygame.image.load(join('assets','image','redcabbage3_wet.png')).convert_alpha()
        self.redcabbage_state4_wet = pygame.image.load(join('assets','image','redcabbage4_wet.png')).convert_alpha()
        self.orange_state1_wet = pygame.image.load(join('assets','image','orange2_wet.png')).convert_alpha()
        self.orange_state2_wet = pygame.image.load(join('assets','image','orange2_wet.png')).convert_alpha()
        self.orange_state3_wet = pygame.image.load(join('assets','image','orange3_wet.png')).convert_alpha()
        self.orange_state4_wet = pygame.image.load(join('assets','image','orange4_wet.png')).convert_alpha()
        self.mango_state1_wet = pygame.image.load(join('assets','image','mango2_wet.png')).convert_alpha()
        self.mango_state2_wet = pygame.image.load(join('assets','image','mango2_wet.png')).convert_alpha()
        self.mango_state3_wet = pygame.image.load(join('assets','image','mango3_wet.png')).convert_alpha()
        self.mango_state4_wet = pygame.image.load(join('assets','image','mango4_wet.png')).convert_alpha()
        self.apple_state1_wet = pygame.image.load(join('assets','image','apple2_wet.png')).convert_alpha()
        self.apple_state2_wet = pygame.image.load(join('assets','image','apple2_wet.png')).convert_alpha()
        self.apple_state3_wet = pygame.image.load(join('assets','image','apple3_wet.png')).convert_alpha()
        self.apple_state4_wet = pygame.image.load(join('assets','image','apple4_wet.png')).convert_alpha()
        self.melon_state1_wet = pygame.image.load(join('assets','image','melon2_wet.png')).convert_alpha()
        self.melon_state2_wet = pygame.image.load(join('assets','image','melon2_wet.png')).convert_alpha()
        self.melon_state3_wet = pygame.image.load(join('assets','image','melon3_wet.png')).convert_alpha()
        self.melon_state4_wet = pygame.image.load(join('assets','image','melon4_wet.png')).convert_alpha()
        self.grape_state1_wet = pygame.image.load(join('assets','image','grape2_wet.png')).convert_alpha()
        self.grape_state2_wet = pygame.image.load(join('assets','image','grape2_wet.png')).convert_alpha()
        self.grape_state3_wet = pygame.image.load(join('assets','image','grape3_wet.png')).convert_alpha()
        self.grape_state4_wet = pygame.image.load(join('assets','image','grape4_wet.png')).convert_alpha()

        self.wheat_state1_dry = pygame.image.load(join('assets','image','wheat2_wet.png')).convert_alpha()
        self.wheat_state2_dry = pygame.image.load(join('assets','image','wheat2_dry.png')).convert_alpha()
        self.wheat_state3_dry = pygame.image.load(join('assets','image','wheat3_dry.png')).convert_alpha()
        self.wheat_state4_dry = pygame.image.load(join('assets','image','wheat4_dry.png')).convert_alpha()
        self.cucumber_state1_dry = pygame.image.load(join('assets','image','cucumber2_dry.png')).convert_alpha()
        self.cucumber_state2_dry = pygame.image.load(join('assets','image','cucumber2_dry.png')).convert_alpha()
        self.cucumber_state3_dry = pygame.image.load(join('assets','image','cucumber3_dry.png')).convert_alpha()
        self.cucumber_state4_dry = pygame.image.load(join('assets','image','cucumber4_dry.png')).convert_alpha()
        self.tomato_state1_dry = pygame.image.load(join('assets','image','tomato2_dry.png')).convert_alpha()
        self.tomato_state2_dry = pygame.image.load(join('assets','image','tomato2_dry.png')).convert_alpha()
        self.tomato_state3_dry = pygame.image.load(join('assets','image','tomato3_dry.png')).convert_alpha()
        self.tomato_state4_dry = pygame.image.load(join('assets','image','tomato4_dry.png')).convert_alpha()
        self.potato_state1_dry = pygame.image.load(join('assets','image','potato2_dry.png')).convert_alpha()
        self.potato_state2_dry = pygame.image.load(join('assets','image','potato2_dry.png')).convert_alpha()
        self.potato_state3_dry = pygame.image.load(join('assets','image','potato3_dry.png')).convert_alpha()
        self.potato_state4_dry = pygame.image.load(join('assets','image','potato4_dry.png')).convert_alpha()
        self.redcabbage_state1_dry = pygame.image.load(join('assets','image','redcabbage2_dry.png')).convert_alpha()
        self.redcabbage_state2_dry = pygame.image.load(join('assets','image','redcabbage2_dry.png')).convert_alpha()
        self.redcabbage_state3_dry = pygame.image.load(join('assets','image','redcabbage3_dry.png')).convert_alpha()
        self.redcabbage_state4_dry = pygame.image.load(join('assets','image','redcabbage4_dry.png')).convert_alpha()
        self.orange_state1_dry = pygame.image.load(join('assets','image','orange2_dry.png')).convert_alpha()
        self.orange_state2_dry = pygame.image.load(join('assets','image','orange2_dry.png')).convert_alpha()
        self.orange_state3_dry = pygame.image.load(join('assets','image','orange3_dry.png')).convert_alpha()
        self.orange_state4_dry = pygame.image.load(join('assets','image','orange4_dry.png')).convert_alpha()
        self.mango_state1_dry = pygame.image.load(join('assets','image','mango2_dry.png')).convert_alpha()
        self.mango_state2_dry = pygame.image.load(join('assets','image','mango2_dry.png')).convert_alpha()
        self.mango_state3_dry = pygame.image.load(join('assets','image','mango3_dry.png')).convert_alpha()
        self.mango_state4_dry = pygame.image.load(join('assets','image','mango4_dry.png')).convert_alpha()
        self.apple_state1_dry = pygame.image.load(join('assets','image','apple2_dry.png')).convert_alpha()
        self.apple_state2_dry = pygame.image.load(join('assets','image','apple2_dry.png')).convert_alpha()
        self.apple_state3_dry = pygame.image.load(join('assets','image','apple3_dry.png')).convert_alpha()
        self.apple_state4_dry = pygame.image.load(join('assets','image','apple4_dry.png')).convert_alpha()
        self.melon_state1_dry = pygame.image.load(join('assets','image','melon2_dry.png')).convert_alpha()
        self.melon_state2_dry = pygame.image.load(join('assets','image','melon2_dry.png')).convert_alpha()
        self.melon_state3_dry = pygame.image.load(join('assets','image','melon3_dry.png')).convert_alpha()
        self.melon_state4_dry = pygame.image.load(join('assets','image','melon4_dry.png')).convert_alpha()
        self.grape_state1_dry = pygame.image.load(join('assets','image','grape2_dry.png')).convert_alpha()
        self.grape_state2_dry = pygame.image.load(join('assets','image','grape2_dry.png')).convert_alpha()
        self.grape_state3_dry = pygame.image.load(join('assets','image','grape3_dry.png')).convert_alpha()
        self.grape_state4_dry = pygame.image.load(join('assets','image','grape4_dry.png')).convert_alpha()
        
        # seed bag
        self.wheat_seed = pygame.image.load(join('assets','image','wheat_seed.png')).convert_alpha()
        self.cucumber_seed = pygame.image.load(join('assets','image','cucumber_seed.png')).convert_alpha()
        self.tomato_seed = pygame.image.load(join('assets','image','tomato_seed.png')).convert_alpha()
        self.potato_seed = pygame.image.load(join('assets','image','potato_seed.png')).convert_alpha()
        self.redcabbage_seed = pygame.image.load(join('assets','image','redcabbage_seed.png')).convert_alpha()
        self.orange_seed = pygame.image.load(join('assets','image','orange_seed.png')).convert_alpha()
        self.mango_seed = pygame.image.load(join('assets','image','mango_seed.png')).convert_alpha()
        self.apple_seed = pygame.image.load(join('assets','image','apple_seed.png')).convert_alpha()
        self.melon_seed = pygame.image.load(join('assets','image','melon_seed.png')).convert_alpha()
        self.grape_seed = pygame.image.load(join('assets','image','grape_seed.png')).convert_alpha()

        # icon
        self.fruit_bag = pygame.image.load(join('assets','image','fruit_bag.png')).convert_alpha()
        self.vegetable_bag = pygame.image.load(join('assets','image','vegetable_bag.png')).convert_alpha()
        self.shop_shelf = pygame.image.load(join('assets','image','shop_shelf.png')).convert_alpha()
        self.shop = pygame.image.load(join('assets','image','shop.png')).convert_alpha()
        self.sale_icon = pygame.image.load(join('assets','image','sale.png')).convert_alpha()
        self.process_icon = pygame.image.load(join('assets','image','process_button.png')).convert_alpha()
        self.next_icon = pygame.image.load(join('assets','image','next_button.png')).convert_alpha()
        self.home_icon = pygame.image.load(join('assets','image','home_button.png')).convert_alpha()
        self.before_icon = pygame.image.load(join('assets','image','before_button.png')).convert_alpha()
        self.weapon0_icon = pygame.image.load(join('assets','image','0.png')).convert_alpha()
        self.weapon2_icon = pygame.image.load(join('assets','image','2.png')).convert_alpha()
        self.weapon5_icon = pygame.image.load(join('assets','image','5.png')).convert_alpha()


        self.apple = pygame.image.load(join('assets','image','apple.png')).convert_alpha()
        self.cucumber = pygame.image.load(join('assets','image','cucumber.png')).convert_alpha()
        self.grape = pygame.image.load(join('assets','image','grape.png')).convert_alpha()
        self.mango = pygame.image.load(join('assets','image','mango.png')).convert_alpha()
        self.melon = pygame.image.load(join('assets','image','melon.png')).convert_alpha()
        self.melon2 = pygame.image.load(join('assets','image','melon2.png')).convert_alpha()
        self.melon3 = pygame.image.load(join('assets','image','melon3.png')).convert_alpha()
        self.orange = pygame.image.load(join('assets','image','orange.png')).convert_alpha()
        self.orange2 = pygame.image.load(join('assets','image','orange2.jpg')).convert_alpha()
        self.potato = pygame.image.load(join('assets','image','potato.png')).convert_alpha()
        self.redcabbage = pygame.image.load(join('assets','image','redcabbage.png')).convert_alpha()
        self.tomato = pygame.image.load(join('assets','image','tomato.png')).convert_alpha()
        self.tomato2 = pygame.image.load(join('assets','image','tomato2.png')).convert_alpha()
        self.wheat = pygame.image.load(join('assets','image','wheat.png')).convert_alpha()
        self.wheat2 = pygame.image.load(join('assets','image','wheat2.png')).convert_alpha()


# Menu --------------------------- Menu
# หน้าฟาร์มของผู้เล่น
class Player_farm():
    def __init__(self, profile):
        self.player = profile# Player()
        self.inv = self.player.inventory
        self.money = self.player.money
        self.farmplot = self.player.farmplot
        self.load_time = 0
        
        self.time = self.load_time + pygame.time.get_ticks()
        self.previous_time = self.time
        self.bot_list = self.player.bot
        self.bot_farm_list = list(map(lambda x: Bot_farm(x), self.bot_list))

        self.money_dispay = ((94,42),(247,76))
        self.seed_dispay = { 'wheat_seed': ((518,539),(551,549)), 
                            'cucumber_seed': ((551,539),(584,549)), 
                            'tomato_seed': ((584,539),(615,549)), 
                            'potato_seed': ((615,539),(648,549)),
                            'redcabbage_seed':((486,539),(518,549)),
                            'orange_seed': ((551,588),(584,598)),
                            'mango_seed': ((518,588),(551,598)),
                            'apple_seed': ((615,588),(648,598)), 
                            'melon_seed': ((486,588),(518,598)), 
                            'grape_seed': ((584,588),(615,598))}

        self.shop_button = ((545, 66),(720,220))
        self.storage_button = ((63,295),(265,499))
        self.watering_button = ((48,235),(120,280))
        self.mainmenu_button = ((218,523),(283,593))
        self.seedselection_button = ((486,499),(647,584))
        self.save_button = ((0,0),(0,0))
        self.saveexit_button = ((0,0),(0,0))
        self.home_button = ((293,523),(356,593))
        self.next_button = ((367,523),(432,593))
        self.farmplot_position = [[(449,257),(581,358)],    # ซ้ายบน
                                [(624,257),(754,358)],      # ขวาบน
                                [(449,386),(581,492)],      # ล่างซ้าย
                                [(624,386),(754,492)]]      # ล่างขวา
        self.hammer_button = ((552,247),(760,484))
        self.paper_button = ((298,247),(504,484))
        self.scissors_button = ((40,247),(250,484))
        self.steal_button = ((663,473),(757,580))
        self.backhome_button = self.steal_button
        
    
    def run(self):
        pygame.display.set_caption("FARMER & THIEF : "+"Farm")
        global loaded_image
        global loaded_sound

        # loop per second 
        clock = pygame.time.Clock()

        # clock
        enter_farm_time = pygame.time.get_ticks()

        # วาดพื้นหลัง
        self.draw_bg()
        pygame.display.update()

        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
        pygame.mixer.music.play(loops=-1)

        cooldown = 60000
        seeding = False
        watering = False
        run = True
        selected = 'home'
        while run:
            
            # loop per second 
            clock.tick(40)

            # debuging display
            if seeding:
                pygame.display.set_caption("FARMER & THIEF : "+"Select your farmland to plant your seed")
                pass
            elif watering:
                pygame.display.set_caption("FARMER & THIEF : "+"Select your farmland to watering")
                pass
            else:
                pygame.display.set_caption("FARMER & THIEF : "+"Farm")
                pass

            # exit to location
            if selected == 'home':
                pass
            elif selected == 'exit':
                # save
                return 'exit'
            elif selected == 'main':
                return 'main'
            elif selected == 'ai_farm' and cooldown <= 0:
                for bot in self.bot_farm_list:
                    # pause theme song
                    pygame.mixer.music.pause()

                    self.inv, self.money, selected, cooldown = bot.run_bot_farm(self.inv, self.money)
                    
                    # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
                    pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
                    pygame.mixer.music.play(loops=-1)

            elif selected == 'ai_farm' and cooldown > 0:
                print ('Player => wait for %s sec. To steal AI\'s crop'%(str(cooldown)[:-3]))
                selected = 'home'
            elif selected == 'scout':
                for bot in self.bot_farm_list:
                    # stop theme song
                    pygame.mixer.music.stop()

                    # play sound effect change_page
                    loaded_sound.change_page.play()

                    selected = bot.look_bot_farm()

                    # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
                    pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
                    pygame.mixer.music.play(loops=-1)
            
            # clock update (clock is millisec)
            self.previous_time = self.time
            self.time = self.load_time + (pygame.time.get_ticks() - enter_farm_time)
            if cooldown > 0 and self.previous_time < self.time:
                cooldown -= (self.time - self.previous_time)

            # ระบบ อัพเดตฟาร์ม/จัดการฟาร์ม
            plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
            for plot in plot_list:
                stats = self.check_crops_status(plot)
                # set farmland dry again
                if stats[2] is not None:
                    if stats[1] and (stats[2] < self.time): # ถ้าฟาร์มชื้น และ เกินเวลาคงเหลือ
                        self.set_dry(plot)
                        self.draw_farmland(plot, False)

                # set crops growing to next state
                if stats[4] is not None:
                    # ถ้ามีเวลาคงเหลือ ลดเวลารอลง ถ้ารดน้ำไว้
                    if stats[1] and not stats[5] and self.previous_time < self.time:
                        time_decrease = self.time - self.previous_time
                        self.growing_by_plot(plot, time_decrease)
                    
                    if stats[4] <= 0:# เพิ่ม state
                        self.grow_up_by_plot(plot)
            
            # วาดพื้นหลัง
            self.draw_bg()
            pygame.display.update()

            # AI background process
            for bot in self.bot_farm_list:
                
                # steal process
                if bot.steal_cooldown > 0 and self.previous_time < self.time:
                    bot.steal_cooldown -= (self.time - self.previous_time)
                
                # randomly steal
                bot_steal_rate = 0.0001 # 0.1% ทุกๆ 40 ครั้ง ใน 1 วินาที
                success = bool(choice([True,False],p=[bot_steal_rate, 1-bot_steal_rate]))
                #print (str(bot.steal_cooldown),success)
                if bot.steal_cooldown <= 0 and success:
                    print ('AI => AI try to steal your crops!!')
                    bot.steal_cooldown = 60000

                    # pause theme song
                    pygame.mixer.music.pause()
                    
                    result = self.minigame()

                    # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
                    pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
                    pygame.mixer.music.play(loops=-1)

                    if result == 'win':
                        bot.money -= 100
                    elif result == 'lose':
                        name = self.random_pickup()
                        print ('Player => AI steal %s from your farm'%name)


                # farm process
                plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
                for plot in plot_list:
                    stats = bot.check_crops_status(plot)
                    #print (stats)
                    # set farmland alway wet (bot is OP!!!! LOLLLL)
                    if not stats[1]:# watering
                        bot.set_wet(plot)
                    
                    # สุ่มปลูก -------------------------- สุ่มปลูก
                    bot_plant_rate = .002 
                    bot_harvest_rate = .001 
                    if stats[0] is None and bool(choice([True,False],p=[bot_plant_rate, 1-bot_plant_rate])):#ชื่อผักเป็น None และ สุ่มติด
                        bot.random_plant(plot)

                    # growing ------------------------ growing
                    # set crops growing to next state
                    if stats[4] is not None:
                        # ถ้ามีเวลาคงเหลือ ลดเวลารอลง ถ้ารดน้ำไว้
                        if stats[1] and not stats[5] and self.previous_time < self.time:
                            time_decrease = self.time - self.previous_time
                            bot.growing_by_plot(plot, time_decrease)
                    
                        if stats[4] <= 0:# เพิ่ม state
                            bot.grow_up_by_plot(plot)
                
                    # สุ่มเก็บ ------------------------ สุ่มเก็บ
                    if stats[5] and bool(choice([True,False],p=[bot_harvest_rate, 1-bot_harvest_rate])): # ถ้าโตแล้ว
                        bot.harvest(plot)
                        

            # input - output
            for event in pygame.event.get():
                #print (self.inv.get_inv())

                # pointer
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # hot key
                    
                # exit
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()

                    selected = 'exit'
                
                # Botton ------------------------- Botton
                # ปุ่ม ส่อง AI
                if is_hit_box(mouse_pos,self.home_button[0], self.home_button[1]):
                    #print ('Bot_farm : home')

                    if clickdown:
                        selected = 'scout'

                # ปุ่ม ออกไป main_menu
                if is_hit_box(mouse_pos,self.mainmenu_button[0], self.mainmenu_button[1]):
                    #print ('Player_farm : main_menu')

                    if clickdown:
                        # stop theme song
                        pygame.mixer.music.stop()

                        # play sound effect change_page
                        loaded_sound.change_page.play()
                        return 'main'
                # ปุ่ม รดน้ำ 
                if is_hit_box(mouse_pos,self.watering_button[0], self.watering_button[1]):
                    #print ('Player_farm : watering')

                    if clickdown :
                        # play sound effect click
                        loaded_sound.click.play()
                        
                        if seeding:  # คุณจะปลูกพร้อมรดน้ำไม่ได้ !!! ทำทีละอย่างนะจ๊ะ มือมีแค่ 2 ข้าง:
                            seeding = not seeding
                            print('Player => Stop Seeding')
                        watering = not watering
                        if watering:
                            print('Player => Start Watering')
                        else:
                            print('Player => Stop Watering')
                
                # ปุ่ม คลัง
                if is_hit_box(mouse_pos,self.storage_button[0], self.storage_button[1]):
                    #print ('Player_farm : storage')

                    if clickdown:
                        # pause theme song
                        pygame.mixer.music.pause()

                        # play sound effect change_page
                        loaded_sound.change_page.play()

                        storage = Storage_menu(self.inv, self.money)
                        self.inv, self.money, selected = storage.run()
                        
                        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
                        pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
                        pygame.mixer.music.play(loops=-1)
                
                # ปุ่ม ร้านค้า
                if is_hit_box(mouse_pos,self.shop_button[0], self.shop_button[1]):
                    #print ('Player_farm : shop')

                    if clickdown:
                        # pause theme song
                        pygame.mixer.music.pause()

                        # play sound effect change_page
                        loaded_sound.change_page.play()

                        shop = Shop_menu(self.inv, self.money)
                        self.inv, self.money, selected = shop.run()
                        
                        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
                        pygame.mixer.music.load(join('assets','sound','Get_Outside_farm.wav'))
                        pygame.mixer.music.play(loops=-1)
                
                # ปุ่มเลือก seed และ จัดการ inv เรื่อง seed
                if is_hit_box(mouse_pos,self.seedselection_button[0], self.seedselection_button[1]):
                    #print ('Player_farm : Seed Selection')                    

                    if clickdown and (not seeding): # ถ้าคลิกตอนไม่ปลูก
                        if watering:  # คุณจะปลูกพร้อมรดน้ำไม่ได้ !!! ทำทีละอย่างนะจ๊ะ มือมีแค่ 2 ข้าง:
                            watering = not watering
                            print('Player => Stop Watering')
                            
                        seed_name = self.seed_index(mouse_pos)
                        print ('Player => Start Seeding: %s'%seed_name)
                        if seed_name is not None:
                            # play sound effect click
                            loaded_sound.click.play()

                            if self.inv.item_dict[seed_name+'_seed'] > 0:
                                seeding = True
                                #print ('Select the plot that you want to plant it')
                            else:
                                seeding = False
                                seed_name = None
                                print ('Player => You don\'t have enough seed to plant it')
                    elif clickdown and seeding: # ถ้าคลิกตอนกำลังเลือกแปลง = ยกเลิกการปลูก
                        seeding = False
                        seed_name = None
                        print('Player => Stop Seeding')
                
                # ปุ่ม next AI
                if is_hit_box(mouse_pos,self.next_button[0], self.next_button[1]):
                    #print ('Player_farm : Next AI')    
                    if clickdown:
                        # play sound effect click
                        loaded_sound.click.play()

                        selected = 'ai_farm'
                # farmplot zone ----------------- farmplot zone
                # top left
                if is_hit_box(mouse_pos, self.farmplot_position[0][0], self.farmplot_position[0][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[0], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('1'+str(index))
                        if watering:
                            # play sound effect watering
                            loaded_sound.watering.play()

                            self.set_wet('1'+str(index))
                            self.draw_farmland('1'+str(index), True)
                        elif seeding and crops_status[0] is None:
                            # play sound effect planting
                            loaded_sound.planting.play()
                            
                            self.inv.remove(seed_name+'_seed', 1)
                            self.set_crops('1'+str(index), seed_name)
                            
                            # ถ้า seed หมด ยกเลิกการปลูกไปเลย
                            if self.inv.item_dict[seed_name+'_seed'] <= 0:
                                seed_name = None
                                seeding = False
                
                        elif seeding and crops_status[0] is not None:
                            # play sound effect unplanting
                            loaded_sound.planting.play()

                            print ('Player => This farm already planted')
                        elif crops_status[5]:# harvest?
                            # play sound effect harvest
                            loaded_sound.planting.play()

                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            self.inv.add(crops_status[0], crop_collected)
                            self.set_crops('1'+str(index), 'empty')
                            print ('Player => Harvested: %s x %s'%(crops_status[0], crop_collected))

                # top right
                if is_hit_box(mouse_pos, self.farmplot_position[1][0], self.farmplot_position[1][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[1], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('2'+str(index))
                        if watering:
                            # play sound effect watering
                            loaded_sound.watering.play()

                            self.set_wet('2'+str(index))
                        elif seeding and crops_status[0] is None:
                            # play sound effect planting
                            loaded_sound.planting.play()

                            self.inv.remove(seed_name+'_seed', 1)
                            self.set_crops('2'+str(index), seed_name)

                            # ถ้า seed หมด ยกเลิกการปลูกไปเลย
                            if self.inv.item_dict[seed_name+'_seed'] <= 0:
                                seed_name = None
                                seeding = False
                            
                        elif seeding and crops_status[0] is not None:
                            # play sound effect unplanting
                            loaded_sound.planting.play()
                            
                            print ('Player => This farm already planted')
                        elif crops_status[5]:# harvest?
                            # play sound effect harvest
                            loaded_sound.planting.play()

                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            self.inv.add(crops_status[0], crop_collected)
                            self.set_crops('2'+str(index), 'empty')
                            print ('Player => Harvested: %s x %s'%(crops_status[0], crop_collected))
                
                # down left
                if is_hit_box(mouse_pos, self.farmplot_position[2][0], self.farmplot_position[2][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[2], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('3'+str(index))
                        if watering:
                            # play sound effect watering
                            loaded_sound.watering.play()

                            self.set_wet('3'+str(index))
                        elif seeding and crops_status[0] is None:
                            # play sound effect planting
                            loaded_sound.planting.play()
                            
                            self.inv.remove(seed_name+'_seed', 1)
                            self.set_crops('3'+str(index), seed_name)

                            # ถ้า seed หมด ยกเลิกการปลูกไปเลย
                            if self.inv.item_dict[seed_name+'_seed'] <= 0:
                                seed_name = None
                                seeding = False
                            
                        elif seeding and crops_status[0] is not None:
                            # play sound effect unplanting
                            loaded_sound.planting.play()
                            
                            print ('Player => This farm already planted')
                        elif crops_status[5]:# harvest?
                            # play sound effect harvest
                            loaded_sound.planting.play()

                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            self.inv.add(crops_status[0], crop_collected)
                            self.set_crops('3'+str(index), 'empty')
                            print ('Player => Harvested: %s x %s'%(crops_status[0], crop_collected))
                
                # down right
                if is_hit_box(mouse_pos, self.farmplot_position[3][0], self.farmplot_position[3][1]):
                    index = self.farmplot_check_crops(self.farmplot_position[3], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('4'+str(index))
                        if watering:
                            # play sound effect watering
                            loaded_sound.watering.play()
                        
                            self.set_wet('4'+str(index))
                        elif seeding and crops_status[0] is None:
                            # play sound effect planting
                            loaded_sound.planting.play()
                           
                            self.inv.remove(seed_name+'_seed', 1)
                            self.set_crops('4'+str(index), seed_name)

                            # ถ้า seed หมด ยกเลิกการปลูกไปเลย
                            if self.inv.item_dict[seed_name+'_seed'] <= 0:
                                seed_name = None
                                seeding = False
                            
                        elif seeding and crops_status[0] is not None:
                            # play sound effect unplanting
                            loaded_sound.planting.play()

                            print ('Player => This farm already planted')
                        elif crops_status[5]:# harvest?
                            # play sound effect harvest
                            loaded_sound.planting.play()

                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            self.inv.add(crops_status[0], crop_collected)
                            self.set_crops('4'+str(index), 'empty')
                            print ('Player => Harvested: %s x %s'%(crops_status[0], crop_collected))
    
    def set_crops(self, plot, seed_name):
        print('Player => Plot:%s was set to crop:%s !'%(plot, seed_name))
        # plot เป็น str มี 2 อักษร คือ เลข และ a-d
        # seed_name เป็น str ที่เป๋็นชื่อของพืช
        if seed_name == 'wheat':
            seed = Wheat()
        elif seed_name == 'cucumber':
            seed = Cucumber()
        elif seed_name == 'tomato':
            seed = Tomato()
        elif seed_name == 'potato':
            seed = Potato()
        elif seed_name == 'redcabbage':
            seed = Redcabbage()
        elif seed_name == 'orange':
            seed = Orange()
        elif seed_name == 'mango':
            seed = Mango()
        elif seed_name == 'apple':
            seed = Apple()
        elif seed_name == 'melon':
            seed = Melon()
        elif seed_name == 'grape':
            seed = Grape()
        else :
            seed = Empty()

        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop = seed
        self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time = self.farmplot[int(plot[0]) - 1].farmland[land].crop.growing_time
            
    def set_dry(self, plot):
        print ('Player => Plot:%s is Dry!'%plot)
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].watering = False
        self.farmplot[int(plot[0]) - 1].farmland[land].dry_time = None
    
    def set_wet(self, plot):
        print ('Player => Plot:%s is Wet!'%plot)
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].watering = True
        self.farmplot[int(plot[0]) - 1].farmland[land].dry_time = self.time + 3000

    def check_crops_status(self, plot):
        # method นี้ return [ชื่อ, สถานะการรดน้ำ, เวลาฟาร์มแห้ง, state ปัจจุบัน, remaining_growth_time, harvestable?, image of cur_state]
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        name = self.farmplot[int(plot[0]) - 1].farmland[land].crop.name
        watering = self.farmplot[int(plot[0]) - 1].farmland[land].watering
        dry_time = self.farmplot[int(plot[0]) - 1].farmland[land].dry_time
        if name is None:
            state = None
        elif self.farmplot[int(plot[0]) - 1].farmland[land].crop.now_state is None:
            state = 4
        else:
            state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.now_state
        remaining_growth_time = self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time
        harvest =  self.farmplot[int(plot[0]) - 1].farmland[land].crop.harvestable
        if state == 1:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state1_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state1_dry
        elif state == 2:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state2_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state2_dry
        elif state == 3:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state3_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state3_dry
        elif (state == 4) or (state is None):
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state4_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state4_dry
            

        return [name, watering, dry_time, state, remaining_growth_time, harvest, image_state]
    
    def growing_by_plot(self, plot, time_decrease):
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time -= time_decrease
        
    def grow_up_by_plot(self, plot):
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop.grow_up()


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
                return 'a'

            # farm  b
            a = (mid_point[0], start_point[1]) # (mid x ,start y)
            b = (final_point[0], mid_point[1]) # (final x, mid y) 
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม b มาแสดงผล
                return 'b'

            # farm  c
            a = (start_point[0], mid_point[1]) # (start x, mid y) 
            b = (mid_point[0], final_point[1]) # (mid x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม c มาแสดงผล
                return 'c'

            # farm  d
            a = mid_point # (mid x ,mid y)
            b = final_point #(final x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม d มาแสดงผล
                return 'd'
            return None
    
    def seed_index(self, mouse_pos):
        # method นี้ return ชื่อ ของผัก ที่กดบนปุ่มเลือก seed
        x_length = (self.seedselection_button[0][0] - self.seedselection_button[1][0]) / 5
        y_length = (self.seedselection_button[0][1] - self.seedselection_button[1][1]) / 2

        box_x = ceil((self.seedselection_button[0][0] - mouse_pos[0]) / x_length)
        box_y = ceil((self.seedselection_button[0][1] - mouse_pos[1]) / y_length)
        
        if box_y == 1:
            if box_x == 2:
                return 'wheat'
            if box_x == 3:
                return 'cucumber'
            if box_x == 4:
                return 'tomato'
            if box_x == 5:
                return 'potato'
            if box_x == 1:
                return 'redcabbage'
        elif box_y == 2:
            if box_x == 3:
                return 'orange'
            if box_x == 2:
                return 'mango'
            if box_x == 5:
                return 'apple'
            if box_x == 1:
                return 'melon'
            if box_x == 4:
                return 'grape'
            
        return None
            
    def save(self, profile_name):
        profile_name = str(self.player.name)
        time = str(self.time)

    def random_pickup(self):
        plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
        stealable_list = []
        for plot in plot_list:
            stats = self.check_crops_status(plot)
            if stats[5]:
                stealable_list.append(plot)
        if len(stealable_list) == 0:
            return None
        len_list = len(stealable_list)
        p_list = list(map(lambda x: (1/len_list),stealable_list))
        selected_plot = choice(stealable_list, p=p_list)
        return self.check_crops_status(selected_plot)[0]

    def minigame(self):
        pygame.display.set_caption("FARMER & THIEF : "+"Minigame")
        global loaded_image
        global loaded_sound

        # loop per second 
        clock = pygame.time.Clock()

        # วาดพื้นหลัง
        self.draw_minigame()
        pygame.display.update()

        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(join('assets','sound','theif_notice.wav'))
        pygame.mixer.music.play(loops=-1)
        
        # bot weapon
        bot_weapon = choice(['0', '2', '5'],p=[1/3, 1/3, 1/3])

        player_weapon = None
        steal = False
        backhome = False
        end = False
        run = True
        result = None
        while run:
            
            # loop per second 
            clock.tick(40)

            # debuging display
            pygame.display.set_caption("FARMER & THIEF : "+"Select your weapon !")
            
            # draw minigame bg and button (draw minigame UI)
            if not end:
                self.draw_minigame()
            else:
                self.draw_minigame_show_result(result)
            pygame.display.update()

            # input - output
            for event in pygame.event.get():
                #print (self.inv.get_inv())
                # pointer
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # exit
                if event.type == pygame.QUIT:
                    # ไอ้พวกขี้ขลาด หักเงินมัน 100 ซะ !!!!!
                    return 'lose' 
                
                # Botton ------------------------- Botton
                
                
                # ปุ่ม home
                if is_hit_box(mouse_pos,self.backhome_button[0], self.backhome_button[1]) and end and backhome:
                    #print ('Bot_farm : home')

                    if clickdown:
                        # play sound change_page
                        loaded_sound.change_page.play() 
                        return result
                
                # ปุ่ม ขโมย
                if is_hit_box(mouse_pos,self.steal_button[0], self.steal_button[1]) and end and steal:
                    #print ('Bot_farm : home')

                    if clickdown:
                        # play sound change_page
                        loaded_sound.change_page.play() 
                        return result
                
                # ปุ่ม hammer
                if is_hit_box(mouse_pos,self.hammer_button[0], self.hammer_button[1]):
                    #print ('Bot_farm : hammer')

                    if clickdown:
                        player_weapon = '0'
                # ปุ่ม paper
                if is_hit_box(mouse_pos,self.paper_button[0], self.paper_button[1]):
                    #print ('Bot_farm : paper')

                    if clickdown:
                        player_weapon = '5'
                # ปุ่ม scissors
                if is_hit_box(mouse_pos,self.scissors_button[0], self.scissors_button[1]):
                    #print ('Bot_farm : scissors')

                    if clickdown:
                        player_weapon = '2'

            # ตัดสินแพ้ / ชนะ
            if (player_weapon is not None) and (not end):
                result = rpc(player_weapon, bot_weapon)
                end = True
                # stop sound
                pygame.mixer.music.stop()

                if result == 'win':
                    # play sound win 
                    loaded_sound.win.play() 

                    steal = True
                elif result == 'draw':
                    # play sound draw
                    loaded_sound.draw.play() 
                    backhome = True
                else:
                    # play sound lose1 
                    loaded_sound.lose1.play() 
                    backhome = True


    def draw_bg(self, hitbox=False):
        global loaded_image
        global loaded_sound
        global resolution
        # background 
        window.blit(pygame.transform.scale(loaded_image.farm_bg, resolution), (0, 0))
        
        plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
        for plot in plot_list:
            self.draw_farmland(plot)

        # วาด text แสดงจำนวน
        # เงิน
        # วาดจำนวนเงิน
        font_size = pygame.font.SysFont("comicsansms",60)
        msg = font_size.render(money_str(self.money), True, (0,128,0))
        txt_size = self.money_dispay[1][0] - self.money_dispay[0][0], self.money_dispay[1][1] - self.money_dispay[0][1]
        window.blit(pygame.transform.scale(msg, txt_size), self.money_dispay[0])

        # วาดจำนวน seed
        for seed_name in self.seed_dispay:
            font_size = pygame.font.SysFont("comicsansms",25)
            msg = font_size.render(money_str(self.inv.item_dict[seed_name], False, 3), True, (128,0,128))
            txt_size = self.seed_dispay[seed_name][1][0] - self.seed_dispay[seed_name][0][0], self.seed_dispay[seed_name][1][1] - self.seed_dispay[seed_name][0][1]
            window.blit(pygame.transform.scale(msg, txt_size), self.seed_dispay[seed_name][0])
        
    def draw_farmland(self, plot, watering=False):
        global loaded_image
        global loaded_sound
        stats = self.check_crops_status(plot)
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

        farmland_overlap = 50
        farm_scale = int(((a+x)/2)-a) , int(((b+y)/2)-b)
        farmland_image = pygame.transform.scale(stats[6], (farm_scale[0],farm_scale[1]+farmland_overlap))
        
        #print ('DRAWFARMLAND ', plot)
        if plot[1] == 'a' or plot[1] == '0':
            window.blit(farmland_image, (self.farmplot_position[index][0][0], self.farmplot_position[index][0][1]-farmland_overlap))
        elif plot[1] == 'b' or plot[1] == '1':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0] , self.farmplot_position[index][0][1]-farmland_overlap))
        elif plot[1] == 'c' or plot[1] == '2':
            window.blit(farmland_image, (self.farmplot_position[index][0][0], self.farmplot_position[index][0][1]+farm_scale[1]-farmland_overlap))
        elif plot[1] == 'd' or plot[1] == '3':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0], self.farmplot_position[index][0][1]+farm_scale[1]-farmland_overlap))

    def draw_minigame(self):
        global loaded_image
        global loaded_sound
        global resolution
        # background
        window.blit(pygame.transform.scale(loaded_image.minigame_bg, resolution), (0, 0))
            
        # ค้อน
        size = (self.hammer_button[1][0] - self.hammer_button[0][0]), (self.hammer_button[1][1] - self.hammer_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon0_icon, size), self.hammer_button[0])
        
        # กรรไกร
        size = (self.scissors_button[1][0] - self.scissors_button[0][0]), (self.scissors_button[1][1] - self.scissors_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon2_icon, size), self.scissors_button[0])
        
        # กระดาษ
        size = (self.paper_button[1][0] - self.paper_button[0][0]), (self.paper_button[1][1] - self.paper_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon5_icon, size), self.paper_button[0]) 

    def draw_minigame_show_result(self, result):
        global loaded_image
        global loaded_sound
        global resolution

        
        if result == 'win':
            window.blit(pygame.transform.scale(loaded_image.win_defend_bg, resolution), (0, 0))
            #print ('You Win !!!')
        elif result == 'lose':
            window.blit(pygame.transform.scale(loaded_image.lose_bg, resolution), (0, 0))
            #print ('You Lose !!!')
        else:
            window.blit(pygame.transform.scale(loaded_image.draw_bg, resolution), (0, 0))
            #print ('Draw !!!')
        #if result == 'win':
            # ไปขโมย
            #size = (self.steal_button[1][0] - self.steal_button[0][0]), (self.steal_button[1][1] - self.steal_button[0][1])
            #window.blit(pygame.transform.scale(loaded_image.next_icon, size), self.steal_button[0])
        #else:
            # กลับไปทำมาหากินต่อ
            #size = (self.backhome_button[1][0] - self.backhome_button[0][0]), (self.backhome_button[1][1] - self.backhome_button[0][1])
            #window.blit(pygame.transform.scale(loaded_image.home_icon, size), self.backhome_button[0])

    def draw_pop_up_msg(self, msg, position):
        pass

class Bot_farm():
    def __init__(self, profile):
        self.player = profile# Player()
        self.inv = self.player.inventory
        self.money = self.player.money
        self.farmplot = self.player.farmplot
        self.steal_cooldown = 120000

        self.money_dispay = ((94,42),(247,76))

        self.shop_button = ((545, 66),(720,220))
        self.storage_button = ((63,295),(265,499))
        self.watering_button = ((48,235),(120,280))
        self.mainmenu_button = ((218,523),(283,593))
        self.seedselection_button = ((486,499),(647,584))
        self.save_button = ((0,0),(0,0))
        self.saveexit_button = ((0,0),(0,0))
        self.home_button = ((293,523),(356,593))
        self.next_button = ((367,523),(432,593))
        self.farmplot_position = [[(449,257),(581,358)],    # ซ้ายบน
                                [(624,257),(754,358)],      # ขวาบน
                                [(449,386),(581,492)],      # ล่างซ้าย
                                [(624,386),(754,492)]]      # ล่างขวา
        self.hammer_button = ((552,247),(760,484))
        self.paper_button = ((298,247),(504,484))
        self.scissors_button = ((40,247),(250,484))
        self.steal_button = ((663,473),(757,580))
        self.backhome_button = self.steal_button
    
    def minigame(self):
        pygame.display.set_caption("FARMER & THIEF : "+"Minigame")
        global loaded_image
        global loaded_sound

        # loop per second 
        clock = pygame.time.Clock()

        # วาดพื้นหลัง
        self.draw_minigame()
        pygame.display.update()

        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(join('assets','sound','minigame_starting.wav'))
        pygame.mixer.music.play()
        
        # bot weapon
        bot_weapon = choice(['0', '2', '5'],p=[1/3, 1/3, 1/3])

        player_weapon = None
        steal = False
        backhome = False
        end = False
        run = True
        result = None
        while run:
            
            # loop per second 
            clock.tick(40)

            # debuging display
            pygame.display.set_caption("FARMER & THIEF : "+"Select your weapon !")
            
            # draw minigame bg and button (draw minigame UI)
            if not end:
                self.draw_minigame()
            else:
                self.draw_minigame_show_result(result)
            pygame.display.update()

            # input - output
            for event in pygame.event.get():
                #print (self.inv.get_inv())
                # pointer
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # exit
                if event.type == pygame.QUIT:
                    # ไอ้พวกขี้ขลาด หักเงินมัน 100 ซะ !!!!!
                    return 'lose' 
                
                # Botton ------------------------- Botton
                
                
                # ปุ่ม home
                if is_hit_box(mouse_pos,self.backhome_button[0], self.backhome_button[1]) and end and backhome:
                    #print ('Bot_farm : home')

                    if clickdown:
                        loaded_sound.click.play()
                        return result
                
                # ปุ่ม ขโมย
                if is_hit_box(mouse_pos,self.steal_button[0], self.steal_button[1]) and end and steal:
                    #print ('Bot_farm : home')

                    if clickdown:
                        loaded_sound.click.play()
                        return result
                
                # ปุ่ม hammer
                if is_hit_box(mouse_pos,self.hammer_button[0], self.hammer_button[1]):
                    #print ('Bot_farm : hammer')

                    if clickdown:
                        player_weapon = '0'
                # ปุ่ม paper
                if is_hit_box(mouse_pos,self.paper_button[0], self.paper_button[1]):
                    #print ('Bot_farm : paper')

                    if clickdown:
                        player_weapon = '5'
                # ปุ่ม scissors
                if is_hit_box(mouse_pos,self.scissors_button[0], self.scissors_button[1]):
                    #print ('Bot_farm : scissors')

                    if clickdown:
                        player_weapon = '2'

            # ตัดสินแพ้ / ชนะ
            if (player_weapon is not None) and (not end):
                result = rpc(player_weapon, bot_weapon)
                end = True

                # stop sound
                pygame.mixer.music.stop()

                if result == 'win':
                    # play sound win 
                    loaded_sound.win.play() 

                    steal = True
                elif result == 'draw':
                    # play sound draw
                    loaded_sound.draw.play() 
                    backhome = True
                else:
                    # play sound lose2
                    loaded_sound.lose2.play() 
                    backhome = True

    def look_bot_farm(self):
        pygame.display.set_caption("FARMER & THIEF : "+"AI Farm")
        global loaded_image
        global loaded_sound

        # loop per second 
        clock = pygame.time.Clock()

        # วาดพื้นหลัง
        self.draw_bg()
        pygame.display.update()

        run = True
        while run:
            
            # loop per second 
            clock.tick(40)
            
            # วาดพื้นหลัง
            self.draw_bg()
            pygame.display.update()

            # input - output
            for event in pygame.event.get():
                #print (self.inv.get_inv())
                # pointer
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # exit
                if event.type == pygame.QUIT:
                    # inv, money, go to?, cooldown
                    return 'exit'
                
                # Botton ------------------------- Botton
                
                # ปุ่ม home
                if is_hit_box(mouse_pos,self.home_button[0], self.home_button[1]):
                    #print ('Bot_farm : home')

                    if clickdown:
                        loaded_sound.click.play()
                        return'home'
        return 'home'


    def run_bot_farm(self, inv, money):
        pygame.display.set_caption("FARMER & THIEF : "+"AI Farm")
        global loaded_image
        global loaded_sound

        # run minigame first
        result = self.minigame()
        if result == 'draw':
            return inv, money, 'home', 60000
        elif result == 'lose':
            money -= 100
            print ('Player => You fail to steal crops.You are charged 100 ฿!')
            return inv, money, 'home', 60000
        
        # loop per second 
        clock = pygame.time.Clock()

        # วาดพื้นหลัง
        self.draw_bg()
        pygame.display.update()

        # debuging display
        pygame.display.set_caption("FARMER & THIEF : "+"Click on the crop to steal")

        cooldown = 0
        run = True
        while run:
            
            # loop per second 
            clock.tick(40)
            
            # วาดพื้นหลัง
            self.draw_bg()
            pygame.display.update()

            # input - output
            for event in pygame.event.get():
                #print (self.inv.get_inv())
                # pointer
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False
                
                # exit
                if event.type == pygame.QUIT:
                    # inv, money, go to?, cooldown
                    return inv, money, 'exit', cooldown
                
                # Botton ------------------------- Botton
                
                # ปุ่ม home
                if is_hit_box(mouse_pos,self.home_button[0], self.home_button[1]):
                    #print ('Bot_farm : home')

                    if clickdown:
                        loaded_sound.click.play()
                        return inv, money, 'home', cooldown
                

                # farmplot zone ----------------- farmplot zone
                # top left
                if is_hit_box(mouse_pos, self.farmplot_position[0][0], self.farmplot_position[0][1]) and cooldown == 0:
                    index = self.farmplot_check_crops(self.farmplot_position[0], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('1'+str(index))
                        if crops_status[5]:
                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            inv.add(crops_status[0], crop_collected)
                            print ('Player => You steal %s x %s from AI.'%(crops_status[0], crop_collected))
                            self.set_crops('1'+str(index), 'empty')
                            cooldown = 60000
                            pygame.display.set_caption("FARMER & THIEF : "+"Time to go home")

                # top right
                if is_hit_box(mouse_pos, self.farmplot_position[1][0], self.farmplot_position[1][1]) and cooldown == 0:
                    index = self.farmplot_check_crops(self.farmplot_position[1], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('2'+str(index))
                        if crops_status[5]:# harvest?
                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            inv.add(crops_status[0], crop_collected)
                            print ('Player => You steal %s x %s from AI.'%(crops_status[0], crop_collected))
                            self.set_crops('2'+str(index), 'empty')
                            cooldown = 60000
                            pygame.display.set_caption("FARMER & THIEF : "+"Time to go home")
                
                # down left
                if is_hit_box(mouse_pos, self.farmplot_position[2][0], self.farmplot_position[2][1]) and cooldown == 0:
                    index = self.farmplot_check_crops(self.farmplot_position[2], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('3'+str(index))
                        if crops_status[5]:# harvest?
                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            inv.add(crops_status[0], crop_collected)
                            print ('Player => You steal %s x %s from AI.'%(crops_status[0], crop_collected))
                            self.set_crops('3'+str(index), 'empty')
                            cooldown = 60000
                            pygame.display.set_caption("FARMER & THIEF : "+"Time to go home")
                
                # down right
                if is_hit_box(mouse_pos, self.farmplot_position[3][0], self.farmplot_position[3][1]) and cooldown == 0:
                    index = self.farmplot_check_crops(self.farmplot_position[3], mouse_pos)
                    if clickdown and (index != None):
                        crops_status = self.check_crops_status('4'+str(index))
                        if crops_status[5]:# harvest?
                            crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
                            inv.add(crops_status[0], crop_collected)
                            print ('Player => You steal %s x %s from AI.'%(crops_status[0], crop_collected))
                            self.set_crops('4'+str(index), 'empty')
                            cooldown = 60000
                            pygame.display.set_caption("FARMER & THIEF : "+"Time to go home")

        return inv, money, 'home', cooldown

    def set_crops(self, plot, seed_name):
        print('AI => Plot:%s was set to crop:%s !'%(plot, seed_name))
        # plot เป็น str มี 2 อักษร คือ เลข และ a-d
        # seed_name เป็น str ที่เป๋็นชื่อของพืช
        if seed_name == 'wheat':
            seed = Wheat()
        elif seed_name == 'cucumber':
            seed = Cucumber()
        elif seed_name == 'tomato':
            seed = Tomato()
        elif seed_name == 'potato':
            seed = Potato()
        elif seed_name == 'redcabbage':
            seed = Redcabbage()
        elif seed_name == 'orange':
            seed = Orange()
        elif seed_name == 'mango':
            seed = Mango()
        elif seed_name == 'apple':
            seed = Apple()
        elif seed_name == 'melon':
            seed = Melon()
        elif seed_name == 'grape':
            seed = Grape()
        else :
            seed = Empty()

        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop = seed
        self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time = self.farmplot[int(plot[0]) - 1].farmland[land].crop.growing_time
    
    def set_wet(self, plot):
        print ('AI => Plot:%s is Wet!'%plot)
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].watering = True

    def check_crops_status(self, plot):
        # method นี้ return [ชื่อ, สถานะการรดน้ำ, เวลาฟาร์มแห้ง, state ปัจจุบัน, remaining_growth_time, harvestable?, image of cur_state]
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        name = self.farmplot[int(plot[0]) - 1].farmland[land].crop.name
        watering = self.farmplot[int(plot[0]) - 1].farmland[land].watering
        dry_time = self.farmplot[int(plot[0]) - 1].farmland[land].dry_time
        if name is None:
            state = None
        elif self.farmplot[int(plot[0]) - 1].farmland[land].crop.now_state is None:
            state = 4
        else:
            state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.now_state
        remaining_growth_time = self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time
        harvest =  self.farmplot[int(plot[0]) - 1].farmland[land].crop.harvestable
        if state == 1:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state1_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state1_dry
        elif state == 2:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state2_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state2_dry
        elif state == 3:
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state3_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state3_dry
        elif (state == 4) or (state is None):
            if watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state4_wet
            if not watering:
                image_state = self.farmplot[int(plot[0]) - 1].farmland[land].crop.crops_state4_dry
            

        return [name, watering, dry_time, state, remaining_growth_time, harvest, image_state]
    
    def growing_by_plot(self, plot, time_decrease):
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop.remaining_growth_time -= time_decrease
        
    def grow_up_by_plot(self, plot):
        if plot[1] == 'a' or plot[1] == '0':
            land = 0
        elif plot[1] == 'b' or plot[1] == '1':
            land = 1
        elif plot[1] == 'c' or plot[1] == '2':
            land = 2
        elif plot[1] == 'd' or plot[1] == '3':
            land = 3
        else:
            land = int(plot[1])

        self.farmplot[int(plot[0]) - 1].farmland[land].crop.grow_up()

    def random_plant(self, plot):
        seed_list = ['wheat', 'cucumber', 'tomato', 'potato', 'redcabbage', 'orange', 'mango', 'apple', 'melon', 'grape']
        selected_seed = choice(seed_list, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
        self.set_crops(plot, selected_seed)
        price_index = { 'wheat': Wheat().seed_price, 
                            'cucumber': Cucumber().seed_price, 
                            'tomato': Tomato().seed_price, 
                            'potato': Potato().seed_price,
                            'redcabbage':Redcabbage().seed_price,
                            'orange': Orange().seed_price,
                            'mango': Mango().seed_price,
                            'apple': Apple().seed_price, 
                            'melon': Melon().seed_price, 
                            'grape': Grape().seed_price}
        self.money -= price_index[selected_seed]

    def harvest(self, plot):
        crop_collected = choice([1, 2, 3],p=[0.5, 0.35, 0.15])
        self.inv.add(self.check_crops_status(plot)[0], crop_collected)
        crops_name = self.check_crops_status(plot)[0].lower()
        self.set_crops(plot, 'empty')
        price_index = { 'wheat': Wheat().sale_price, 
                            'cucumber': Cucumber().sale_price, 
                            'tomato': Tomato().sale_price, 
                            'potato': Potato().sale_price,
                            'redcabbage':Redcabbage().sale_price,
                            'orange': Orange().sale_price,
                            'mango': Mango().sale_price,
                            'apple': Apple().sale_price, 
                            'melon': Melon().sale_price, 
                            'grape': Grape().sale_price,
                            None:0}
        print ('AI => Harvested:',crops_name,' x ',crop_collected, ', AI_money:',self.money)                    
        self.money += (price_index[crops_name]*crop_collected)

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
                return 'a'

            # farm  b
            a = (mid_point[0], start_point[1]) # (mid x ,start y)
            b = (final_point[0], mid_point[1]) # (final x, mid y) 
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม b มาแสดงผล
                return 'b'

            # farm  c
            a = (start_point[0], mid_point[1]) # (start x, mid y) 
            b = (mid_point[0], final_point[1]) # (mid x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม c มาแสดงผล
                return 'c'

            # farm  d
            a = mid_point # (mid x ,mid y)
            b = final_point #(final x, final y)
            if is_hit_box(mouse_pos,a, b):  
                #f ดึงข้อมูล ฟาร์ม d มาแสดงผล
                return 'd'
            return None
    
    def seed_index(self, mouse_pos):
        # method นี้ return ชื่อ ของผัก ที่กดบนปุ่มเลือก seed
        x_length = (self.seedselection_button[0][0] - self.seedselection_button[1][0]) / 5
        y_length = (self.seedselection_button[0][1] - self.seedselection_button[1][1]) / 2

        box_x = ceil((self.seedselection_button[0][0] - mouse_pos[0]) / x_length)
        box_y = ceil((self.seedselection_button[0][1] - mouse_pos[1]) / y_length)
        
        if box_y == 1:
            if box_x == 2:
                return 'wheat'
            if box_x == 3:
                return 'cucumber'
            if box_x == 4:
                return 'tomato'
            if box_x == 5:
                return 'potato'
            if box_x == 1:
                return 'redcabbage'
        elif box_y == 2:
            if box_x == 3:
                return 'orange'
            if box_x == 2:
                return 'mango'
            if box_x == 5:
                return 'apple'
            if box_x == 1:
                return 'melon'
            if box_x == 4:
                return 'grape'
            
        return None
            

    def draw_bg(self, hitbox=False):
        global loaded_image
        global loaded_sound
        global resolution
        # background 
        window.blit(pygame.transform.scale(loaded_image.farm_bg, resolution), (0, 0))
        
        plot_list = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d']
        for plot in plot_list:
            self.draw_farmland(plot)

        # วาดจำนวนเงิน
        font_size = pygame.font.SysFont("comicsansms",60)
        msg = font_size.render(money_str(self.money), True, (0,128,0))
        txt_size = self.money_dispay[1][0] - self.money_dispay[0][0], self.money_dispay[1][1] - self.money_dispay[0][1]
        window.blit(pygame.transform.scale(msg, txt_size), self.money_dispay[0])


    def draw_farmland(self, plot, watering=False):
        global loaded_image
        global loaded_sound
        stats = self.check_crops_status(plot)
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

        farmland_overlap = 50
        farm_scale = int(((a+x)/2)-a) , int(((b+y)/2)-b)
        farmland_image = pygame.transform.scale(stats[6], (farm_scale[0],farm_scale[1]+farmland_overlap))
        
        #print ('DRAWFARMLAND ', plot)
        if plot[1] == 'a' or plot[1] == '0':
            window.blit(farmland_image, (self.farmplot_position[index][0][0], self.farmplot_position[index][0][1]-farmland_overlap))
        elif plot[1] == 'b' or plot[1] == '1':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0] , self.farmplot_position[index][0][1]-farmland_overlap))
        elif plot[1] == 'c' or plot[1] == '2':
            window.blit(farmland_image, (self.farmplot_position[index][0][0], self.farmplot_position[index][0][1]+farm_scale[1]-farmland_overlap))
        elif plot[1] == 'd' or plot[1] == '3':
            window.blit(farmland_image, (self.farmplot_position[index][0][0]+farm_scale[0], self.farmplot_position[index][0][1]+farm_scale[1]-farmland_overlap))

    def draw_minigame(self):
        global loaded_image
        global loaded_sound
        global resolution
        # background
        window.blit(pygame.transform.scale(loaded_image.minigame_bg, resolution), (0, 0))
            
        # ค้อน
        size = (self.hammer_button[1][0] - self.hammer_button[0][0]), (self.hammer_button[1][1] - self.hammer_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon0_icon, size), self.hammer_button[0])
        
        # กรรไกร
        size = (self.scissors_button[1][0] - self.scissors_button[0][0]), (self.scissors_button[1][1] - self.scissors_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon2_icon, size), self.scissors_button[0])
        
        # กระดาษ
        size = (self.paper_button[1][0] - self.paper_button[0][0]), (self.paper_button[1][1] - self.paper_button[0][1])
        window.blit(pygame.transform.scale(loaded_image.weapon5_icon, size), self.paper_button[0])        
    
    def draw_minigame_show_result(self, result):
        global loaded_image
        global loaded_sound
        global resolution
        
        if result == 'win':
            window.blit(pygame.transform.scale(loaded_image.win_bg, resolution), (0, 0))

        elif result == 'lose':
            window.blit(pygame.transform.scale(loaded_image.lose_bg, resolution), (0, 0))

        else:
            window.blit(pygame.transform.scale(loaded_image.draw_bg, resolution), (0, 0))
        
        #if result == 'win':
            ## ไปขโมย
            #size = (self.steal_button[1][0] - self.steal_button[0][0]), (self.steal_button[1][1] - self.steal_button[0][1])
            #window.blit(pygame.transform.scale(loaded_image.next_icon, size), self.steal_button[0])
        #else:
            # กลับไปทำมาหากินต่อ
            #size = (self.backhome_button[1][0] - self.backhome_button[0][0]), (self.backhome_button[1][1] - self.backhome_button[0][1])
            #window.blit(pygame.transform.scale(loaded_image.home_icon, size), self.backhome_button[0])

# shop
class Shop_menu():
    def __init__(self,inventory, money):
        self.inv = inventory
        self.money = money
        
        self.money_dispay = ((109,33),(311,80))
        self.seed_dispay = { 'wheat_seed': ((498,36),(553,60)), 
                            'cucumber_seed': ((576,36),(629,60)), 
                            'tomato_seed': ((650,36),(704,60)), 
                            'potato_seed': ((727,36),(785,60)),
                            'redcabbage_seed':((423,36),(478,60)),
                            'orange_seed': ((576,192),(629,215)),
                            'mango_seed': ((498,192),(553,215)),
                            'apple_seed': ((727,192),(785,215)), 
                            'melon_seed': ((423,192),(478,215)), 
                            'grape_seed': ((650,192),(704,215))}

        self.home_button = ((586,360),(637,418))
        self.buy_button = ((575,267),(647,341))
        self.seedselection_button = [((43,190),(114,298)), ((114,190),(185,298)), ((185,190),(257,298)), ((257,190),(328,298)), ((328,190),(399,298)),
                                    ((43,326),(114,433)), ((114,326),(185,433)), ((185,326),(257,433)), ((257,326),(328,433)), ((328,326),(399,433))]
        self.seedselection_order = ['redcabbage_seed', 'wheat_seed', 'cucumber_seed', 'tomato_seed', 'potato_seed', 
                                    'melon_seed', 'mango_seed', 'orange_seed', 'grape_seed', 'apple_seed']
        self.price_index = { 'wheat_seed': Wheat().seed_price, 
                            'cucumber_seed': Cucumber().seed_price, 
                            'tomato_seed': Tomato().seed_price, 
                            'potato_seed': Potato().seed_price,
                            'redcabbage_seed':Redcabbage().seed_price,
                            'orange_seed': Orange().seed_price,
                            'mango_seed': Mango().seed_price,
                            'apple_seed': Apple().seed_price, 
                            'melon_seed': Melon().seed_price, 
                            'grape_seed': Grape().seed_price}


    def run(self):
        # display
        pygame.display.set_caption("FARMER & THIEF : "+"Shop")

        window.fill((0,0,0))
        pygame.display.update()
        
        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(join('assets','sound','Mr_Turtle_shop.wav'))
        pygame.mixer.music.play(loops=-1)

        buy = False
        run = True
        while run:
            # draw bg
            self.draw_bg()
            pygame.display.update()
            # input - output
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()
                    return self.inv, self.money, 'exit'
                
                # mouse pos
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False

                # Botton ------------------------- Botton
                # ปุ่ม ออกไป farm
                if is_hit_box(mouse_pos,self.home_button[0], self.home_button[1]):
                    #print ('Shop : home')

                    if clickdown:
                        # stop theme song
                        pygame.mixer.music.stop()

                        # play sound change_page
                        loaded_sound.change_page.play() 

                        return self.inv, self.money, 'home'
                
                # ปุ่ม buy
                if is_hit_box(mouse_pos,self.buy_button[0], self.buy_button[1]):
                    #print ('Shop : buy')

                    if clickdown:
                        # play sound click
                        loaded_sound.click.play() 
                        
                        buy = not buy
                
                # buy zone ------------------------- buy zone
                index = 0
                for slot in self.seedselection_button:
                    if is_hit_box(mouse_pos,slot[0], slot[1]) and buy:
                        seed_name = self.seedselection_order[index]
                        #print ('Shop : buy ',seed_name)
                        if clickdown and (self.money >= self.price_index[seed_name]):
                            # play sound coin
                            loaded_sound.coin.play() 
                            #print ('buy: ',seed_name, ' ,price: ', self.price_index[seed_name], ' ,You balance: ',self.money)
                            self.inv.add(seed_name, 1)
                            self.money -= self.price_index[seed_name]
                        elif clickdown and (self.money < self.price_index[seed_name]):
                            #print ('You don\'t have money to buy buy: ',seed_name, ' ,price: ', self.price_index[seed_name], ' ,You balance: ',self.money)
                            pass
                    index += 1
                    
        # คืนค่า self.inventory, self.money เมื่อผู้เล่นออกจากร้านด้วย
        return self.inv, self.money, 'home'

    def draw_bg(self):
        global loaded_image
        global loaded_sound
        global resolution
        # bg
        window.blit(pygame.transform.scale(loaded_image.shop_bg, resolution), (0, 0))

        # วาดจำนวนเงิน
        font_size = pygame.font.SysFont("comicsansms",60)
        msg = font_size.render(money_str(self.money), True, (0,128,0))
        txt_size = self.money_dispay[1][0] - self.money_dispay[0][0], self.money_dispay[1][1] - self.money_dispay[0][1]
        window.blit(pygame.transform.scale(msg, txt_size), self.money_dispay[0])
        
        # วาดจำนวน seed
        for seed_name in self.seed_dispay:
            font_size = pygame.font.SysFont("comicsansms",60)
            msg = font_size.render(money_str(self.inv.item_dict[seed_name], False, 5), True, (128,0,128))
            txt_size = self.seed_dispay[seed_name][1][0] - self.seed_dispay[seed_name][0][0], self.seed_dispay[seed_name][1][1] - self.seed_dispay[seed_name][0][1]
            window.blit(pygame.transform.scale(msg, txt_size), self.seed_dispay[seed_name][0])
        

# คลัง
class Storage_menu():
    def __init__(self,inventory, money):
        global loaded_image
        self.inv = inventory
        self.money = money
        self.max_page = None

        self.money_display = ((100,35),(272, 80))
        
        self.money_dispay = ((100,36),(272,78))
        self.sell_button = ((670, 151),(761,249))
        self.home_button = ((670, 324),(764,423))
        self.next_button = ((449, 514),(523,594))
        self.previous_button = ((286, 514),(360,594))
        self.inv_slot_button = [((176, 110),(299,210)), ((339, 110),(464,210)), ((504, 110),(626,210)),
                                ((176, 242),(299,343)), ((339, 242),(464,343)), ((504, 242),(626,343)),
                                ((176, 375),(299,474)), ((339, 375),(464,474)), ((504, 375),(626,474))]
        self.price_index = {'wheat': Wheat().sale_price, 'wheat_seed': Wheat().seed_price, 
                    'cucumber': Cucumber().sale_price, 'cucumber_seed': Cucumber().seed_price, 
                    'tomato': Tomato().sale_price, 'tomato_seed': Tomato().seed_price,
                    'potato': Potato().sale_price,  'potato_seed': Potato().seed_price,
                    'redcabbage': Redcabbage().sale_price, 'redcabbage_seed':Redcabbage().seed_price,
                    'orange': Orange().sale_price, 'orange_seed': Orange().seed_price,
                    'mango': Mango().sale_price, 'mango_seed': Mango().seed_price,
                    'apple': Apple().sale_price, 'apple_seed': Apple().seed_price, 
                    'melon': Melon().sale_price, 'melon_seed': Melon().seed_price, 
                    'grape': Grape().sale_price, 'grape_seed': Grape().seed_price}
        self.icon_index = {'wheat': loaded_image.wheat, 'wheat_seed': loaded_image.wheat_seed, 
                    'cucumber': loaded_image.cucumber, 'cucumber_seed': loaded_image.cucumber_seed, 
                    'tomato': loaded_image.tomato, 'tomato_seed': loaded_image.tomato_seed,
                    'potato': loaded_image.potato,  'potato_seed': loaded_image.potato_seed,
                    'redcabbage': loaded_image.redcabbage, 'redcabbage_seed': loaded_image.redcabbage_seed,
                    'orange': loaded_image.orange, 'orange_seed': loaded_image.orange_seed,
                    'mango': loaded_image.mango, 'mango_seed': loaded_image.mango_seed,
                    'apple': loaded_image.apple, 'apple_seed': loaded_image.apple_seed, 
                    'melon': loaded_image.melon, 'melon_seed': loaded_image.melon_seed, 
                    'grape': loaded_image.grape, 'grape_seed': loaded_image.grape_seed}

    def run(self):
        # display
        pygame.display.set_caption("FARMER & THIEF : "+"Storage")
        # FPS
        clock = pygame.time.Clock()

        # วาดพื้นหลัง
        self.draw_bg(1)
        pygame.display.update()  

        # music theme (ต้อง load ใหม่ เพื่อเปิดเสียงแยกจาก effect)
        pygame.mixer.music.load(join('assets','sound','Path_to_Follow_shop_storage.wav'))
        pygame.mixer.music.play(loops=-1)

        run = True
        page = 1
        sell = False
        while run:
            # loop per second  (FPS)
            clock.tick(40)

            # draw bg
            self.draw_bg(page)
            pygame.display.update()

            # สร้าง index ของ item ขึ้นมา เมื่อ init ด้วย inv
            item_name_index = []
            for name in self.inv.get_inv_only_have():
                item_name_index.append(name)
            self.max_page = ceil(len(item_name_index)/9)
            #print ('max index ', self.max_page)

            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    # stop theme song
                    pygame.mixer.music.stop()
                    return self.inv, self.money, 'exit'
                
                # mouse pos
                mouse_pos = pygame.mouse.get_pos()
                #print (mouse_pos)

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickdown = True
                else:
                    clickdown = False

                # Botton ------------------------- Botton
                # ปุ่ม ออกไป farm
                if is_hit_box(mouse_pos,self.home_button[0], self.home_button[1]):
                    #print ('Storage : home')

                    if clickdown:
                        # stop theme song
                        pygame.mixer.music.stop()
                        return self.inv, self.money,'home'
                
                # ปุ่ม sell
                if is_hit_box(mouse_pos,self.sell_button[0], self.sell_button[1]):
                    #print ('Storage : sell')

                    if clickdown:
                        # play sound click
                        loaded_sound.click.play() 

                        sell = not sell
                
                # ปุ่ม previous
                if is_hit_box(mouse_pos,self.previous_button[0], self.previous_button[1]):
                    #print ('Storage : previous')

                    if clickdown and (page > 1):
                        # play sound change_page
                        loaded_sound.change_page.play()

                        page -= 1
                    
                    elif clickdown and (page <= 1):
                        # play sound change_page
                        loaded_sound.change_page.play() 

                        page = self.max_page
                
                # ปุ่ม next
                if is_hit_box(mouse_pos,self.next_button[0], self.next_button[1]):
                    #print ('Storage : next')

                    if clickdown and (page < self.max_page):
                        # play sound change_page
                        loaded_sound.change_page.play()

                        page += 1

                    elif clickdown and (page >= self.max_page):
                        #print (page,' >= ', self.max_page)
                        # play sound change_page
                        loaded_sound.change_page.play()

                        page = 1

                # inv zone ------------------- inv zone 
                for table_index in range(9):
                    index = table_index + ((page-1)*9)
                    if is_hit_box(mouse_pos,self.inv_slot_button[table_index][0], self.inv_slot_button[table_index][1]):
                        #print ('Storage : index ',index, 'Page =',page, 'table =',table_index )
                        if clickdown and sell:
                            try:
                                item_name = item_name_index[index]
                            except IndexError:
                                #print ('have no item')
                                continue

                            # play sound coin
                            loaded_sound.coin.play()

                            self.inv.remove(item_name, 1)
                            self.money += self.price_index[item_name]
                            print ('sell:', item_name)

                            if ceil(len(self.inv.get_inv_only_have())/9) < ceil(len(item_name_index)/9): # ถ้าขายของไป แล้วทำให้ของหาย และ page นั้น ไม่มีของจะแสดง
                                #print (ceil(len(self.inv.get_inv_only_have())/9),' < ',ceil(len(item_name_index)/9))
                                self.max_page -= 1
                                if page > 1:
                                    page -= 1
                            
                        try:
                            item_name = item_name_index[index]
                        except IndexError:
                            #print ('have no item')
                            continue 
                        #print ('here are ',self.inv.item_dict[item_name], ' item')           


        # คืนค่า self.inventory, self.money เมื่อผู้เล่นออกจากคลังด้วย
        return self.inv, self.money, 'home'

    def draw_bg(self, page):
        global loaded_image
        global loaded_sound
        global resolution
        # bg
        if page == 1:
            window.blit(pygame.transform.scale(loaded_image.storage_bg_p1, resolution), (0, 0))
        elif page == 2:
            window.blit(pygame.transform.scale(loaded_image.storage_bg_p2, resolution), (0, 0))
        elif page == 3:
            window.blit(pygame.transform.scale(loaded_image.storage_bg_p3, resolution), (0, 0))
        else:
            window.blit(pygame.transform.scale(loaded_image.storage_bg, resolution), (0, 0))

        item_name_index = []
        for name in self.inv.get_inv_only_have():
            item_name_index.append(name)
        
        # วาดจำนวนเงิน
        font_size = pygame.font.SysFont("comicsansms",60)
        msg = font_size.render(money_str(self.money), True, (0,128,0))
        txt_size = self.money_dispay[1][0] - self.money_dispay[0][0], self.money_dispay[1][1] - self.money_dispay[0][1]
        window.blit(pygame.transform.scale(msg, txt_size), self.money_dispay[0])
        

        # ถ้าไม่มีอะไรเลย ไม่ต้องวาด 
        if len(item_name_index) == 0:
            return True

        # วาดผักลงในตาราง 
        for table_index in range(9):
            index = table_index + ((page-1)*9)
            try:
                item_name = item_name_index[index]
            except IndexError:
                # print ('Here are no item')
                continue
            xyab = self.inv_slot_button[table_index]
            size = (xyab[1][0] - xyab[0][0]), (xyab[1][1] - xyab[0][1])
            window.blit(pygame.transform.scale(self.icon_index[item_name], size), xyab[0])
            
            # วาดจำนวน ผัก
            font_size = pygame.font.SysFont("comicsansms",60)
            msg = font_size.render(str(self.inv.item_dict[item_name]), True, (255,255,255))
            txt_size = int(size[0]*0.3), int(size[1]*0.5)
            locate = int((xyab[0][0])+(size[0]*0.7)), int((xyab[0][1])+(size[1]*0.5))
            window.blit(pygame.transform.scale(msg, txt_size), locate)


        

# main menu
class Main_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global resolution
        pygame.display.set_caption("FARMER & THIEF : "+"Main Menu")
        # drawing page ------------------- drawing page
        # background 
        window.blit(pygame.transform.scale(loaded_image.main_bg, resolution), (0, 0))
        # exit botton
        #pygame.draw.rect(window, (150,0,0),[220, 400, 380, 100], 3)

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
                #print (mouse_pos)
                # ปุ่ม newgame
                newgame_a = (0,0)
                newgame_b = (0,0)
                if is_hit_box(mouse_pos,newgame_a, newgame_b):
                    #print ('Main_menu : newgame')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        loaded_sound.click.play()
                        return 'newgame'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม continue
                continue_a = (560, 270)
                continue_b = (780,575)
                if is_hit_box(mouse_pos,continue_a, continue_b):
                    #print ('Main_menu : continue')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        loaded_sound.click.play()
                        return 'load'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม credit
                credit_a = (240,65)
                credit_b = (610,250)
                if is_hit_box(mouse_pos,credit_a, credit_b):
                    #print ('Main_menu : credit')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        loaded_sound.click.play()
                        return 'credit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม exit
                quit_a = (452,459)#(220,400)
                quit_b = (560,570)#(500,500)
                if is_hit_box(mouse_pos,quit_a, quit_b):
                    #print ('Main_menu : exit')
                    # วาดปุ่มเรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        loaded_sound.click.play()
                        return 'exit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

# loadgame
class Load_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        pygame.display.set_caption("FARMER & THIEF : "+"Load game")
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
            profile = Player()
            break
        farm = Player_farm(profile)
        out = farm.run()
        return out

# credit
class Credit_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        pygame.display.set_caption("FARMER & THIEF : "+"Credit_menu")
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.MOUSEBUTTONUP:
                    return 'main'
            return 'main'


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self, name="profile"):
        self.name = name
        self.money = 1000
        self.inventory = Inventory()
        self.farmplot = [Farmplot(), Farmplot(), Farmplot(), Farmplot()]
        self.bot = [Bot('bot_1')]
    
    def save(self):
        pass

class Bot():
    def __init__(self, name="bot"):
        self.name = name
        self.money = 1000
        self.inventory = Inventory()
        self.farmplot = [Farmplot(), Farmplot(), Farmplot(), Farmplot()]
    
    def load(self):
        pass
    
    def get_data(self):
        pass

class Inventory():
    def __init__(self):
        self.item_dict = {'wheat': 0, 'cucumber': 0, 
                        'tomato': 0, 'potato': 0,  
                        'redcabbage': 0, 'orange': 0, 
                        'mango': 0, 'apple': 0,
                        'melon': 0, 'grape': 0, 
	                    'wheat_seed': 0, 'cucumber_seed': 0, 
                        'tomato_seed': 0,'potato_seed': 0,
                        'redcabbage_seed':0, 'orange_seed': 0,
                        'mango_seed': 0, 'apple_seed': 0, 
                        'melon_seed': 0, 'grape_seed': 0}
    
    # add item to Inventory
    def add(self, name, amout):
        self.item_dict[name.lower()] += amout
    
    # remove item from Inventory
    def remove(self, name, amout):
        self.item_dict[name.lower()] -= amout
    
    def get_inv(self):
        return dict(self.item_dict)
    
    # get Inventory (dict type) อันนี้ให้ใช้กับ storage เพื่อแสดงผล
    def get_inv_only_have(self):
        item_name = list(filter(lambda x : self.item_dict[x] > 0, self.item_dict))
        inv = dict()
        for key in item_name:
            inv[key] = self.item_dict[key]
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
        global loaded_image
        global loaded_sound
        self.name = 'Wheat'
        self.growing_time = 1000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.wheat_state1_wet
        self.crops_state2_wet = loaded_image.wheat_state2_wet
        self.crops_state3_wet = loaded_image.wheat_state3_wet
        self.crops_state4_wet = loaded_image.wheat_state4_wet
        self.crops_state1_dry = loaded_image.wheat_state1_dry
        self.crops_state2_dry = loaded_image.wheat_state2_dry
        self.crops_state3_dry = loaded_image.wheat_state3_dry
        self.crops_state4_dry = loaded_image.wheat_state4_dry
        self.sale_price = 10
        self.seed_price = 5
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time
         

class Cucumber():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Cucumber'
        self.growing_time = 2000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.cucumber_state1_wet
        self.crops_state2_wet = loaded_image.cucumber_state2_wet
        self.crops_state3_wet = loaded_image.cucumber_state3_wet
        self.crops_state4_wet = loaded_image.cucumber_state4_wet
        self.crops_state1_dry = loaded_image.cucumber_state1_dry
        self.crops_state2_dry = loaded_image.cucumber_state2_dry
        self.crops_state3_dry = loaded_image.cucumber_state3_dry
        self.crops_state4_dry = loaded_image.cucumber_state4_dry
        self.sale_price = 30
        self.seed_price = 10
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Tomato():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Tomato'
        self.growing_time = 3000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.tomato_state1_wet
        self.crops_state2_wet = loaded_image.tomato_state2_wet
        self.crops_state3_wet = loaded_image.tomato_state3_wet
        self.crops_state4_wet = loaded_image.tomato_state4_wet
        self.crops_state1_dry = loaded_image.tomato_state1_dry
        self.crops_state2_dry = loaded_image.tomato_state2_dry
        self.crops_state3_dry = loaded_image.tomato_state3_dry
        self.crops_state4_dry = loaded_image.tomato_state4_dry
        self.sale_price = 50
        self.seed_price = 15
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Potato():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Potato'
        self.growing_time = 5000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.potato_state1_wet
        self.crops_state2_wet = loaded_image.potato_state2_wet
        self.crops_state3_wet = loaded_image.potato_state3_wet
        self.crops_state4_wet = loaded_image.potato_state4_wet
        self.crops_state1_dry = loaded_image.potato_state1_dry
        self.crops_state2_dry = loaded_image.potato_state2_dry
        self.crops_state3_dry = loaded_image.potato_state3_dry
        self.crops_state4_dry = loaded_image.potato_state4_dry
        self.sale_price = 70
        self.seed_price = 20
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Redcabbage():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Redcabbage'
        self.growing_time = 6000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.redcabbage_state1_wet
        self.crops_state2_wet = loaded_image.redcabbage_state2_wet
        self.crops_state3_wet = loaded_image.redcabbage_state3_wet
        self.crops_state4_wet = loaded_image.redcabbage_state4_wet
        self.crops_state1_dry = loaded_image.redcabbage_state1_dry
        self.crops_state2_dry = loaded_image.redcabbage_state2_dry
        self.crops_state3_dry = loaded_image.redcabbage_state3_dry
        self.crops_state4_dry = loaded_image.redcabbage_state4_dry
        self.sale_price = 100
        self.seed_price = 25
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Orange():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Orange'
        self.growing_time = 7000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.orange_state1_wet
        self.crops_state2_wet = loaded_image.orange_state2_wet
        self.crops_state3_wet = loaded_image.orange_state3_wet
        self.crops_state4_wet = loaded_image.orange_state4_wet
        self.crops_state1_dry = loaded_image.orange_state1_dry
        self.crops_state2_dry = loaded_image.orange_state2_dry
        self.crops_state3_dry = loaded_image.orange_state3_dry
        self.crops_state4_dry = loaded_image.orange_state4_dry
        self.sale_price = 50
        self.seed_price = 30
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Mango():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Mango'
        self.growing_time = 8000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.mango_state1_wet
        self.crops_state2_wet = loaded_image.mango_state2_wet
        self.crops_state3_wet = loaded_image.mango_state3_wet
        self.crops_state4_wet = loaded_image.mango_state4_wet
        self.crops_state1_dry = loaded_image.mango_state1_dry
        self.crops_state2_dry = loaded_image.mango_state2_dry
        self.crops_state3_dry = loaded_image.mango_state3_dry
        self.crops_state4_dry = loaded_image.mango_state4_dry
        
        self.sale_price = 150
        self.seed_price = 40
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Apple():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Apple'
        self.growing_time = 10000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.apple_state1_wet
        self.crops_state2_wet = loaded_image.apple_state2_wet
        self.crops_state3_wet = loaded_image.apple_state3_wet
        self.crops_state4_wet = loaded_image.apple_state4_wet
        self.crops_state1_dry = loaded_image.apple_state1_dry
        self.crops_state2_dry = loaded_image.apple_state2_dry
        self.crops_state3_dry = loaded_image.apple_state3_dry
        self.crops_state4_dry = loaded_image.apple_state4_dry
        
        
        self.sale_price = 350
        self.seed_price = 50
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Melon():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Melon'
        self.growing_time = 12000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.melon_state1_wet
        self.crops_state2_wet = loaded_image.melon_state2_wet
        self.crops_state3_wet = loaded_image.melon_state3_wet
        self.crops_state4_wet = loaded_image.melon_state4_wet
        self.crops_state1_dry = loaded_image.melon_state1_dry
        self.crops_state2_dry = loaded_image.melon_state2_dry
        self.crops_state3_dry = loaded_image.melon_state3_dry
        self.crops_state4_dry = loaded_image.melon_state4_dry
        self.sale_price = 400
        self.seed_price = 60
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Grape():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = 'Grape'
        self.growing_time = 15000 # growing_time per 1 state (sec)
        self.remaining_growth_time = None
        self.harvestable = False
        self.now_state = 2
        self.crops_state1_wet = loaded_image.grape_state1_wet
        self.crops_state2_wet = loaded_image.grape_state2_wet
        self.crops_state3_wet = loaded_image.grape_state3_wet
        self.crops_state4_wet = loaded_image.grape_state4_wet
        self.crops_state1_dry = loaded_image.grape_state1_dry
        self.crops_state2_dry = loaded_image.grape_state2_dry
        self.crops_state3_dry = loaded_image.grape_state3_dry
        self.crops_state4_dry = loaded_image.grape_state4_dry
        self.sale_price = 500
        self.seed_price = 70
    
    def grow_up(self):
        # ถ้าโตพร้อมเก็บ
        if self.now_state == 4:
            self.now_state = None
            self.harvestable = True
            self.remaining_growth_time = None
        else:   
            self.now_state += 1
            self.remaining_growth_time = self.growing_time + self.remaining_growth_time

class Empty():
    def __init__(self):
        global loaded_image
        global loaded_sound
        self.name = None
        self.growing_time = None
        self.harvestable = False
        self.remaining_growth_time = None
        self.now_state = None
        self.crops_state4_wet = loaded_image.wet_farm
        self.crops_state4_dry = loaded_image.dry_farm

        self.sale_price = None
        self.seed_price = None
        


# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("FARMER & THIEF : "+"Loading...")


window.fill((255,255,153))
pygame.display.update()
loaded_image = Image_()
loaded_sound = Sound_()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():
    global loaded_image
    global loaded_sound
    pygame.display.set_caption("FARMER & THIEF : "+"Menu Selection")
    selected = 'main'
    run = True
    while run:
        if selected == 'main':
            main = Main_menu()
            selected = main.run()
        
        if selected == 'load':
            load = Load_menu()
            selected = load.run()
        
        if selected == 'credit':
            credit = Credit_menu()
            selected = credit.run()

        if selected == 'exit':
            run = False
            
        

# RUN !
main()

# EXIT !
pygame.quit()
