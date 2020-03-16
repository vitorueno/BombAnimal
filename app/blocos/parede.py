import arcade
from .indestrutivel import Indestrutivel

class Parede(Indestrutivel):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/indestrutiveis/parede3.png",0.7,center_x,center_y)

