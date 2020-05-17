import arcade
from .player import Player
from app.var import IMG_ARARA


class Arara(Player):
    def __init__(self, x=0, y=0, tipo_player = 1, arquivo=IMG_ARARA, scale=1.09, 
                 velocidade=3,bombas=1,forca=1):
        super().__init__(arquivo=arquivo, scale=scale, velocidade=velocidade, x=x,
                        y=y, bombas=bombas,forca=forca,tipo_player=tipo_player)
        self.tipo = "arara"
        #self.som = arcade.load_sound("sound/voo.mp3")
        self.recarga_pulo = 0
        self.pulou = False
        self.load_images(self.tipo)

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
