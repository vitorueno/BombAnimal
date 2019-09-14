import arcade
from .player import Player

class Lebre(Player):
    def __init__(self,x=0,y=0,c=arcade.key.W,b=arcade.key.S,d=arcade.key.D,e=arcade.key.A,bomb=arcade.key.SPACE,
                arquivo="img/animais/lebre3.png",escala=1.09,velocidade=5.75,bombas=1,forca=1):     
        super().__init__(arquivo,escala,velocidade,x,y,bombas,forca,c,b,d,e,bomb)
        self.tipo = "lebre"