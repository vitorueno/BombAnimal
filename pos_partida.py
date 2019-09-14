import arcade
from botoes.botao_voltar_menu_pos import Botao_voltar_menu_pos
from botoes.botao_jogar_novamente import Botao_jogar_novamente
from botoes.botao_voltar_selecao import Botao_voltar_selecao


class Pos_partida():
    def __init__(self,screen_width,screen_height,p1,p2):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width/2
        self.center_y = screen_height/2
        self.p1 = p1
        self.p2 = p2

        #criar botoes e jogar numa lista de botoes
        
        self.botao_menu = Botao_voltar_menu_pos(250, self.center_y - 150)
        self.botao_selecao = Botao_voltar_selecao(self.center_x,self.center_y - 150)
        self.botao_novamente = Botao_jogar_novamente(550, self.center_y - 150)
        self.lista_botoes = [self.botao_menu,self.botao_selecao,self.botao_novamente]
    
    def draw_pos_partida(self):
        #fundo

        #opcao 1
        '''fundo = arcade.Sprite("img/fundo_pos_partida.png",center_x=self.center_x,center_y=self.center_y,scale=1)
        fundo.draw()'''
        #opcao 2
        '''fundo = arcade.Sprite("img/fundo_pos_partida2.png",center_x=self.center_x,center_y=self.center_y,scale=1)
        fundo.draw()'''
        #opcao 3
        fundo = arcade.Sprite("img/fundo_pos_partida3.png",center_x=self.center_x,center_y=self.center_y,scale=1)
        fundo.draw()

        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.screen_width - 300, self.screen_height - 200,(22,120,111,232))

        #imagem personagem vitorioso
        
        #se for o p1
        if self.p1.ganhou is not None and self.p1.ganhou:
            texto_ganhador = "Vitória do jogador 1!!!"
            arcade.draw_text(texto_ganhador,self.center_x,self.center_y+150,arcade.color.RED,30,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
            player_ganhador = arcade.Sprite(f"img/animais/{self.p1.tipo}1.png",scale=0.170,center_x=self.center_x, center_y= self.center_y)
            player_ganhador.draw()

        #se for o p2
        elif self.p2.ganhou is not None and self.p2.ganhou:
            texto_ganhador = "Vitória do jogador 2!!!"
            arcade.draw_text(texto_ganhador,self.center_x,self.center_y+150,arcade.color.GREEN,30,
                        width=self.screen_width-300, align="center", anchor_x="center", anchor_y="center")
            player_ganhador = arcade.Sprite(f"img/animais/{self.p2.tipo}1.png",scale=0.170,center_x=self.center_x, center_y= self.center_y)
            player_ganhador.draw()

        #se não for nenhum dos dois (?)
        else:
            player_empate1 = arcade.Sprite(f"img/animais/{self.p1.tipo}1.png",scale=0.170,center_x=self.center_x-100, center_y= self.center_y)
            player_empate2 = arcade.Sprite(f"img/animais/{self.p2.tipo}1.png",scale=0.170,center_x=self.center_x+100, center_y= self.center_y)
            player_empate1.draw()
            player_empate2.draw()


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