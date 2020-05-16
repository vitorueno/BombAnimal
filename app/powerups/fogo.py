import arcade
from .powerup import Powerup


class Fogo(Powerup):
    def __init__(self,imagem ="app/img/powerups/fogo3.png",escala=0.7,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def melhorar_player(self,player):
        if player.fogo < 4:
            player.fogo += 1
            player.forca += 1 
