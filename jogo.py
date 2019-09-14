import arcade
import random
import time
from personagens.arara import Arara 
from personagens.lebre import Lebre
from personagens.pinguim import Pinguim
from personagens.panda import Panda
from blocos.destrutivel import Destrutivel
from blocos.indestrutivel import Indestrutivel
from hud import Hud
from mapa import Mapa
from menu import Menu
from selecao import Selecao_personagem
from pause import Tela_pause
from pos_partida import Pos_partida
from bombas.explosao import Explosao_central

SCREEN_WIDTH = HUD_WIDTH = 800
SCREEN_HEIGHT = 600
HUD_HEIGHT = 50
HUD_CENTER_X = SCREEN_WIDTH / 2
HUD_CENTER_Y = SCREEN_HEIGHT - HUD_HEIGHT//2
DURACAO_PARTIDA = 120.00
SCREEN_TITLE = "Bombanimal"
SPRITE_SCALING = 0.69
ORIGINAL_SPRITE_SIZE = 900
SPRITE_SIZE = ORIGINAL_SPRITE_SIZE * SPRITE_SCALING
MOVEMENT_SPEED = 5
NUM_DESTRUTIVOS = 10
EXPLOSION_TEXTURE_COUNT = 7


#numeros que representam os estados
MENU = 0
SELECAO_PERSONAGEM = 1
PARTIDA = 2
PAUSE = 3 
POS_PARTIDA = 4
OPCOES = 5
SAIR = 6

class Jogo(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title,resizable=False)
        arcade.set_background_color(arcade.color.AMAZON)

        self.pausado = False

        #interface
        #carregar apenas na execução do jogo
        self.hud = None
        self.mapa = None
        self.pos_partida = None
        

        #carregar antes porque são importantes
        self.selecao_personagem = Selecao_personagem(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.menu = Menu(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.tela_pause = Tela_pause(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.estado_atual = MENU
        


        #fisica
        self.physics_engine = None
        self.physics_engine2 = None
        self.physics_engine3 = None

        #inicializar listas
        self.wall_list = None
        self.background_list = None
        self.destrutiveis = None
        self.indestrutiveis = None
        self.player_list = None
        self.bomb_list = None
        self.explosao_list = None
        self.power_up_list = None

        #inicializar players
        self.player1_sprite = None
        self.player2_sprite = None
        self.tipo_p1 = "pinguim" 
        self.tipo_p2 = "lebre"
        

    def setup(self):
        if self.estado_atual == PARTIDA:
            #listas com sprites
            self.wall_list = arcade.SpriteList()
            self.background_list = arcade.SpriteList()
            self.destrutiveis = arcade.SpriteList()
            self.player_list = arcade.SpriteList()
            self.bomb_list = arcade.SpriteList()
            self.explosao_list = arcade.SpriteList()
            self.power_up_list = arcade.SpriteList()

            #personagens
            if self.tipo_p1 == "arara":
                self.player1_sprite = Arara(x=16,y=16)
            elif self.tipo_p1 == "lebre":
                self.player1_sprite = Lebre(x=16,y=16)
            elif self.tipo_p1 == "pinguim":
                self.player1_sprite = Pinguim(x=16,y=16)
            elif self.tipo_p1 == "panda":
                self.player1_sprite = Panda(x=16,y=16)

            if self.tipo_p2 == "arara":
                self.player2_sprite = Arara(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,c=arcade.key.UP,b=arcade.key.DOWN,
                                            d=arcade.key.RIGHT,e=arcade.key.LEFT,bomb=arcade.key.ENTER)
            elif self.tipo_p2 == "lebre":
                self.player2_sprite = Lebre(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,c=arcade.key.UP,b=arcade.key.DOWN,
                                            d=arcade.key.RIGHT,e=arcade.key.LEFT,bomb=arcade.key.ENTER)
            elif self.tipo_p2 == "pinguim":
                self.player2_sprite = Pinguim(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,c=arcade.key.UP,b=arcade.key.DOWN,
                                            d=arcade.key.RIGHT,e=arcade.key.LEFT,bomb=arcade.key.ENTER)
            elif self.tipo_p2 == "panda":
                self.player2_sprite = Panda(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,c=arcade.key.UP,b=arcade.key.DOWN,
                                            d=arcade.key.RIGHT,e=arcade.key.LEFT,bomb=arcade.key.ENTER)

            self.player_list.append(self.player1_sprite)
            self.player_list.append(self.player2_sprite)

            #interface
            self.hud = Hud(HUD_WIDTH,HUD_HEIGHT,HUD_CENTER_X,HUD_CENTER_Y,DURACAO_PARTIDA,self.player1_sprite,self.player2_sprite)
            self.mapa = Mapa(SCREEN_WIDTH,SCREEN_HEIGHT-HUD_HEIGHT,32,32)
            self.pos_partida = Pos_partida(SCREEN_WIDTH,SCREEN_HEIGHT,self.player1_sprite,self.player2_sprite)
            
            self.background_list = self.mapa.get_background()
            self.destrutiveis = self.mapa.get_destrutiveis()

            temp_indestrutiveis = self.mapa.get_indestrutiveis()
            temp_destrutiveis = self.mapa.get_destrutiveis()

            for bloco in temp_indestrutiveis:
                self.wall_list.append(bloco)
            for bloco in temp_destrutiveis:
                self.wall_list.append(bloco)

            #carregar texturas para criar explosões
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
        
    def draw_game(self):
        #listas de coisas desenhadas
        self.background_list.draw()
        self.player_list.draw()
        self.wall_list.draw()
        self.bomb_list.draw()
        self.explosao_list.draw()
        self.power_up_list.draw()

        #interface
        self.hud.draw_hud()

        if self.pausado:
            self.tela_pause.draw()

    def on_draw(self):
        #coisas que serão desenhadas na tela
        arcade.start_render()
        
        if self.estado_atual == MENU:
            self.menu.draw_menu()
        elif self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.draw_selecao()
        elif self.estado_atual == PARTIDA:
            self.draw_game()
        elif self.estado_atual == POS_PARTIDA:
            self.pos_partida.draw_pos_partida()
    
    def update(self, delta_time):
        if self.estado_atual == MENU:
            self.set_mouse_visible(True)
        elif self.estado_atual == SELECAO_PERSONAGEM: 
            self.set_mouse_visible(True)
        elif self.estado_atual == PARTIDA:
            if not self.pausado:
                #hud
                self.hud.atualizar_tempo(delta_time)
                self.hud.atualizar_powerups(self.player1_sprite,self.player2_sprite)

                #atualizar fisica do jogo (checagens de colisão)
                self.physics_engine.update()
                self.physics_engine2.update()
                
                #movimentação player 1 e 2
                for player in self.player_list:
                    player.mover()
                    player.evitar_fuga(SCREEN_WIDTH,SCREEN_HEIGHT-HUD_HEIGHT)

                for bomba_plantada in self.bomb_list:
                    explodiu = bomba_plantada.explodir(delta_time,self.texturas_totais_explosao)
                    if explodiu is not None:
                        for pedaco_explosao in explodiu:
                            self.explosao_list.append(pedaco_explosao)

                #checar colisão das explosões com blocos
                for explosao in self.explosao_list:

                    explosao.update(delta_time)
                    hits_paredes = arcade.check_for_collision_with_list(explosao,self.wall_list)
                    

                    for parede_atingida in hits_paredes:
                        indestrutivel = isinstance(parede_atingida,Indestrutivel)
                        #se a parede atingida for indestrutível, o pedaço de explosao que a atingiu deve ser excluído (bloqueado)
                        if indestrutivel:
                            #x e y da explosao bloqueada pelo bloco indestrutível
                            x_bloqueado = explosao.center_x
                            y_bloqueado = explosao.center_y

                            #x e y da explosao central 
                            x_central = explosao.pos_central[0]
                            y_central = explosao.pos_central[1]

                            #descobrir onde a explosao bloqueada está em relação à central
                            caso_direita = x_bloqueado > x_central and y_bloqueado == y_central
                            caso_cima = x_bloqueado == x_central and y_bloqueado > y_central
                            caso_esquerda = x_bloqueado < x_central and y_bloqueado == y_central
                            caso_baixo = x_bloqueado == x_central and y_bloqueado < y_central

                            #de acordo com o caso exclui a explosao bloqueada e as subsequentes de sua linha
                            if caso_direita:
                                for explosao_indesejada in self.explosao_list:
                                    if explosao_indesejada.center_x >= x_bloqueado and explosao_indesejada.center_y == y_bloqueado:
                                        explosao_indesejada.kill()
                                        del(explosao_indesejada)
                            elif caso_cima:
                                for explosao_indesejada in self.explosao_list:
                                    if explosao_indesejada.center_x == x_bloqueado and explosao_indesejada.center_y >= y_bloqueado:
                                        explosao_indesejada.kill()
                                        del(explosao_indesejada)
                            elif caso_esquerda:
                                for explosao_indesejada in self.explosao_list:
                                    if explosao_indesejada.center_x <= x_bloqueado and explosao_indesejada.center_y == y_bloqueado:
                                        explosao_indesejada.kill()
                                        del(explosao_indesejada)
                            elif caso_baixo:
                                for explosao_indesejada in self.explosao_list:
                                    if explosao_indesejada.center_x == x_bloqueado and explosao_indesejada.center_y <= y_bloqueado:
                                        explosao_indesejada.kill()
                                        del(explosao_indesejada)

                        #se for destrutível ativa o algoritmo de geração de power up que pode ou não ser gerado
                        else:
                            power_up = parede_atingida.destruir_bloco()
                            if power_up is not None:
                                self.power_up_list.append(power_up)

                #nesse ponto a lista de bombas foi atualizada, o que garante que as colisões com player vão ignorar as bombas bloqueadas

                #checar colisão das explosões com players 
                for explosao in self.explosao_list:
                    hits_players = arcade.check_for_collision_with_list(explosao,self.player_list)
                    for player_atingido in hits_players:
                        estado = player_atingido.verificar_sobrevivencia(delta_time)
                        print(estado)
                        if estado is not None:
                            if player_atingido == self.player1_sprite:
                                self.player2_sprite.ganhou = True
                            else:
                                self.player1_sprite.ganhou = True
                            self.estado_atual = POS_PARTIDA

                #checar por colisões com powerups
                if self.power_up_list is not None:
                    for power_up in self.power_up_list:
                        power_up.update()
                        coletas = arcade.check_for_collision_with_list(power_up,self.player_list)
                        for coleta in coletas:
                            power_up.coletar_powerUp(coleta)


        elif self.estado_atual == PAUSE:
            self.set_mouse_visible(True)

        elif self.estado_atual == POS_PARTIDA:
            self.set_mouse_visible(True)
        
        elif self.estado_atual == SAIR:
            self.close()


    def on_key_press(self, key, key_modifiers):
        if self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.on_key_press_p1(key,key_modifiers)
        
        if self.estado_atual == PARTIDA:
            if not self.pausado:
                for player in self.player_list:
                    bomba_solicitada = player.on_key_press(key,key_modifiers)
                    if bomba_solicitada:
                        bomba = player.plantar_bomba()
                        self.bomb_list.append(bomba)

            
                
    def on_key_release(self, key, key_modifiers):
        if self.estado_atual == MENU:
            pass
        elif self.estado_atual == SELECAO_PERSONAGEM:
            pass
        elif self.estado_atual == PARTIDA:
            if not self.pausado:
                for player in self.player_list:
                    player.on_key_release(key,key_modifiers)

                if key == arcade.key.ESCAPE:
                    self.pausado = True

            else:
                if key == arcade.key.ESCAPE:
                    self.pausado = False

        elif self.estado_atual == PAUSE:
            pass
        elif self.estado_atual == POS_PARTIDA:
            pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.estado_atual == MENU:
            self.menu.on_mouse_press_menu(x,y,button,key_modifiers)

        if self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.on_mouse_press_selecao(x,y,button,key_modifiers)

        if self.pausado:
            self.tela_pause.on_mouse_press(x,y,button,key_modifiers)
        
        if self.estado_atual == POS_PARTIDA:
            self.pos_partida.on_mouse_press(x,y,button,key_modifiers)
            

    def on_mouse_release(self,x,y,button,key_modifiers):
        if self.estado_atual == MENU:
            resultado = self.menu.on_mouse_release_menu(x,y,button,key_modifiers)
            if resultado is not None:
                self.estado_atual = resultado

        if self.estado_atual == SELECAO_PERSONAGEM:
            resultado = self.selecao_personagem.on_mouse_release_selecao(x,y,button,key_modifiers)
            if resultado is not None:
                if type(resultado) == int:
                    self.estado_atual = resultado
                elif type(resultado) == tuple:
                    self.estado_atual = resultado[0]
                    self.tipo_p1 = resultado[1]
                    self.tipo_p2 = resultado[2]
                    self.selecao_personagem.personagem_p1 = None
                    self.selecao_personagem.personagem_p2 = None
                    self.setup()
        
        if self.pausado:
            proxima_acao = self.tela_pause.on_mouse_release(x,y,button,key_modifiers)
            if proxima_acao is not None:
                if proxima_acao == PAUSE:
                    self.pausado = False
                else:
                    self.estado_atual = proxima_acao
        
        if self.estado_atual == POS_PARTIDA:
            proxima_tela = self.pos_partida.on_mouse_release(x,y,button,key_modifiers)
            if proxima_tela is not None:
                if proxima_tela == PARTIDA:
                    self.player1_sprite.ganhou = None
                    self.player2_sprite.ganhou = None
                    self.estado_atual = PARTIDA
                    self.setup()
                else:
                    self.estado_atual = proxima_tela

def main():
    """ Main method """
    game = Jogo(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()