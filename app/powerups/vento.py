import arcade
from .powerup import Powerup


class Vento(Powerup):
    def __init__(self,imagem ="app/img/powerups/vento3.png",escala=0.7,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def melhorar_player(self,player):
        if player.vento < 5:
            player.vento += 1
            player.velocidade += 1 
