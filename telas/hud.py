import arcade

class Hud():
    def __init__(self,hud_width,hud_height,center_x,center_y,duracao_partida,p1,p2):
        self.hud_width = hud_width
        self.hud_height = hud_height
        self.center_x = center_x
        self.center_y = center_y
        self.timer = duracao_partida

        self.p1 = p1
        self.p2 = p2

        self.tipo_p1 = self.p1.tipo
        self.tipo_p2 = self.p2.tipo


        self.fogo_p1 = self.p1.fogo 
        self.vento_p1 = self.p1.vento
        self.bombas_p1 = self.p1.num_bombas
        self.macaco_p1 = self.p1.macaco
        self.capacete_p1 = self.p1.capacete

        self.fogo_p2 = self.p2.fogo
        self.vento_p2 = self.p2.vento
        self.bombas_p2 = self.p2.num_bombas
        self.macaco_p2 = self.p2.macaco
        self.capacete_p2 = self.p2.capacete
        

    def atualizar_powerups(self,p1,p2):
        self.fogo_p1 = p1.fogo 
        self.vento_p1 = p1.vento
        self.bombas_p1 = p1.num_bombas
        self.macaco_p1 = p1.macaco
        self.capacete_p1 = p1.capacete

        self.fogo_p2 = p2.fogo
        self.vento_p2 = p2.vento
        self.bombas_p2 = p2.num_bombas
        self.macaco_p2 = p2.macaco
        self.capacete_p2 = p2.capacete

    def atualizar_tempo(self,delta_time):
        self.timer -= float(delta_time)

    
    def draw(self):
        #retangulo
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.hud_width,
                                     self.hud_height,(22,120,111,232))

        #risco
        arcade.draw_rectangle_filled(self.center_x,self.center_y-25,self.hud_width,
                                     2,(0,0,0,170))

        #personagens

        #descobrir a miniatura do player 1
        if self.tipo_p1 == "arara":
            miniatura_p1 = arcade.Sprite("img/animais/full_size/arara1.png",scale=0.04,center_x=self.center_x-370, center_y= self.center_y)
        elif self.tipo_p1 == "lebre":
            miniatura_p1 = arcade.Sprite("img/animais/full_size/lebre1.png",scale=0.04,center_x=self.center_x-370, center_y= self.center_y)
        elif self.tipo_p1 == "pinguim":
            miniatura_p1 = arcade.Sprite("img/animais/full_size/pinguim1.png",scale=0.04,center_x=self.center_x-370, center_y= self.center_y)
        elif self.tipo_p1 == "panda":
            miniatura_p1 = arcade.Sprite("img/animais/full_size/panda1.png",scale=0.04,center_x=self.center_x-370, center_y= self.center_y)
        
        #descobrir a miniatura player 2
        if self.tipo_p2 == "arara":
            miniatura_p2 = arcade.Sprite("img/animais/full_size/arara1.png",scale=0.04,center_x=self.center_x+370, center_y= self.center_y)
        elif self.tipo_p2 == "lebre":
            miniatura_p2 = arcade.Sprite("img/animais/full_size/lebre1.png",scale=0.04,center_x=self.center_x+370, center_y= self.center_y)
        elif self.tipo_p2 == "pinguim":
            miniatura_p2 = arcade.Sprite("img/animais/full_size/pinguim1.png",scale=0.04,center_x=self.center_x+370, center_y= self.center_y)
        elif self.tipo_p2 == "panda":
            miniatura_p2 = arcade.Sprite("img/animais/full_size/panda1.png",scale=0.04,center_x=self.center_x+370, center_y= self.center_y)

        #desenhar miniaturas
        miniatura_p1.draw()
        miniatura_p2.draw()

        #texto players
        jogador1 = f"Jogador 1"
        jogador2 = f"Jogador 2"
        arcade.draw_text(jogador1,self.center_x-300,self.center_y+7,arcade.color.WHITE,13,width=self.hud_width, align="center", anchor_x="center", anchor_y="bottom")
        arcade.draw_text(jogador2,self.center_x+300,self.center_y+7,arcade.color.WHITE,13,width=self.hud_width, align="center", anchor_x="center", anchor_y="bottom")
        
        #powerups 

        #criar miniaturas dos powerups do jogador 1
        mini_fogo_p1 = arcade.Sprite("img/powerups/fogo3.png",scale=0.5,center_x=self.center_x-325,center_y=self.center_y-3)
        mini_vento_p1 = arcade.Sprite("img/powerups/vento3.png",scale=0.5,center_x=self.center_x-307,center_y=self.center_y-3)
        mini_bombas_p1 = arcade.Sprite("img/powerups/bombaExtra3.png",scale=0.5,center_x=self.center_x-287,center_y=self.center_y-3)
        mini_macaco_p1 = arcade.Sprite("img/powerups/macaco3.png",scale=0.5,center_x=self.center_x-267,center_y=self.center_y-3)
        mini_capacete_p1 = arcade.Sprite("img/powerups/capacete3.png",scale=0.5,center_x=self.center_x-247,center_y=self.center_y-3)

        #criar miniaturas dos powerups do jogador 2
        mini_fogo_p2 = arcade.Sprite("img/powerups/fogo3.png",scale=0.5,center_x=self.center_x+325,center_y=self.center_y-3)
        mini_vento_p2 = arcade.Sprite("img/powerups/vento3.png",scale=0.5,center_x=self.center_x+307,center_y=self.center_y-3)
        mini_bombas_p2 = arcade.Sprite("img/powerups/bombaExtra3.png",scale=0.5,center_x=self.center_x+287,center_y=self.center_y-3)
        mini_macaco_p2 = arcade.Sprite("img/powerups/macaco3.png",scale=0.5,center_x=self.center_x+267,center_y=self.center_y-3)
        mini_capacete_p2 = arcade.Sprite("img/powerups/capacete3.png",scale=0.5,center_x=self.center_x+247,center_y=self.center_y-3)

        #mostrar miniaturas do jogador 1
        mini_fogo_p1.draw()
        mini_vento_p1.draw()
        mini_bombas_p1.draw()
        #só mostra a mão de macaco se o jogador coletou ela
        if self.macaco_p1:
            mini_macaco_p1.draw()
        #só mostra o capacete se o jogador coletou ele
        if self.capacete_p1:
            mini_capacete_p1.draw()

        #mostrar miniaturas do jogador 2
        mini_fogo_p2.draw()
        mini_vento_p2.draw()
        mini_bombas_p2.draw()
        #só mostra a mão de macaco se o jogador coletou ela
        if self.macaco_p2:
            mini_macaco_p2.draw()
        #só mostra o capacete se o jogador coletou ele
        if self.capacete_p2:
            mini_capacete_p2.draw()

        #contador powerups do jogador 1
        arcade.draw_text(str(self.fogo_p1),self.center_x-325, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.vento_p1),self.center_x-307, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.bombas_p1),self.center_x-287, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        if self.p1.capacete:
            arcade.draw_text("∞",self.center_x-247, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        if self.p1.macaco:
            arcade.draw_text("∞",self.center_x-267, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")

        #contador powerups do jogador 2
        arcade.draw_text(str(self.fogo_p2),self.center_x+325, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.vento_p2),self.center_x+307, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.bombas_p2),self.center_x+287, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        if self.p2.capacete:
            arcade.draw_text("∞",self.center_x+247, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        if self.p2.macaco:
            arcade.draw_text("∞",self.center_x+267, self.center_y-17,arcade.color.WHITE,12,
                        width=self.hud_width, align="center", anchor_x="center", anchor_y="center")

        #timer                            
        minutos = int(self.timer) // 60
        segundos = int(self.timer) % 60 
        tempo_texto = f"Tempo: {minutos:02d}:{segundos:02d}"
        morte_subita_texto = f"MORTE SÚBITA"
        if self.timer > 0:
            arcade.draw_text(tempo_texto,self.center_x,self.center_y,arcade.color.WHITE,14,
                            width=self.hud_width, align="center", anchor_x="center", anchor_y="center")
        elif self.timer <= 0:
            arcade.draw_text(morte_subita_texto,self.center_x,self.center_y,arcade.color.RED,14,
                            width=self.hud_width,align="center", anchor_x="center", anchor_y="center")


