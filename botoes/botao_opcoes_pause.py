import arcade
from .botao import Botao

#botao de opções
class Botao_opcoes_pause(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_opcoes_pause.png",center_x,center_y,143,30,1,acao_botao=5)
