import arcade
from .player import Player

#0.06
TEXTURE_RIGHT = 0
TEXTURE_LEFT = 1
TEXTURE_TOP_LEFT = 2
TEXTURE_TOP_RIGHT = 3
TEXTURE_BOTTOM = 4


class Arara(Player):
    def __init__(self,x=0,y=0,c=arcade.key.W,b=arcade.key.S,d=arcade.key.D,e=arcade.key.A,bomb=arcade.key.SPACE,
                arquivo="app/img/animais/arara/arara1.png",scale=1.09,velocidade=3,bombas=1,forca=1):
        super().__init__(arquivo=arquivo,scale=scale,velocidade=velocidade,x=x,y=y,bombas=bombas,forca=forca,c=c,b=b,d=d,e=e,bomb=bomb)
        self.tipo = "arara"
        #self.som = arcade.load_sound("sound/voo.mp3")
        self.recarga_pulo = 0
        self.pulou = False
        self.load_images("app/img/animais/arara/",1.09)

    def pular_parede(self,paredes,mapa,delta_time):
        TEMPO_RECARGA_PULO = 5

        pos_x = ((self.center_x // 32) * 32) + 16 
        pos_y = ((self.center_y // 32) * 32) + 16
       
        if self.change_x > 0 and self.change_y == 0:
            existe_parede1 = mapa.get_bloco_da_coord(pos_x + 32,pos_y)
            existe_parede2 = mapa.get_bloco_da_coord(pos_x + 64,pos_y)
            
            if existe_parede1 and not existe_parede2 and not self.pulou:
                #arcade.play_sound(self.som)
                self.center_x += 64
                self.pulou = True

        elif self.change_x < 0 and self.change_y == 0:
            existe_parede1 = mapa.get_bloco_da_coord(pos_x - 32,pos_y)
            existe_parede2 = mapa.get_bloco_da_coord(pos_x - 64,pos_y)
            
            if existe_parede1 and not existe_parede2 and not self.pulou: 
                #arcade.play_sound(self.som)
                self.center_x -= 64
                self.pulou = True
        
        elif self.change_y > 0 and self.change_x == 0:
            existe_parede1 = mapa.get_bloco_da_coord(pos_x,pos_y + 32)
            existe_parede2 = mapa.get_bloco_da_coord(pos_x,pos_y + 64)
            
            if existe_parede1 and not existe_parede2 and not self.pulou:
                #arcade.play_sound(self.som)
                self.center_y += 64
                self.pulou = True
            
        elif self.change_y < 0 and self.change_x == 0:
            existe_parede1 = mapa.get_bloco_da_coord(pos_x,pos_y - 32)
            existe_parede2 = mapa.get_bloco_da_coord(pos_x,pos_y - 64)
            
            if existe_parede1 and not existe_parede2 and not self.pulou:
                #arcade.play_sound(self.som)
                self.center_y -= 64
                self.pulou = True

        if self.pulou:
            self.recarga_pulo += delta_time
            #print(self.recarga_pulo)
            if self.recarga_pulo >= TEMPO_RECARGA_PULO:
                self.pulou = False
                self.recarga_pulo = 0

    def load_images(self,arquivo,escala):
        #se for pra direita ele usa o sprite pro lado 
        self.textures.append(arcade.load_texture(arquivo+"arara4.png",scale=escala))

        #se for pra esquerda ele usa o sprite pro lado, porém espelhados
        self.textures.append(arcade.load_texture(arquivo+"arara4.png",scale=escala, mirrored=True))

        #pra cima ele usa os sprite pra cima 
        self.textures.append(arcade.load_texture(arquivo+"arara3.png",scale=escala))
        self.textures.append(arcade.load_texture(arquivo+"arara3.png",scale=escala, mirrored= True))
        self.textures.append(arcade.load_texture(arquivo+'arara2.png',scale=escala))

        #pra baixo ele usa o sprite padrão 
        self.textures.append(arcade.load_texture(arquivo+'arara1.png',scale=escala))
        
        self.set_texture(TEXTURE_BOTTOM)

        self.texture_change_distance = 20

    