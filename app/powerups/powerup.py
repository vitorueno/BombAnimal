import arcade
from app.blocos.bloco import Bloco

class Powerup(Bloco):
    def __init__(self,imagem,escala=0,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)
        self.som_coleta = arcade.load_sound("app/sound/powerup.wav")

    def coletar_powerUp(self,player):
        arcade.sound.play_sound(self.som_coleta)
        self.melhorar_player(player)
        self.kill()
    
    def melhorar_player(self,player):
        pass