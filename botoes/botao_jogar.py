import arcade
from .botao import Botao

#botao de play(jogar)
class Botao_jogar(Botao):
    def __init__(self,center_x,center_y):
        super().__init__(center_x,center_y,120,30,"Jogar",29,"Arial",face_color=(0,0,0,0),cor_texto=(0,240,255),acao_botao=1)

        