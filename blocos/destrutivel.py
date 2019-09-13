import arcade
import random
from .bloco import Bloco
from powerups.bombaExtra import BombaExtra
from powerups.capaceteCoco import CapaceteCoco
from powerups.maoMacaco import MaoMacaco
from powerups.fogo import Fogo
from powerups.vento import Vento

class Destrutivel(Bloco):
    def __init__(self,arquivo,escala,center_x=0,center_y=0):
        super().__init__(arquivo,escala,center_x=center_x,center_y=center_y)
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
        chance = random.randint(1,125)

        if chance > 100 and chance < 126:
            powerup = MaoMacaco(center_x=self.center_x,center_y=self.center_y)
            return powerup

        elif chance > 75 and chance < 100:
            powerup = BombaExtra(center_x=self.center_x,center_y=self.center_y)
            return powerup

        elif chance > 50 and chance < 75:
            powerup = CapaceteCoco(center_x=self.center_x,center_y=self.center_y)
            return powerup
        
        elif chance > 25 and chance < 50:
            powerup = Fogo(center_x=self.center_x,center_y=self.center_y)
            return powerup
        
        elif chance > 0 and chance < 25:
            powerup = Vento(center_x=self.center_x,center_y=self.center_y)
            return powerup
        

