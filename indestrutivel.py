import arcade
from bloco import Bloco

class Indestrutivel(Bloco):
    def __init__(self,arquivo,escala,center_x=0,center_y=0,vida=1):
        super().__init__(arquivo,escala,center_x=center_x,center_y=center_y)
        
    