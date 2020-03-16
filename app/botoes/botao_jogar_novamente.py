import arcade
from .botao import Botao

#botão jogar novamente
class Botao_jogar_novamente(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_jogar_novamente.png",center_x=center_x,center_y=center_y,width=188,height=25,escala=1,acao_botao=2)
