import arcade
from .botao import Botao

#botao de sair
class Botao_voltar_pag_ajuda(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("img/botoes/botao_voltar_pagina_ajuda.png",center_x,center_y,170,27,1,acao_botao=9)
