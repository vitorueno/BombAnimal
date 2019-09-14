import arcade
from botoes.botao_jogar import Botao_jogar
from botoes.botao_opcoes import Botao_opcoes
from botoes.botao_sair import Botao_sair


class Menu():
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width/2
        self.center_y = screen_height/2

        #criar botoes e jogar numa lista de botoes
        self.lista_botoes = []
        botao_jogar = Botao_jogar(self.center_x, self.center_y + 60)
        botao_opcoes = Botao_opcoes(self.center_x, self.center_y - 10)
        botao_sair = Botao_sair(self.center_x,self.center_y- 80)
        self.lista_botoes.append(botao_jogar)
        self.lista_botoes.append(botao_opcoes)
        self.lista_botoes.append(botao_sair)
    
    def draw_menu(self):
        #fundo
        fundo = arcade.Sprite("img/fundo_menu.png",center_x=self.center_x,center_y=self.center_y,scale=1)
        fundo.draw()

        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.screen_width - 300, self.screen_height - 200,(22,120,111,232))

        #logo
        logo = arcade.Sprite("img/logo.png",center_x=self.center_x,center_y=self.center_y + 150,scale=1)
        logo.draw()

        #botoes
        for botao in self.lista_botoes:
            botao.draw()

    def on_mouse_press_menu(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            botao.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release_menu(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            proxima_tela = botao.desclicar(x,y,button,key_modifiers)
            if proxima_tela is not None:
                return proxima_tela