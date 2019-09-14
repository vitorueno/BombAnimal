import arcade
from .botao import Botao

#botao de voltar pra seleção de personagem
class Botao_voltar_selecao(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_voltar_selecao.png",center_x,center_y,215,31,1,acao_botao=1)
