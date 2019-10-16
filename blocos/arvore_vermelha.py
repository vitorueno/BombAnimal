import arcade
from .destrutivel import Destrutivel

class Arvore_vermelha(Destrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("img/arvores/arvore3_vermelha.png",0.7,center_x,center_y)
        self.drop_hate = 40