import arcade
from .botao import Botao

#botao de confirmar seleção
class Botao_confirmar_selecao(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_confirmar_selecao.png",center_x,center_y,204,34,1,acao_botao=2)
