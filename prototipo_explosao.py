import arcade
import random
import time
from player import Player 
from bloco import Bloco
from destrutivel import Destrutivel
from indestrutivel import Indestrutivel

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bombanimal"
SPRITE_SCALING_PLAYER = 0.06
SPRITE_SCALING = 0.69
ORIGINAL_SPRITE_SIZE = 900
SPRITE_SIZE = ORIGINAL_SPRITE_SIZE * SPRITE_SCALING
MOVEMENT_SPEED = 5
NUM_DESTRUTIVOS = 10
EXPLOSION_TEXTURE_COUNT = 7


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        #fisica
        self.physics_engine = None
        self.physics_engine2 = None
        self.physics_engine3 = None

        #inicializar listas
        self.wall_list = None
        self.destrutiveis = None
        self.indestrutiveis = None
        self.player_list = None
        self.bomb_list = None
        self.explosao_list = None
        self.power_up_list = None

        #inicializar sprites dos players
        self.player1_sprite = None
        self.player2_sprite = None
    

    def setup(self):
        #listas com sprites
        self.wall_list = arcade.SpriteList()
        self.destrutiveis = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.explosao_list = arcade.SpriteList()
        self.power_up_list = arcade.SpriteList()

        #sprite player 1
        self.player1_sprite = Player("img/character1.png", SPRITE_SCALING_PLAYER,MOVEMENT_SPEED,x=50,y=50,vidas=2)
        self.player_list.append(self.player1_sprite)

        #sprite player 2
        self.player2_sprite = Player("img/panda1.png",SPRITE_SCALING_PLAYER,MOVEMENT_SPEED,x=SCREEN_WIDTH-49,y=SCREEN_HEIGHT-12,
        c=arcade.key.UP,b=arcade.key.DOWN,d=arcade.key.RIGHT,e=arcade.key.LEFT,bomb=arcade.key.ENTER,vidas=2)
        self.player_list.append(self.player2_sprite)
        
        #criar blocos
        for y in range(40,780,130):
            for x in range(120,720,115):
                bloco = Indestrutivel("img/bloco70.png",SPRITE_SCALING,x,y)
                self.wall_list.append(bloco)

        #criar blocos destrutiveis (aleatórios)

        destrutivo = NUM_DESTRUTIVOS
        while destrutivo > 0:
            destrutivel = Destrutivel("img/box70.png", SPRITE_SCALING)
            posicionado = False
            while not posicionado:
                destrutivel.center_x = random.randrange(SCREEN_WIDTH)
                destrutivel.center_y = random.randrange(SCREEN_HEIGHT)
                destrutivel.manter_na_tela(SCREEN_WIDTH,SCREEN_HEIGHT)
                colisao_bloco = arcade.check_for_collision_with_list(destrutivel, self.wall_list)
                colisao_player = arcade.check_for_collision_with_list(destrutivel,self.player_list)
                distancia_p1 = arcade.get_distance_between_sprites(destrutivel,self.player1_sprite)
                distancia_p2 = arcade.get_distance_between_sprites(destrutivel,self.player2_sprite)
                if len(colisao_bloco) == 0 and len(colisao_player) == 0 and distancia_p1 > 55 and distancia_p2 > 55:
                    posicionado = True
            destrutivo -= 1
            self.wall_list.append(destrutivel)
        
        self.textura_explosao_central = []
        self.textura_explosao_trilho = []
        self.textura_explosao_fim = []
        for i in range(1,EXPLOSION_TEXTURE_COUNT+1):
            central = f"img/explosao/explosao_central{i}.png"
            trilho = f"img/explosao/explosao_trilho{i}.png"
            fim = f"img/explosao/explosao_fim{i}.png"
            self.textura_explosao_central.append(arcade.load_texture(central))
            self.textura_explosao_trilho.append(arcade.load_texture(trilho))
            self.textura_explosao_fim.append(arcade.load_texture(fim))
        

        self.texturas_totais_explosao = [self.textura_explosao_central,
                                        self.textura_explosao_trilho,
                                        self.textura_explosao_fim]


        #definir engine de física que cuida das colisões
        self.physics_engine = arcade.PhysicsEngineSimple(self.player1_sprite,self.wall_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.player2_sprite,self.wall_list)
            
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        self.bomb_list.draw()
        self.explosao_list.draw()
        self.power_up_list.draw()

    def update(self, delta_time):
        #atualizar fisica do jogo (checagens de colisão)
        self.physics_engine.update()
        self.physics_engine2.update()
        
        
        #movimentação player 1 e 2
        for player in self.player_list:
            player.mover()
            player.evitar_fuga(SCREEN_WIDTH,SCREEN_HEIGHT)

        for bomba_plantada in self.bomb_list:
            explodiu = bomba_plantada.explodir(delta_time,self.texturas_totais_explosao)
            if explodiu is not None:
                for pedaco_explosao in explodiu:
                    self.explosao_list.append(pedaco_explosao)


        for explosao in self.explosao_list:
            explosao.update(delta_time)
            hits_paredes = arcade.check_for_collision_with_list(explosao,self.wall_list)
            hits_players = arcade.check_for_collision_with_list(explosao,self.player_list)
            for parede_atingida in hits_paredes:
                indestrutivel = isinstance(parede_atingida,Indestrutivel)
                if indestrutivel:
                    explosao.kill()
                else:
                    power_up = parede_atingida.destruir_bloco()
                    if power_up is not None:
                        self.power_up_list.append(power_up)

            for player_atingido in hits_players:
                player_atingido.vidas -= 1
                if player_atingido.vidas == 0:
                    arcade.sound.play_sound(player_atingido.som)
                    player_atingido.kill()

        if self.power_up_list is not None:
            for power_up in self.power_up_list:
                power_up.update()
                coletas = arcade.check_for_collision_with_list(power_up,self.player_list)
                for coleta in coletas:
                    power_up.coletar_powerUp(coleta)
    
    def on_key_press(self, key, key_modifiers):
        #verificar tecla pressionada
        for player in self.player_list:
            bomba_solicitada = player.on_key_press(key,key_modifiers)
            if bomba_solicitada:
                bomba = player.plantar_bomba()
                self.bomb_list.append(bomba)


    def on_key_release(self, key, key_modifiers):
        #verificar tecla despressionada
        for player in self.player_list:
            player.on_key_release(key,key_modifiers)

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()