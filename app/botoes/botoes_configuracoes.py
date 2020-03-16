import arcade
from .botao import Botao

#p1
class Botao_cima_p1(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_cima.png",center_x,center_y,64,38,1,acao_botao="cima_p1")

class Botao_direita_p1(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_direita.png",center_x,center_y,76,38,1,acao_botao="direita_p1")

class Botao_baixo_p1(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_baixo.png",center_x,center_y,68,38,1,acao_botao="baixo_p1")

class Botao_esquerda_p1(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_esquerda.png",center_x,center_y,105,42,1,acao_botao="esquerda_p1")

class Botao_bomba_p1(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_bomba.png",center_x,center_y,83,38,1,acao_botao="bomba_p1")

#p2
class Botao_cima_p2(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_cima.png",center_x,center_y,64,38,1,acao_botao="cima_p2")

class Botao_direita_p2(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_direita.png",center_x,center_y,76,38,1,acao_botao="direita_p2")

class Botao_baixo_p2(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_baixo.png",center_x,center_y,68,38,1,acao_botao="baixo_p2")

class Botao_esquerda_p2(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_esquerda.png",center_x,center_y,105,42,1,acao_botao="esquerda_p2")

class Botao_bomba_p2(Botao):
    def __init__(self,center_x,center_y):
        super().__init__("app/img/botoes/botao_bomba.png",center_x,center_y,83,38,1,acao_botao="bomba_p2")