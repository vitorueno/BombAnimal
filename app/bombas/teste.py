import arcade

class Explosao(arcade.Sprite):

    def __init__(self,texture_list,img,escala,center_x,center_y,angulo):
        imagem_inicial = img 
        super().__init__(filename=imagem_inicial,scale=escala,center_x=center_x,center_y=center_y)
        self.current_texture = 0
        self.textures = texture_list
        self._angle = angulo
        self.tamanho_lista = len(self.textures)
        self.timer = 0
        self.tamanho = 32
        self.escala = escala

    def update(self,delta_time):
        self.timer += delta_time
        if self.timer >= 0.04:
            self.current_texture += 1
            if self.current_texture < self.tamanho_lista:
                self.set_texture(self.current_texture)
            else:
                self.kill()
            self.timer = 0

class Explosao_central(Explosao):
    def __init__(self,texture_list,img="img/explosao/explosao_central1.png",escala=0.66,center_x=0,center_y=0,angulo=0):
        super().__init__(texture_list,img,escala,center_x,center_y,angulo)

class Explosao_trilho(Explosao):
    def __init__(self,texture_list,img="img/explosao/explosao_trilho1.png",escala=0.66,center_x=0,center_y=0,angulo=0):
        super().__init__(texture_list,img,escala,center_x,center_y,angulo)

class Explosao_fim(Explosao):
    def __init__(self,texture_list,img="img/explosao/explosao_fim1.png",escala=0.66,center_x=0,center_y=0,angulo=0):
        super().__init__(texture_list,img,escala,center_x,center_y,angulo)
