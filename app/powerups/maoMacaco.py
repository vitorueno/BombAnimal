import arcade
from .powerup import Powerup

class MaoMacaco(Powerup):
    def __init__(self,imagem ="app/img/powerups/macaco3.png",escala=0.7,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def melhorar_player(self,player):
        if not player.macaco:
            player.macaco = True