import arcade
from .botao import Botao

#botao de sair
class Botao_retornar_padrao(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_retornar_padrao.png",center_x,center_y,186,30,1,acao_botao=11)
