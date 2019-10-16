import arcade
from .botao import Botao

#botao de opções
class Botao_opcoes_pause(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_opcoes2.png",center_x,center_y,129,48,1,acao_botao=5)
