import arcade
from .bloco import Bloco

class Grama(Bloco):
    def __init__(self,center_x,center_y):
        super().__init__("img/chao/grama_mapa.png",1,center_x,center_y)
