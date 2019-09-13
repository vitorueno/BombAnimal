import arcade
from .player import Player

#0.06

class Arara(Player):
    def __init__(self,x=0,y=0,c=arcade.key.W,b=arcade.key.S,d=arcade.key.D,e=arcade.key.A,bomb=arcade.key.SPACE,
                arquivo="img/animais/arara3.png",escala=1,velocidade=5,bombas=1,forca=1,vidas=1):
        super().__init__(arquivo,escala,velocidade,x,y,bombas,forca,vidas,c,b,d,e,bomb)
        self.tipo = "arara"