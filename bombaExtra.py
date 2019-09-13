import arcade
from powerup import Powerup

class BombaExtra(Powerup):
    def __init__(self,imagem ="img/powerups/bombaExtra.png",escala=0.03,center_x=0,center_y=0):
        super().__init__(imagem,escala,center_x,center_y)

    def coletar_powerUp(self,player):
        arcade.sound.play_sound(self.som_coleta)
        self.melhorarPlayer(player)
        self.kill()

    def melhorarPlayer(self,player):
        if player.num_bombas < 5:
            player.num_bombas += 1
            return True
        return False