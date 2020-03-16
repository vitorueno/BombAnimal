import arcade
from .destrutivel import Destrutivel

class Arvore_verde(Destrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/arvores/arvore3_verde.png",0.7,center_x,center_y)
        self.drop_hate = 20