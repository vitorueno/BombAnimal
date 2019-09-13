import arcade
from .bloco import Bloco

class Grama(Bloco):
    def __init__(self,center_x,center_y):
        super().__init__("img/grama3.png",1,center_x,center_y)
