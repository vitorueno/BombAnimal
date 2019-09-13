import arcade
from .destrutivel import Destrutivel

class Arvore_dourada(Destrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("img/arvores/arvore3_dourada.png",0.9,center_x,center_y)
