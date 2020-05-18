import arcade
from app.botoes import Botao_voltar_menu, Botao_confirmar_selecao
from app.var import (SCREEN_WIDTH, SCREEN_HEIGHT, CENTER_X, CENTER_Y, 
                    ARARA_FULLSIZE, PANDA_FULLSIZE,LEBRE_FULLSIZE,
                    PINGUIM_FULLSIZE, config_atual)

class Selecao_personagem():
    def __init__(self):
        self.borda_p1 = arcade.Sprite("app/img/selecao/selecao_p1.png", 
                                    scale=1.15,center_x=250,center_y=400)
        self.borda_p2 = arcade.Sprite("app/img/selecao/selecao_p2.png",
                                    scale=1.15,center_x=550,center_y=200) 
        self.confirm_p1 = arcade.Sprite("app/img/selecao/confirmacao_p1.png",
                                        scale=1.15,center_x=250,center_y=400)
        self.confirm_p2 = arcade.Sprite("app/img/selecao/confirmacao_p2.png",
                                        scale=1.15,center_x=550,center_y=200) 
        self.char_p1 = None
        self.char_p2 = None
        self.titulo = arcade.Sprite("app/img/textos/texto_selecao.png",
                                    scale=1,center_x=CENTER_X,
                                    center_y=CENTER_Y+250)
        self.botao_confirmar = Botao_confirmar_selecao(680,34)
        self.botao_voltar = Botao_voltar_menu(130,34)
        self.set_player_keys()
    
    def set_player_keys(self):
        self.p1 = {'c':config_atual['cima_p1'], 
                'b':config_atual['baixo_p1'], 
                'd': config_atual['direita_p1'],
                'e': config_atual['esquerda_p1'],
                'bmb': config_atual['bomba_p1']}

        self.p2 = {'c':config_atual['cima_p2'], 
                'b':config_atual['baixo_p2'], 
                'd': config_atual['direita_p2'],
                'e': config_atual['esquerda_p2'],
                'bmb': config_atual['bomba_p2']}

    def draw(self):
        #fundo
        fundo = arcade.Sprite("app/img/fundos/fundo_selecao.png",scale=1,
                            center_x=CENTER_X,center_y=CENTER_Y)
        fundo.draw()
        #retangulo
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH - 200,
                                     SCREEN_HEIGHT - 200,(22,120,111,232))
        #linha horizontal
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH-200,2,
                                    (2,225,237))
        #linha vertical
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,2,SCREEN_HEIGHT-200,
                                    (2,225,237))

        #desenho personagens
        arara = arcade.Sprite(ARARA_FULLSIZE,0.170,center_x=250,center_y=400)
        arara.draw()
        lebre = arcade.Sprite(LEBRE_FULLSIZE,0.170,center_x=550,center_y=400)
        lebre.draw()
        pinguim = arcade.Sprite(PINGUIM_FULLSIZE,0.170,center_x=250,center_y=200)
        pinguim.draw()
        panda = arcade.Sprite(PANDA_FULLSIZE,0.170,center_x=550,center_y=200)
        panda.draw()

        #borda de seleção p2
        [self.borda_p2.draw() if self.char_p2 is None else self.confirm_p2.draw()]
        
        #borda de seleção p1
        [self.borda_p1.draw() if self.char_p1 is None else self.confirm_p1.draw()]
        
        #título
        self.titulo.draw()

        #botoes
        self.botao_voltar.draw()
        if self.char_p1 and self.char_p2:
            self.botao_confirmar.draw()
        
    def on_mouse_press(self,x,y,button,key_modifiers):
        self.botao_voltar.checar_clique(x,y,button,key_modifiers)
        if self.char_p1 and self.char_p2:
            self.botao_confirmar.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release(self,x,y,button,key_modifiers):
        voltar_menu = self.botao_voltar.desclicar(x,y,button,key_modifiers)
        confirmar_selecao = self.botao_confirmar.desclicar(x,y,button,key_modifiers)
        if voltar_menu is not None:
            return voltar_menu
        elif confirmar_selecao is not None:
            return confirmar_selecao,self.char_p1,self.char_p2

    def on_key_press(self, key, key_modifiers):
        self.set_player_keys()
        # movimentação player 1 
        if self.char_p1 is None:
            if key == self.p1['c'] and self.borda_p1.center_y == 200:
                self.borda_p1.center_y = 400
                self.confirm_p1.center_y = 400
            elif key == self.p1['e'] and self.borda_p1.center_x == 550:
                self.borda_p1.center_x = 250
                self.confirm_p1.center_x = 250
            elif key == self.p1['b'] and self.borda_p1.center_y == 400:
                self.borda_p1.center_y = 200
                self.confirm_p1.center_y = 200
            elif key == self.p1['d'] and self.borda_p1.center_x == 250:
                self.borda_p1.center_x = 550
                self.confirm_p1.center_x = 550
            # seleção player 1
            elif key == self.p1['bmb']:
                self.set_char_p1()
        elif key == self.p1['bmb'] and self.char_p1:
                self.char_p1 = None

        # movimentação player 2
        if self.char_p2 is None:
            if key == self.p2['c'] and self.borda_p2.center_y == 200:
                self.borda_p2.center_y = 400
                self.confirm_p2.center_y = 400
            elif key == self.p2['e'] and self.borda_p2.center_x == 550:
                self.borda_p2.center_x = 250
                self.confirm_p2.center_x = 250
            elif key == self.p2['b'] and self.borda_p2.center_y == 400:
                self.borda_p2.center_y = 200 
                self.confirm_p2.center_y = 200
            elif key == self.p2['d'] and self.borda_p2.center_x == 250:
                self.borda_p2.center_x = 550
                self.confirm_p2.center_x = 550
            # confirmação player 2 
            elif key == self.p2['bmb']:
                self.set_char_p2()
        elif key == self.p2['bmb']:
                self.char_p2 = None
        
    def set_char_p1(self):
        if self.borda_p1.center_x == 250 and self.borda_p1.center_y == 400:
            self.char_p1 = "arara"
        elif self.borda_p1.center_x == 250 and self.borda_p1.center_y == 200:
            self.char_p1 = "pinguim"
        elif self.borda_p1.center_x == 550 and self.borda_p1.center_y == 400:
            self.char_p1 = "lebre"
        elif self.borda_p1.center_x == 550 and self.borda_p1.center_y == 200:
            self.char_p1 = "panda"

    def set_char_p2(self):
        if self.borda_p2.center_x == 250 and self.borda_p2.center_y == 400:
            self.char_p2 = "arara"
        elif self.borda_p2.center_x == 250 and self.borda_p2.center_y == 200:
            self.char_p2 = "pinguim"
        elif self.borda_p2.center_x == 550 and self.borda_p2.center_y == 400:
            self.char_p2 = "lebre"
        elif self.borda_p2.center_x == 550 and self.borda_p2.center_y == 200:
            self.char_p2 = "panda"