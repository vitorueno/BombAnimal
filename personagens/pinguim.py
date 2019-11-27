import arcade
from .player import Player

TEXTURE_RIGHT = 0
TEXTURE_LEFT = 1
TEXTURE_TOP_LEFT = 2
TEXTURE_TOP_RIGHT = 3
TEXTURE_BOTTOM = 4

class Pinguim(Player):
    def __init__(self,x=0,y=0,c=arcade.key.W,b=arcade.key.S,d=arcade.key.D,e=arcade.key.A,bomb=arcade.key.SPACE,
                arquivo="img/animais/pinguim/pinguim1.png",scale=1.09,velocidade=3,bombas=2,forca=1):
        super().__init__(arquivo=arquivo,scale=scale,velocidade=velocidade,x=x,y=y,bombas=bombas,forca=forca,c=c,b=b,d=d,e=e,bomb=bomb)
        self.tipo = "pinguim"
        self.load_images("img/animais/pinguim/",1.09)

    def load_images(self,arquivo,escala):

        #se for pra direita ele usa o sprite pro lado 
        self.textures.append(arcade.load_texture(arquivo+"pinguim4.png",scale=escala))

        #se for pra esquerda ele usa o sprite pro lado, porém espelhados
        self.textures.append(arcade.load_texture(arquivo+"pinguim4.png",scale=escala, mirrored=True))

        #pra cima ele usa os sprite pra cima 
        self.textures.append(arcade.load_texture(arquivo+"pinguim3.png",scale=escala))
        self.textures.append(arcade.load_texture(arquivo+"pinguim3.png",scale=escala, mirrored= True))
        self.textures.append(arcade.load_texture(arquivo+'pinguim2.png',scale=escala))

        #pra bajxo ele usa o sprite padrão 
        self.textures.append(arcade.load_texture(arquivo+'pinguim1.png',scale=escala))
        
        self.set_texture(TEXTURE_BOTTOM)

        self.texture_change_distance = 20