import arcade
from .botao import Botao

#botao de play
class Botao_jogar(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_jogar.png",center_x=center_x,center_y=center_y,width=115,height=36,escala=1,acao_botao=1)
