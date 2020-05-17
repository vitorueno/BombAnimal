import arcade
from app.botoes import Botao_jogar, Botao_opcoes, Botao_sair, Botao_ajuda
from app.var import SCREEN_WIDTH, SCREEN_HEIGHT, CENTER_X, CENTER_Y

class Menu():
    def __init__(self):
        #criar botoes e jogar numa lista de botoes
        botao_jogar = Botao_jogar(CENTER_X, CENTER_Y + 60)
        botao_opcoes = Botao_opcoes(CENTER_X, CENTER_Y - 10)
        botao_ajuda = Botao_ajuda(CENTER_X,CENTER_Y - 80)
        botao_sair = Botao_sair(CENTER_X,CENTER_Y- 150)
        self.lista_botoes = [botao_jogar,botao_opcoes,botao_ajuda,botao_sair]
        
    def draw(self):
        #fundo
        fundo = arcade.Sprite("app/img/fundos/fundo_menu.png",center_x=CENTER_X,center_y=CENTER_Y,scale=1)
        fundo.draw()

        #retangulo
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH - 300, SCREEN_HEIGHT - 200,(22,120,111,232))

        #logo
        logo = arcade.Sprite("app/img/textos/logo.png",center_x=CENTER_X,center_y=CENTER_Y + 150,scale=1)
        logo.draw()

        #botoes
        for botao in self.lista_botoes:
            botao.draw()

    def on_mouse_press(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            botao.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            proxima_tela = botao.desclicar(x,y,button,key_modifiers)
            if proxima_tela is not None:
                return proxima_tela