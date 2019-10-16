import arcade
from botoes.botao_voltar_menu import Botao_voltar_menu
from botoes.botao_confirmar import Botao_confirmar
from botoes.botao_retornar_padrao import Botao_retornar_padrao
from botoes.botoes_configuracoes import *


CONFIRMAR_CONFIGURACAO = 10
VOLTAR_PADRAO = 11

class Configuracoes():
    def __init__(self,screen_width,screen_height,config_atuais):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width/2
        self.center_y = screen_height/2
        self.titulo = arcade.Sprite("img/textos/texto_configuracoes.png",scale=1,center_x=self.center_x,center_y=self.center_y + 250)
        self.fundo = arcade.Sprite('img/fundo_menu.png',1,center_x=self.center_x,center_y=self.center_y)

        self.config_atuais = config_atuais

        self.alterar = False
        self.alterando = None

        botao_menu = Botao_voltar_menu(89,20)
        botao_confirmar = Botao_confirmar(self.center_x + 250, self.center_y-10 -210) 
        botao_padrao = Botao_retornar_padrao(self.center_x - 225,self.center_y-10 - 210)

        botao_cima_p1 = Botao_cima_p1(170,430) 
        botao_direita_p1 = Botao_direita_p1(170,360)
        botao_baixo_p1 = Botao_baixo_p1(170,290)
        botao_esquerda_p1 = Botao_esquerda_p1(170,220)
        botao_bomba_p1 = Botao_bomba_p1(170,150)

        botao_cima_p2 = Botao_cima_p2(625,430) 
        botao_direita_p2 = Botao_direita_p2(625,360)
        botao_baixo_p2 = Botao_baixo_p2(625,290)
        botao_esquerda_p2 = Botao_esquerda_p2(625,220)
        botao_bomba_p2 = Botao_bomba_p2(625,150)

        self.lista_botoes = [botao_menu,botao_confirmar,botao_padrao,botao_cima_p1,botao_direita_p1,
                            botao_baixo_p1,botao_esquerda_p1,botao_bomba_p1,botao_cima_p2,botao_direita_p2,
                            botao_baixo_p2,botao_esquerda_p2,botao_bomba_p2]

    def draw(self):
        self.fundo.draw()
        arcade.draw_rectangle_filled(self.center_x,self.center_y-10,self.screen_width - 150, self.screen_height - 140,(22,120,111,232))
        arcade.draw_rectangle_filled(self.center_x,self.center_y-10,3, self.screen_height - 220,arcade.color.ARSENIC)
        self.titulo.draw()

        for botao in self.lista_botoes:
            botao.draw()

        arcade.draw_text("AÇÃO",170,490,(0,240,255,255),18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        
        arcade.draw_text("TECLA ATUAL",300,490,(0,240,255,255),18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        

        arcade.draw_text(str(self.config_atuais["cima_p1"]),300,430,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["direita_p1"]),300,360,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["baixo_p1"]),300,290,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["esquerda_p1"]),300,220,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["bomba_p1"]),300,150,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")

        arcade.draw_text("AÇÃO",625,490,(0,240,255,255),18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        
        arcade.draw_text("TECLA ATUAL",495,490,(0,240,255,255),18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")

        arcade.draw_text(str(self.config_atuais["cima_p2"]),495,430,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["direita_p2"]),495,360,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["baixo_p2"]),495,290,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["esquerda_p2"]),495,220,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.config_atuais["bomba_p2"]),495,150,arcade.color.WHITE,18,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")

        if self.alterar:
            arcade.draw_text("MODO ALTERAR ATIVADO",self.center_x + 25,74,arcade.color.RED,16,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")

    def on_mouse_press(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            botao.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            proxima_tela = botao.desclicar(x,y,button,key_modifiers)
            if proxima_tela is not None:
                if type(proxima_tela) == int:
                    return proxima_tela
                else:
                    self.alterar = True
                    self.alterando = proxima_tela

    def on_key_release(self, key, key_modifiers):
        if self.alterar and key != arcade.key.ESCAPE:
            for chave in self.config_atuais:
                if self.config_atuais[chave] == key:
                    break
            else:
                self.config_atuais[self.alterando] = key
                self.alterando = None
                self.alterar = False