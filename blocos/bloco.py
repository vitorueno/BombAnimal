import arcade

class Bloco(arcade.Sprite):
    def __init__(self,arquivo,escala,center_x=0,center_y=0):
        super().__init__(arquivo,escala,center_x=center_x,center_y=center_y)

    def manter_na_tela(self,larg_tela,alt_tela):
        if self.left < 0:
            self.left = 0
        if self.right > larg_tela:
            self.right = larg_tela-1
        if self.top > alt_tela:
            self.top = alt_tela-1
        if self.bottom < 0:
            self.bottom = 0