import arcade

#botão base
class Botao:
    def __init__(self, imagem, center_x, center_y, width, height, escala=1,
                acao_botao = 0):
        self.imagem = imagem
        self.center_x = center_x
        self.center_y = center_y
        self.height = height
        self.width = width
        self.acao_botao = acao_botao
        self.pressed = False
        self.sprite_botao = arcade.Sprite(imagem,escala,center_x=center_x,
                                        center_y=center_y)

    def draw(self):
        self.sprite_botao.draw()

    # se for solto o estado do botão é não pressionado
    def on_release(self):
        self.pressed = False
        return self.acao_botao

    def checar_clique(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.mouse_on_button(x,y,button,modifiers):
                self.pressed = True
                # self.on_press()
                
    def desclicar(self,x,y,button,modifiers):
        if self.pressed and self.mouse_on_button(x,y,button,modifiers):
            proxima_acao = self.on_release()
            return proxima_acao
        return None

    def mouse_on_button(self,x,y,button, modifiers):
        if x > self.center_x + self.width / 2:
            return None
        elif x < self.center_x - self.width / 2:
            return None
        elif y > self.center_y + self.height / 2:
            return None
        elif y < self.center_y - self.height / 2:
            return None
        else:
            return True





