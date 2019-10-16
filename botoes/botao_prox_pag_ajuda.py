import arcade
from .botao import Botao

#botao de sair
class Botao_proxima_pag_ajuda(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_proxima_pag_ajuda.png",center_x,center_y,261,44,1,acao_botao=8)
