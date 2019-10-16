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
        self.drop_hate = 0

    def destruir_bloco(self):
        power_up = self.sortear_PowerUp()
        arcade.sound.play_sound(self.som)
        self.kill()
        if power_up is not None:
            return power_up
        return None

    #sortear se haverá power up e qual será
    def sortear_PowerUp(self):
        #os valores abaixo são em porcentagem
        chance_gerar_item = random.randint(1,100)
        sorte = 100 - self.drop_hate
        if chance_gerar_item >= sorte:
            qual_item = random.randint(1,100)

            #35%
            if qual_item > 0 and qual_item <= 35:
                powerup = Vento(center_x=self.center_x,center_y=self.center_y)
                return powerup

            #30%
            elif qual_item > 35 and qual_item <= 65:
                powerup = BombaExtra(center_x=self.center_x,center_y=self.center_y)
                return powerup

            #20%
            elif qual_item >= 65 and qual_item <= 85:
                powerup = Fogo(center_x=self.center_x,center_y=self.center_y)
                return powerup

            #10%
            elif qual_item > 85 and qual_item <= 95:
                powerup = MaoMacaco(center_x=self.center_x,center_y=self.center_y)
                return powerup

            #5
            elif qual_item > 95 and qual_item <= 100:
                powerup = CapaceteCoco(center_x=self.center_x,center_y=self.center_y)
                return powerup