import arcade
from .botao import Botao

class Botao_voltar_menu_pos(Botao):
    def __init__(self, center_x,center_y):
        super().__init__(center_x,center_y,150,50,"Voltar ao menu",14,"Arial",face_color=(0,0,0,0),cor_texto=(0,240,255),acao_botao=0)