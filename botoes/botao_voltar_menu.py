import arcade
from .botao import Botao

#botao de voltar pro menu
class Botao_voltar_menu(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_voltar_menu.png",center_x,center_y,170,27,1,acao_botao=0)
