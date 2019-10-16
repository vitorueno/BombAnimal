import arcade
from botoes.botao_voltar_menu import Botao_voltar_menu
from botoes.botao_prox_pag_ajuda import Botao_proxima_pag_ajuda
from botoes.botao_voltar_pag_ajuda import Botao_voltar_pag_ajuda

class Ajuda():
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width/2
        self.center_y = screen_height/2
        self.pagina_atual = 1

        self.titulo = arcade.Sprite('img/textos/texto_ajuda.png',1,center_x=self.center_x,center_y=self.center_y + 250)
        self.fundo = arcade.Sprite('img/fundo_menu.png',1,center_x=self.center_x,center_y=self.center_y)

        
        botao_voltar_pagina = Botao_voltar_pag_ajuda(self.center_x - 230,self.center_y-10 - 210)
        botao_voltar_menu = Botao_voltar_menu(89,20)
        proxima_pag = Botao_proxima_pag_ajuda(self.center_x + 230, self.center_y-10 -210)
        
        self.lista_botoes = [botao_voltar_pagina,proxima_pag,botao_voltar_menu]
        
        self.titulo_sobre = 'O que é?'
        self.titulo_tutorial = 'Como faço pra jogar?'
        self.titulo_partida = 'Gameplay'
        self.titulo_personagens = 'Personagens'
        self.titulo_itens = 'Itens'
        self.titulo_contato = 'Contato'
        self.titulo_teclado = 'Controles Padrões'

        self.texto_sobre = arcade.Sprite('img/textos/texto_sobre_ajuda.png',1,center_x=self.center_x,center_y=self.center_y)
        self.texto_tutorial = arcade.Sprite('img/textos/texto_tutorial_ajuda.png',1,center_x=self.center_x,center_y=self.center_y)
        self.texto_partida = arcade.Sprite('img/textos/texto_partida_ajuda.png',1,center_x=self.center_x,center_y=self.center_y)
        self.texto_contato = arcade.Sprite('img/textos/texto_contato_ajuda.png',1,center_x=self.center_x,center_y=self.center_y)

        self.tabela_itens = arcade.Sprite('img/tabela_itens.png',0.75,center_x=self.center_x,center_y=self.center_y - 10)
        self.tabela_personagens = arcade.Sprite('img/tabela_personagens.png',0.9,center_x=self.center_x,center_y=self.center_y-10)
        self.teclado = arcade.Sprite('img/teclas.png',0.389,center_x=self.center_x,center_y=self.center_y - 10)

    def draw(self):
        self.fundo.draw()
        arcade.draw_rectangle_filled(self.center_x,self.center_y-10,self.screen_width - 150, self.screen_height - 140,(22,120,111,232))
        self.titulo.draw()  

        for botao in self.lista_botoes:
            botao.draw()

        #pagina 1
        if self.pagina_atual == 1:
            self.texto_sobre.draw()
            arcade.draw_text(self.titulo_sobre,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")
        
        #pagina 2 
        elif self.pagina_atual == 2:
            self.texto_tutorial.draw()
            arcade.draw_text(self.titulo_tutorial,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")
        
        #pagina 3
        elif self.pagina_atual == 3:
            self.tabela_personagens.draw()
            arcade.draw_text(self.titulo_personagens,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width - 150, anchor_x="center", anchor_y="center")
            
        #pagina 4
        elif self.pagina_atual == 4:
            self.texto_partida.draw()
            arcade.draw_text(self.titulo_partida,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")

        #pagina 5
        elif self.pagina_atual == 5:
            self.teclado.draw()
            arcade.draw_text(self.titulo_teclado,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")
        
        #pagina 6
        elif self.pagina_atual == 6:
            self.tabela_itens.draw()
            arcade.draw_text(self.titulo_itens,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")
        
        #pagina 7
        elif self.pagina_atual == 7:
            self.texto_contato.draw()
            arcade.draw_text(self.titulo_contato,self.center_x, self.center_y-10 + 200,arcade.color.WHITE,24, align="center",
            width=self.screen_width -150, anchor_x="center", anchor_y="center")

    def on_mouse_press(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            botao.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release(self,x,y,button,key_modifiers):
        for botao in self.lista_botoes:
            proxima_tela = botao.desclicar(x,y,button,key_modifiers)
            if proxima_tela is not None:
                if proxima_tela == 8:
                    if self.pagina_atual < 7:
                        self.pagina_atual += 1
                    return None
                elif proxima_tela == 9:
                    if self.pagina_atual > 1:
                        self.pagina_atual -= 1
                    return None
                else:
                    return proxima_tela