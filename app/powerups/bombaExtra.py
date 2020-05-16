import arcade
from .powerup import Powerup


class BombaExtra(Powerup):
    def __init__(self,imagem ="app/img/powerups/bombaExtra3.png",escala=0.7,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def melhorar_player(self,player):
        if player.num_bombas < 5:
            player.num_bombas += 1
            return True
        return False