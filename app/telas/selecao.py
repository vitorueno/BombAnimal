import arcade
from app.botoes import Botao_voltar_menu, Botao_confirmar_selecao
from app.var import SCREEN_WIDTH, SCREEN_HEIGHT, CENTER_X, CENTER_Y

class Selecao_personagem():
    def __init__(self):
        self.borda_p1 = arcade.Sprite("app/img/selecao/selecao_p1.png",scale=1.15,center_x=250,center_y=400)
        self.borda_p2 = arcade.Sprite("app/img/selecao/selecao_p2.png",scale=1.15,center_x=550,center_y=200) 
        self.confirmacao_p1 = arcade.Sprite("app/img/selecao/confirmacao_p1.png",scale=1.15,center_x=250,center_y=400)
        self.confirmacao_p2 = arcade.Sprite("app/img/selecao/confirmacao_p2.png",scale=1.15,center_x=550,center_y=200) 
        self.personagem_p1 = None
        self.personagem_p2 = None
        
        self.titulo = arcade.Sprite("app/img/textos/texto_selecao.png",scale=1,center_x=CENTER_X,center_y=CENTER_Y+250)


        self.botao_confirmar = Botao_confirmar_selecao(680,34)
        self.botao_voltar = Botao_voltar_menu(130,34)

    def draw(self):
        #fundo
        fundo = arcade.Sprite("app/img/fundos/fundo_selecao.png",scale=1,center_x=CENTER_X,center_y=CENTER_Y)
        fundo.draw()
        #retangulo
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200,(22,120,111,232))
        #linha horizontal
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,SCREEN_WIDTH-200,2,(2,225,237))
        #arcade.draw_rectangle_filled()
        #linha vertical
        arcade.draw_rectangle_filled(CENTER_X,CENTER_Y,2,SCREEN_HEIGHT-200,(2,225,237))

        #desenho personagens
        arara = arcade.Sprite("app/img/animais/full_size/arara1.png",0.170,center_x=250,center_y=400)
        arara.draw()
        lebre = arcade.Sprite("app/img/animais/full_size/lebre1.png",0.170,center_x=550,center_y=400)
        lebre.draw()
        pinguim = arcade.Sprite("app/img/animais/full_size/pinguim1.png",0.170,center_x=250,center_y=200)
        pinguim.draw()
        panda = arcade.Sprite("app/img/animais/full_size/panda1.png",0.170,center_x=550,center_y=200)
        panda.draw()

        #borda de seleção p2
        if self.personagem_p2 is None:
            self.borda_p2.draw()
        else:
            self.confirmacao_p2.draw()

        #borda de seleção p1
        if self.personagem_p1 is None:
            self.borda_p1.draw()
        else:
            self.confirmacao_p1.draw()

        #título
        
        self.titulo.draw()

        #botoes
        self.botao_voltar.draw()
        if self.personagem_p1 is not None and self.personagem_p2 is not None:
            self.botao_confirmar.draw()
        
    def on_mouse_press(self,x,y,button,key_modifiers):
        self.botao_voltar.checar_clique(x,y,button,key_modifiers)
        if self.personagem_p1 is not None and self.personagem_p2 is not None:
            self.botao_confirmar.checar_clique(x,y,button,key_modifiers)

    def on_mouse_release(self,x,y,button,key_modifiers):
        voltar_menu = self.botao_voltar.desclicar(x,y,button,key_modifiers)
        confirmar_selecao = self.botao_confirmar.desclicar(x,y,button,key_modifiers)
        if voltar_menu is not None:
            return voltar_menu
        elif confirmar_selecao is not None:
            return confirmar_selecao,self.personagem_p1,self.personagem_p2

    def on_key_press_p1(self, key, key_modifiers):
        if key == arcade.key.W and self.personagem_p1 is None:
            if self.borda_p1.center_y == 200:
                self.borda_p1.center_y = 400
                self.confirmacao_p1.center_y = 400
        elif key == arcade.key.A and self.personagem_p1 is None:
            if self.borda_p1.center_x == 550:
                self.borda_p1.center_x = 250
                self.confirmacao_p1.center_x = 250
        elif key == arcade.key.S and self.personagem_p1 is None:
            if self.borda_p1.center_y == 400:
                self.borda_p1.center_y = 200
                self.confirmacao_p1.center_y = 200
        elif key == arcade.key.D and self.personagem_p1 is None:
            if self.borda_p1.center_x == 250:
                self.borda_p1.center_x = 550
                self.confirmacao_p1.center_x = 550

        elif key == arcade.key.SPACE and self.personagem_p1 is None:
            if self.borda_p1.center_x == 250 and self.borda_p1.center_y == 400:
                self.personagem_p1 = "arara"
            elif self.borda_p1.center_x == 250 and self.borda_p1.center_y == 200:
                self.personagem_p1 = "pinguim"
            elif self.borda_p1.center_x == 550 and self.borda_p1.center_y == 400:
                self.personagem_p1 = "lebre"
            elif self.borda_p1.center_x == 550 and self.borda_p1.center_y == 200:
                self.personagem_p1 = "panda"
        elif key == arcade.key.SPACE and self.personagem_p1 is not None:
            self.personagem_p1 = None

        if key == arcade.key.UP and self.personagem_p2 is None:
            if self.borda_p2.center_y == 200:
                self.borda_p2.center_y = 400
                self.confirmacao_p2.center_y = 400
        elif key == arcade.key.LEFT and self.personagem_p2 is None:
            if self.borda_p2.center_x == 550:
                self.borda_p2.center_x = 250
                self.confirmacao_p2.center_x = 250
        elif key == arcade.key.DOWN and self.personagem_p2 is None:
            if self.borda_p2.center_y == 400:
                self.borda_p2.center_y = 200 
                self.confirmacao_p2.center_y = 200
        elif key == arcade.key.RIGHT and self.personagem_p2 is None:
            if self.borda_p2.center_x == 250:
                self.borda_p2.center_x = 550
                self.confirmacao_p2.center_x = 550
        elif key == arcade.key.ENTER and self.personagem_p2 is None:
            if self.borda_p2.center_x == 250 and self.borda_p2.center_y == 400:
                self.personagem_p2 = "arara"
            elif self.borda_p2.center_x == 250 and self.borda_p2.center_y == 200:
                self.personagem_p2 = "pinguim"
            elif self.borda_p2.center_x == 550 and self.borda_p2.center_y == 400:
                self.personagem_p2 = "lebre"
            elif self.borda_p2.center_x == 550 and self.borda_p2.center_y == 200:
                self.personagem_p2 = "panda"
        elif key == arcade.key.ENTER and self.personagem_p2 is not None:
            self.personagem_p2 = None

    def on_key_release(self, key, key_modifiers):
        pass