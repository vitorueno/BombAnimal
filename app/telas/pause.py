import arcade
from app.botoes import Botao_continuar, Botao_voltar_menu, Botao_sair_pause, Botao_opcoes_pause
from app.var import SCREEN_HEIGHT, SCREEN_WIDTH, CENTER_Y, CENTER_X

class Tela_pause():
    def __init__(self):
        self.botao_continuar = Botao_continuar(CENTER_X,CENTER_Y + 60)
        #self.botao_configuracao = Botao_opcoes_pause(CENTER_X,CENTER_Y - 10)
        self.botao_voltar_menu = Botao_voltar_menu(CENTER_X,CENTER_Y-10)
        self.botao_sair = Botao_sair_pause(CENTER_X,CENTER_Y-80)
        
        self.lista_botoes = [self.botao_continuar,self.botao_voltar_menu,self.botao_sair]

    def draw(self):
        #retangulo
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH - 300,
                                     SCREEN_HEIGHT - 200,(22,120,111,232))

        #texto jogo pausado 
        texto_pause = "Jogo Pausado"
        arcade.draw_text(texto_pause,CENTER_X,CENTER_Y+150,arcade.color.WHITE,30,
                        width=SCREEN_WIDTH-300, align="center", anchor_x="center", anchor_y="center")
        
        #botoes
        for botao in self.lista_botoes:
            botao.draw()
    
    def on_mouse_press(self,x,y,button,modifiers):
        for botao in self.lista_botoes:
            botao.checar_clique(x,y,button,modifiers)
    
    def on_mouse_release(self,x,y,button,modifiers):
        for botao in self.lista_botoes:
            proxima_tela = botao.desclicar(x,y,button,modifiers)
            if proxima_tela is not None:
                return proxima_tela

