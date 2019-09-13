import arcade
from .destrutivel import Destrutivel

class Arvore_rosa(Destrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("img/arvores/arvore3_rosa.png",0.9,center_x,center_y)
