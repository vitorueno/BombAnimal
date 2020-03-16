import arcade
from .powerup import Powerup

#0.03
class CapaceteCoco(Powerup):
    def __init__(self,imagem ="app/img/powerups/capacete3.png",escala=0.7,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def melhorar_player(self,player):
        if not player.capacete:
            player.capacete = True