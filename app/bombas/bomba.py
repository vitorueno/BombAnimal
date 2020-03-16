import arcade
from app.blocos.bloco import Bloco
from .explosao import Explosao_central,Explosao_trilho,Explosao_fim

class Bomba(arcade.Sprite):
    def __init__(self, escala=0.5, imagem="app/img/bombas/bomba3.png", player=None, x=0, y=0, forca=1, limite=4):
        self.player = player
        super().__init__(imagem,escala,center_x=x,center_y=y)
        self.raio = forca
        self.timer = 0
        self.limite = limite
        #self.quantidade_bombas_original = player.num_bombas
        self.som_explosao = arcade.sound.load_sound("app/sound/explosion.wav")
        self.som_colocar_bomba = arcade.sound.load_sound("app/sound/naosei.wav")
        arcade.sound.play_sound(self.som_colocar_bomba)
        self.empurrada = False


    def explodir(self,delta_time,lista_texturas_explosao):
        if self.timer >= self.limite:
            arcade.sound.play_sound(self.som_explosao)
            explodiu = self.criar_explosao(lista_texturas_explosao)
            if self.player is not None:
                self.player.num_bombas += 1
            self.kill()
            self.timer = 0
            return explodiu
        self.timer += delta_time
        

    def criar_explosao(self,lista):
        x = self.center_x 
        y = self.center_y
        tam = 0
        explosao = []

        for i in range(0,self.raio+1):
            #0,1,2,3,4

            #1
            if i == 0:
                #centro da explosão
                central = Explosao_central(lista[0],x,y)
                explosao.append(central)
                tam = central.tamanho

            #2,3
            elif i > 0 and i < self.raio:
                #cima
                explosao.append(Explosao_trilho(lista[1], x, y + tam, angulo=90))
                #direitas
                explosao.append(Explosao_trilho(lista[1], x + tam, y, angulo=0))
                #baixo 
                explosao.append(Explosao_trilho(lista[1], x, y - tam, angulo=270)) 
                #esquerda
                explosao.append(Explosao_trilho(lista[1], x - tam, y, angulo=180))  
                tam += central.tamanho 

            #4
            else:
                #cima
                explosao.append(Explosao_fim(lista[2], x, y + tam, angulo=90))
                #direita
                explosao.append(Explosao_fim(lista[2], x + tam, y, angulo=0))
                #baixo
                explosao.append(Explosao_fim(lista[2],x, y - tam, angulo=270)) 
                #esquerda
                explosao.append(Explosao_fim(lista[2],x - tam, y, angulo=180)) 

                for explo in explosao:
                    explo.pos_central = (self.center_x,self.center_y)

        return explosao

        
        
        
        
