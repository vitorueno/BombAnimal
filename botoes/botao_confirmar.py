import arcade
from .botao import Botao

class Botao_confirmar(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_confirmar.png",center_x,center_y,119,27,1,acao_botao=10)
