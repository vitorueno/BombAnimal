import arcade
from app.personagens import *
from app.bombas.bomba import Bomba

TEXTURE_RIGHT = 0
TEXTURE_LEFT = 1
TEXTURE_TOP_LEFT = 2
TEXTURE_TOP_RIGHT = 3
TEXTURE_TOP_STAND = 4
TEXTURE_BOTTOM = 5

class Player(arcade.Sprite):
    def __init__(self,arquivo,scale=1,velocidade=3,x=0,y=0,bombas=1,forca=1,c=arcade.key.W,b=arcade.key.S,d=arcade.key.D,e=arcade.key.A,bomb=arcade.key.SPACE,ganhou=None,limite_imortal=1.5):
        super().__init__(scale=scale,center_x=x,center_y=y)
        self.arquivo = arquivo
        self.num_bombas = bombas
        self.forca = 1
        self.velocidade = velocidade
        self.imortal = False
        self.tempo_imortal = 0.0
        self.limite_imortal = limite_imortal
        self.cima = False
        self.baixo = False
        self.esquerda = False
        self.direita = False
        self.c = c
        self.b = b
        self.d = d
        self.e = e
        self.bomb = bomb
        self.plantado = False
        self.som = arcade.sound.load_sound("app/sound/down.wav")
        self.ganhou = ganhou
        self.vento = 0
        self.fogo = 0
        self.macaco = False
        self.capacete = False
        self.timer_andar = 0.0

    def mover(self):
        self.change_x = 0
        self.change_y = 0

        #só cima
        if self.cima and not self.baixo and not self.direita and not self.esquerda:
            self.change_y += self.velocidade

        #só baixo
        elif self.baixo and not self.cima and not self.direita and not self.esquerda:
            self.change_y -= self.velocidade

        #só esquerda
        elif self.esquerda and not self.direita and not self.cima and not self.baixo:
            self.change_x -= self.velocidade

        #só direita
        elif self.direita and not self.esquerda and not self.cima and not self.baixo:
            self.change_x += self.velocidade

        #cima direita
        elif self.cima and not self.baixo and self.direita and not self.esquerda:
            self.change_x += self.velocidade/2
            self.change_y += self.velocidade/2
        
        #cima esquerda
        elif self.cima and not self.baixo and not self.direita and self.esquerda:
            self.change_x -= self.velocidade/2
            self.change_y += self.velocidade/2

        #baixo direita
        elif self.baixo and not self.cima and self.direita and not self.esquerda:
            self.change_x += self.velocidade/2
            self.change_y -= self.velocidade/2

        #baixo esquerda
        elif self.baixo and not self.cima and not self.direita and self.esquerda:
            self.change_x -= self.velocidade/2
            self.change_y -= self.velocidade/2

    def on_key_press(self,key,key_modifiers):
        if key == self.c:
            self.cima = True
        if key == self.b:
            self.baixo = True
        if key == self.d:
            self.direita = True
        if key == self.e:
            self.esquerda = True
        if key == self.bomb and self.num_bombas > 0:
            return True
            
    
    def on_key_release(self,key,key_modifiers):
        if key == self.c:
            self.cima = False
        if key == self.b:
            self.baixo = False
        if key == self.d:
            self.direita = False
        if key == self.e:
            self.esquerda = False

    def plantar_bomba(self):
        pos_x = ((self.center_x // 32) * 32) + 16 
        pos_y = ((self.center_y // 32) * 32) + 16
        bomba = Bomba(0.5, x= pos_x, y= pos_y, forca=self.forca, player=self, limite=2.75)
        self.num_bombas -= 1
        return bomba
        
    def evitar_fuga(self,largura,altura):
        if self.left < 0:
            self.left = 0
        if self.right > largura:
            self.right = largura-1
        if self.top > altura:
            self.top = altura-1
        if self.bottom < 0:
            self.bottom = 0
    
    def set_num_bombas(self,num_bombas):
        self.num_bombas = num_bombas

    def esta_morto(self,delta_time):
        morto = False

        if self.capacete:
            self.imortal = True
            self.capacete = False

        if not self.capacete and not self.imortal:
            arcade.sound.play_sound(self.som)
            self.ganhou = False
            morto = True
            self.kill()
            del(self)

        return morto

    def atualizar_imortal(self,delta_time):
        if self.imortal:
            self.tempo_imortal += delta_time
            if self.tempo_imortal >= self.limite_imortal:
                self.tempo_imortal = 0.0
                self.imortal = False

    def mudar_texturas(self,delta_time):
        self.timer_andar += delta_time
        if self.timer_andar >= 2.0:
            self.timer_andar = 0.0
            

        if self.change_x < 0:
            self.set_texture(TEXTURE_LEFT)
        if self.change_x > 0:
            self.set_texture(TEXTURE_RIGHT)
        if self.change_y > 0:
            if self.timer_andar < 0.5:
                self.set_texture(TEXTURE_TOP_LEFT)
            elif self.timer_andar >= 0.5 and self.timer_andar < 1:
                self.set_texture(TEXTURE_TOP_STAND)
            elif self.timer_andar >= 1 and self.timer_andar < 1.5:
                self.set_texture(TEXTURE_TOP_RIGHT)
            elif self.timer_andar >= 1.5:
                self.set_texture(TEXTURE_TOP_STAND)
        

    
        if self.change_y < 0:
            self.set_texture(TEXTURE_BOTTOM)
        if self.change_x == 0 and self.change_y == 0:
            self.set_texture(TEXTURE_BOTTOM)

    def update_colisao(self,lista_paredes):
        self.center_x += self.change_x
        colisoes = arcade.check_for_collision_with_list(self,lista_paredes)

        if len(colisoes) > 0:

            if self.change_x > 0:
                for colisao in colisoes:
                    self.right = min(colisao.left,self.right)

            elif self.change_x < 0:
                for colisao in colisoes:
                    self.left = max(colisao.right,self.left)
            
        self.center_y += self.change_y
        colisoes = arcade.check_for_collision_with_list(self,lista_paredes)

        if len(colisoes) > 0:
            if self.change_y > 0:
                for colisao in colisoes:
                    self.top = min(colisao.bottom,self.top)

            elif self.change_y < 0:
                for colisao in colisoes:
                    self.bottom = max(colisao.top, self.bottom)