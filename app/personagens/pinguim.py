import arcade
from .player import Player
from app.var import IMG_PINGUIM


class Pinguim(Player):
    def __init__(self, x=0, y=0, tipo_player=1, arquivo=IMG_PINGUIM, scale=1.09,
                vel=3, bombas=2, forca=1):
        super().__init__(arquivo=arquivo, scale=scale, velocidade=vel, x=x, y=y, 
                         bombas=bombas, forca=forca, tipo_player=tipo_player)
        self.tipo = "pinguim"
        # self.load_images("app/img/animais/pinguim/",1.09)
        self.load_images(self.tipo)
