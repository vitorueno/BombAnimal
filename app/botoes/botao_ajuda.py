import arcade
from .botao import Botao

#botao de opções
class Botao_ajuda(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_ajuda.png",center_x,center_y,129,48,1,acao_botao=7)
