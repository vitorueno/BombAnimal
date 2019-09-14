import arcade
from .botao import Botao

#botao de opções
class Botao_opcoes(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_opcoes.png",center_x,center_y,129,48,1,acao_botao=5)
