import arcade

class Explosao(arcade.Sprite):
    pos_central = None
    def __init__(self,texture_list,imagem,center_x,center_y,angulo):
        imagem_inicial = imagem 
        super().__init__(filename=imagem_inicial,center_x=center_x,center_y=center_y)
        self.current_texture = 0
        self.textures = texture_list
        self._angle = angulo
        self.tamanho_lista = len(self.textures)
        self.timer = 0
        self.tamanho = 32
        self.isolada = False
        

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
    def __init__(self,texture_list,center_x=0,center_y=0,angulo=0,img="img/explosao/explosao_central1.png"):
        super().__init__(texture_list,img,center_x,center_y,angulo)
    
    

class Explosao_trilho(Explosao):
    def __init__(self,texture_list,center_x=0,center_y=0,angulo=0,img="img/explosao/explosao_trilho1.png"):
        super().__init__(texture_list,img,center_x,center_y,angulo)

class Explosao_fim(Explosao):
    def __init__(self,texture_list,center_x=0,center_y=0,angulo=0,img="img/explosao/explosao_fim1.png"):
        super().__init__(texture_list,img,center_x,center_y,angulo)