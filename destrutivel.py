import arcade
import random
from bloco import Bloco
from bombaExtra import BombaExtra

class Destrutivel(Bloco):
    def __init__(self,arquivo,escala,center_x=0,center_y=0,vida=1):
        super().__init__(arquivo,escala,center_x=center_x,center_y=center_y)
        #self.vida = vida
        self.som = arcade.sound.load_sound("sound/bloco_quebrou.wav")

    def destruir_bloco(self):
        power_up = self.sortear_PowerUp()
        arcade.sound.play_sound(self.som)
        self.kill()
        if power_up is not None:
            return power_up
        return None

    #sortear se haverá power up e qual será
    def sortear_PowerUp(self):
        chance = random.randint(1,100)
        if chance > 75 and chance < 101:
            powerup = BombaExtra(center_x=self.center_x,center_y=self.center_y)
            return powerup
