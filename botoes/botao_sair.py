import arcade
from .botao import Botao

#botao de sair
class Botao_sair(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_sair.png",center_x,center_y,74,36,1,acao_botao=6)
