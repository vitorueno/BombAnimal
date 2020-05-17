import arcade
from .player import Player
from app.var import IMG_LEBRE


class Lebre(Player):
    def __init__(self, x=0, y=0, tipo_player=1, arquivo=IMG_LEBRE, scale=1.09,
                 vel=3.45, bombas=1, forca=1):     
        super().__init__(arquivo=arquivo, scale=scale, velocidade=vel, x=x, y=y,
                        bombas=bombas, forca=forca, tipo_player=tipo_player)
        self.tipo = "lebre"
        self.load_images(self.tipo)
