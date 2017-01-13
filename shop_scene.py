from scene import *

import time
import ui

import globals 
import stats_scene 
import credits_scene 
import shop_scene 
import help_scene 
import game_scene 
import settings_scene 



class HitAndRunShopScene(Scene):
    def setup(self):
        
        self.heart = []
        self.heartshow = 1
        self.fixed_time_step = 'Nill'
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.buy1_label_down = False
        self.buy2_label_down = False
        self.buy3_label_down = False
        self.buy4_label_down = False
        self.buy5_label_down = False
        self.buy6_label_down = False
        
        self.price1 = 100
        self.price2 = 100
        self.price3 = 100
        self.price4 = 100
        self.price5 = 100
        self.price6 = 100
        
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode('assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'Shop',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 50, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = (75, self.size_of_screen_y - 75),
                                       scale = 0.17,
                                       color = 'grey')
                                       
        self.back1_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6))
        self.health_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_035.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.57))
        self.health_label = LabelNode(text = 'HEALTH',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.79),
                                     color = 'red')
        self.back1_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7))
        self.damage_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_034.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.6))
        self.damage_label = LabelNode(text = 'DAMAGE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/3.3),
                                     color = 'red')
        self.back1_square3 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/9.25))
        self.critdamage_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_019.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/8.25))
        self.critdamage_label = LabelNode(text = 'CRIT DAMAGE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/24),
                                     color = 'red')
        self.back1_square4 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/6.5))
        self.regen_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_027.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/7.35))
        self.regen_label = LabelNode(text = 'REGEN',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y/1.279),
                                     color = 'red')
        self.back1_square5 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.4))
        self.armor_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_025.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.48))
        self.armor_label = LabelNode(text = 'ARMOR',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y/1.92),
                                     color = 'red')
        self.back1_square6 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.465))
        self.attackspeed_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_006.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.5))
        self.attackspeed_label = LabelNode(text = 'ATK SPEED',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x -self.screen_center_x/2, self.screen_center_y/3.9),
                                     color = 'red')
        self.back2_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/1.6))
        self.price1_label = LabelNode(text = str(self.price1),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/1.6),
                                     color = 'gold')
        self.back2_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/2.7))
        self.price2_label = LabelNode(text = str(self.price2),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/2.7),
                                     color = 'gold')
        self.back2_square3 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/9.25))
        self.price3_label = LabelNode(text = str(self.price3),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/9.25),
                                     color = 'gold')
        self.back2_square4 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/6.5))
        self.price4_label = LabelNode(text = str(self.price4),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/6.5),
                                     color = 'gold')
        self.back2_square5 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/2.4))
        self.price5_label = LabelNode(text = str(self.price5),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/2.4),
                                     color = 'gold')
        self.back2_square6 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/1.465))
        self.price6_label = LabelNode(text = str(self.price6),
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y - self.screen_center_y/1.465),
                                     color = 'gold')
        self.back3_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6))
        self.buy1_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6),
                                     color = 'grey')
        self.back3_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7))
        self.buy2_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7),
                                     color = 'grey')
        self.back3_square3 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/9.25))
        self.buy3_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/9.25),
                                     color = 'grey')
        self.back3_square4 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/6.5))
        self.buy4_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/6.5),
                                     color = 'grey')
        self.back3_square5 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.4))
        self.buy5_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.4),
                                     color = 'grey')
        self.back3_square6 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.465))
        self.buy6_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.465),
                                     color = 'grey')
        self.coins_display = (LabelNode(text = 'Coins - ' + str(globals.coins),
                                     font = ('CopperPlate-Light', 30),
                                     parent = self,
                                     position = (self.screen_center_x, self.size_of_screen_y - 50),
                                     color = 'gold'))
    def update(self):
        # this method is called, hopefully, 60 times a second
        globals.coins = globals.coins + 10
        self.coins_display.text = 'Coins - ' + str(globals.coins)
        # after 2 seconds, move to main menu scene
        self.price1_label.text = str(self.price1)
        self.price2_label.text = str(self.price2)
        self.price3_label.text = str(self.price3)
        self.price4_label.text = str(self.price4)
        self.price5_label.text = str(self.price5)
        self.price6_label.text = str(self.price6)
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        if self.buy1_label.frame.contains_point(touch.location):
            self.buy1_label_down = True
            if globals.coins >= self.price1:
                globals.coins = globals.coins - self.price1
                self.price1 = self.price1*2
                globals.fullhealth = round(globals.fullhealth*1.5)
            else:
                pass
             
        if self.buy2_label.frame.contains_point(touch.location):
            self.buy2_label_down = True
            if globals.coins >= self.price2:
                globals.coins = globals.coins - self.price2
                self.price2 = self.price2*2
                globals.playerdmglowest = round(globals.playerdmglowest*1.5)
                globals.playerdmghighest = round(globals.playerdmghighest*1.5)
            else:
                pass
            
        if self.buy3_label.frame.contains_point(touch.location):
            self.buy3_label_down = True
            if globals.coins >= self.price3:
                globals.coins = globals.coins - self.price3
                self.price3 = self.price3*2
                globals.playercritdmg = round(globals.playercritdmg*1.5)
            else:
                pass
            
        if self.buy4_label.frame.contains_point(touch.location):
            self.buy4_label_down = True
            if globals.coins >= self.price4:
                globals.coins = globals.coins - self.price4
                self.price4 = self.price4*2
                globals.overtimeregen = round(globals.overtimeregen*1.5)
                
            else:
                pass
            
        if self.buy5_label.frame.contains_point(touch.location):
            self.buy5_label_down = True
            if globals.coins >= self.price5:
                globals.coins = globals.coins - self.price5
                self.price5 = self.price5*2
                globals.playerarmor = round(globals.playerarmor*1.5)
            else:
                pass
            
        if self.buy6_label.frame.contains_point(touch.location):
            self.buy6_label_down = True
            if globals.coins >= self.price6:
                globals.coins = globals.coins - self.price6
                self.price = self.price6*2
                globals.playeratkspeed = round(globals.playeratkspeed*1.5)
            else:
                pass
            
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
        
    
                                     
    
        
