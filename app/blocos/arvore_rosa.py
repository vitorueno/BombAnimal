import arcade
from .destrutivel import Destrutivel

class Arvore_rosa(Destrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/arvores/arvore3_rosa.png",0.7,center_x,center_y)
        self.drop_hate = 30