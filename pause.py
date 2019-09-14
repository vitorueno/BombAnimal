import arcade
from botoes.botao_continuar import Botao_continuar
from botoes.botao_voltar_menu import Botao_voltar_menu
from botoes.botao_sair import Botao_sair
from botoes.botao_opcoes import Botao_opcoes
from botoes.botao_opcoes_pause import Botao_opcoes_pause

class Tela_pause():
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width/2
        self.center_y = screen_height/2
    
        self.botao_continuar = Botao_continuar(self.center_x,self.center_y + 60)
        self.botao_configuracao = Botao_opcoes_pause(self.center_x,self.center_y - 10)
        self.botao_voltar_menu = Botao_voltar_menu(self.center_x,self.center_y-80)
        self.botao_sair = Botao_sair(self.center_x,self.center_y-150)
        
        self.lista_botoes = [self.botao_continuar,self.botao_configuracao,self.botao_voltar_menu,self.botao_sair]

    def draw(self):
        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.screen_width - 300,
                                     self.screen_height - 200,(22,120,111,232))

        #texto jogo pausado 
        texto_pause = "Jogo Pausado"
        arcade.draw_text(texto_pause,self.center_x,self.center_y+150,arcade.color.WHITE,30,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        
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

