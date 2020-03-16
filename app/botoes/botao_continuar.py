import arcade
from .botao import Botao

#botao de continuar
class Botao_continuar(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_continuar.png",center_x,center_y,117,27,1,acao_botao=3)
