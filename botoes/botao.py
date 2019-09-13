import arcade

#botão base
class Botao:
    def __init__(self,center_x, center_y,width, height, text, font_size=18,font_face="Arial",
                face_color=arcade.color.LIGHT_GRAY,highlight_color=arcade.color.WHITE,
                shadow_color=arcade.color.GRAY,button_height=2,frame=False,cor_texto=arcade.color.WHITE,acao_botao = 0):

        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height
        self.frame = frame
        self.cor_texto = cor_texto
        self.acao_botao = acao_botao

    def draw(self):
        """ desenhar_botão """

        #retangulo do botão
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color

        else:
            color = self.highlight_color

        if self.frame:
            #linha horizontal de baixo
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                            self.center_x + self.width / 2, self.center_y - self.height / 2,
                            color, self.button_height)

            #linha vertical da direita
            arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                            self.center_x + self.width / 2, self.center_y + self.height / 2,
                            color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        if self.frame:
            #linha horizontal do topo
            arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                            self.center_x + self.width / 2, self.center_y + self.height / 2,
                            color, self.button_height)

            #linha vertical da esquerda
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                            self.center_x - self.width / 2, self.center_y + self.height / 2,
                            color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         self.cor_texto, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    #se for pressionado o estado do botão é pressionado
    def on_press(self):
        self.pressed = True

    #se for solto o estado do botão é não pressionado
    def on_release(self):
        self.pressed = False
        return self.acao_botao

    def checar_clique(self,x,y,button,modifiers):
        '''if x >= self.center_x and x <= self.width/2 and y >= self.center_y and y <= self.height/2 and button == arcade.MOUSE_BUTTON_LEFT:
            self.on_press()
        elif x <= self.center_x and x <= self.width/2 and y>= self.center_y and y <= self.height/2 and button == arcade.MOUSE_BUTTON_LEFT:
            self.on_press()
        elif x >= self.center_x and x <= self.width/2 and y <= self.center_y and y <= self.height/2 and button == arcade.MOUSE_BUTTON_LEFT:
            self.on_press()
        elif x  <= self.center_x and x <= self.width/2 and y <= self.center_y and y <= self.height/2 and button == arcade.MOUSE_BUTTON_LEFT:
            self.on_press()'''
        if button == arcade.MOUSE_BUTTON_LEFT:
            if x > self.center_x + self.width / 2:
                return None
            elif x < self.center_x - self.width / 2:
                return None
            elif y > self.center_y + self.height / 2:
                return None
            elif y < self.center_y - self.height / 2:
                return None
            else:
                self.on_press()

    def desclicar(self,x,y,button,modifiers):
        if self.pressed:
            proxima_acao = self.on_release()
            return proxima_acao
        return None







