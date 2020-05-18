from app import * 
 

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
        self.selecao_personagem = Selecao_personagem()
        self.menu = Menu()
        self.tela_pause = Tela_pause()
        self.ajuda = Ajuda()
        self.configuracoes = Configuracoes(config_atual)
        self.estado_atual = MENU

        #fisica
        self.physics_engine = None
        self.physics_engine2 = None

        #inicializar listas
        self.wall_list = None
        self.background_list = None
        self.destrutiveis = None
        self.indestrutiveis = None
        self.player_list = None
        self.bomb_list = None
        self.explosao_list = None
        self.power_up_list = None
        self.lista_intransponiveis = None

        #inicializar players
        self.player1 = None
        self.player2 = None
        self.tipo_p1 = "pinguim" 
        self.tipo_p2 = "lebre"
        
        self.timer_morte_subita = DURACAO_PARTIDA
        self.morte_subita = None
        self.random_bomb_list = None

    def setup(self):
        global config_atual

        if self.estado_atual == PARTIDA:

            self.morte_subita = False
            self.timer_morte_subita = DURACAO_PARTIDA

            #listas com sprites
            self.wall_list = arcade.SpriteList()
            self.background_list = arcade.SpriteList()
            self.destrutiveis = arcade.SpriteList()
            self.player_list = arcade.SpriteList()
            self.bomb_list = arcade.SpriteList()
            self.explosao_list = arcade.SpriteList()
            self.power_up_list = arcade.SpriteList()
            self.lista_intransponiveis = arcade.SpriteList()
            self.random_bomb_list = arcade.SpriteList()

            #personagens
            if self.tipo_p1 == "arara":
                self.player1 = Arara(x=16,y=16)

            elif self.tipo_p1 == "lebre":
                self.player1 = Lebre(x=16,y=16)

            elif self.tipo_p1 == "pinguim":
                self.player1 = Pinguim(x=16,y=16)

            elif self.tipo_p1 == "panda":
                self.player1 = Panda(x=16,y=16)

            if self.tipo_p2 == "arara":
                self.player2 = Arara(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,tipo_player=2)

            elif self.tipo_p2 == "lebre":
                self.player2 = Lebre(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,tipo_player=2)

            elif self.tipo_p2 == "pinguim":
                self.player2 = Pinguim(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,tipo_player=2)

            elif self.tipo_p2 == "panda":
                self.player2 = Panda(x=SCREEN_WIDTH-16,y=SCREEN_HEIGHT-16,tipo_player=2)

            self.player_list.append(self.player1)
            self.player_list.append(self.player2)

            #interface
            self.hud = Hud(DURACAO_PARTIDA,self.player1,self.player2)
            self.mapa = Mapa()
            self.pos_partida = Pos_partida(self.player1,self.player2)
            

            self.background_list = self.mapa.get_background()
            self.destrutiveis = self.mapa.get_destrutiveis()

            temp_indestrutiveis = self.mapa.get_indestrutiveis()
            temp_destrutiveis = self.mapa.get_destrutiveis()

            for bloco in temp_indestrutiveis:
                self.wall_list.append(bloco)
                self.lista_intransponiveis.append(bloco)
            for bloco in temp_destrutiveis:
                self.wall_list.append(bloco)
                self.lista_intransponiveis.append(bloco)

            #carregar texturas para criar explosões
            self.textura_explosao_central = []
            self.textura_explosao_trilho = []
            self.textura_explosao_fim = []
            for i in range(1,EXPLOSION_TEXTURE_COUNT+1):
                central = f"app/img/explosao/explosao_central{i}.png"
                trilho = f"app/img/explosao/explosao_trilho{i}.png"
                fim = f"app/img/explosao/explosao_fim{i}.png"
                self.textura_explosao_central.append(arcade.load_texture(central))
                self.textura_explosao_trilho.append(arcade.load_texture(trilho))
                self.textura_explosao_fim.append(arcade.load_texture(fim))
            

            self.texturas_totais_explosao = [self.textura_explosao_central,
                                            self.textura_explosao_trilho,
                                            self.textura_explosao_fim]
    
            
    def draw_game(self):
        #listas de coisas desenhadas
        self.background_list.draw()
        self.player_list.draw()
        if self.timer_morte_subita > 0:
            self.wall_list.draw()
        self.bomb_list.draw()
        self.explosao_list.draw()
        self.power_up_list.draw()
        self.random_bomb_list.draw()

        #interface
        self.hud.draw()

        if self.pausado:
            self.tela_pause.draw()

    def on_draw(self):
        #coisas que serão desenhadas na tela
        arcade.start_render()
        
        if self.estado_atual == MENU:
            self.menu.draw()
        elif self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.draw()
        elif self.estado_atual == PARTIDA:
            self.draw_game()
        elif self.estado_atual == POS_PARTIDA:
            self.pos_partida.draw()
        elif self.estado_atual == AJUDA:
            self.ajuda.draw()
        elif self.estado_atual == OPCOES:
            self.configuracoes.draw()

    
    def update(self, delta_time):
        if self.estado_atual == MENU:
            self.set_mouse_visible(True)
        if self.estado_atual == SELECAO_PERSONAGEM: 
            self.set_mouse_visible(True)
        if self.estado_atual == PARTIDA:
            if not self.pausado:
                self.timer_morte_subita -= delta_time
                #atualizando informações da hud
                self.hud.atualizar_tempo(delta_time)
                self.hud.atualizar_powerups(self.player1,self.player2)

                if self.timer_morte_subita <= 0:
                    self.morte_subita = True

                if self.morte_subita:
                    for bloco in self.wall_list:
                        bloco.kill() 
                        del(bloco)
                    self.morte_subita = False

                    if len(self.random_bomb_list) < LIMITE_BOMBAS_MORTE_SUBITA:
                        random_x = random.randint(0,800)
                        random_y = random.randint(0,600)
                        random_bomb = Bomba(x=random_x,y=random_y,forca=4)
                        self.random_bomb_list.append(random_bomb)
                        self.bomb_list.append(random_bomb)



                #movimentação player 1 e 2
                for player in self.player_list:
                    player.update_colisao(self.lista_intransponiveis)
                    player.mover()
                    player.evitar_fuga(SCREEN_WIDTH,SCREEN_HEIGHT-HUD_HEIGHT)
                    player.atualizar_imortal(delta_time)
                    player.mudar_texturas(delta_time)
                    if player.tipo == "arara":
                        player.pular_parede(self.lista_intransponiveis,self.mapa,delta_time)
                     
                #atualizando bombas plantadas e verificando a colisão com o item mão de primata
                for bomba_plantada in self.bomb_list:
                    colisao_bomba = arcade.check_for_collision_with_list(bomba_plantada,self.player_list)
                    for player in colisao_bomba:
                        if player.change_x > 0 and player.center_x < bomba_plantada.left:
                            if player.macaco and not bomba_plantada.empurrada:
                                existe_bloco = self.mapa.get_bloco_da_coord(bomba_plantada.center_x + 32,bomba_plantada.center_y)
                                if not existe_bloco and (bomba_plantada.center_x + 32) <= SCREEN_WIDTH and not bomba_plantada.empurrada:
                                    bomba_plantada.center_x += 32
                                    bomba_plantada.empurrada = True
                                else:
                                    player.right = min(bomba_plantada.left,player.right)
                            else:
                                player.right = min(bomba_plantada.left,player.right)
                        
                        elif player.change_x < 0 and player.center_x > bomba_plantada.right:
                            if player.macaco and not bomba_plantada.empurrada:
                                existe_bloco = self.mapa.get_bloco_da_coord(bomba_plantada.center_x - 32,bomba_plantada.center_y)
                                if not existe_bloco and (bomba_plantada.center_x - 32) >= 0 and not bomba_plantada.empurrada:
                                    bomba_plantada.center_x -= 32
                                    bomba_plantada.empurrada = True
                                else:
                                    player.left = max(bomba_plantada.left,player.right)
                            else:
                                player.left = max(bomba_plantada.left,player.right)

                        elif player.change_y > 0 and player.center_y < bomba_plantada.bottom:
                            if player.macaco and not bomba_plantada.empurrada:
                                existe_bloco = self.mapa.get_bloco_da_coord(bomba_plantada.center_x,bomba_plantada.center_y + 32)
                                if not existe_bloco and (bomba_plantada.center_y + 32) <= SCREEN_HEIGHT and not bomba_plantada.empurrada:
                                    bomba_plantada.center_y += 32
                                    bomba_plantada.empurrada = True
                                else:
                                    player.top = min(bomba_plantada.bottom,player.top)
                            else:
                                player.top = min(bomba_plantada.bottom,player.top)

                        elif player.change_y < 0 and player.center_y > bomba_plantada.top:
                            if player.macaco and not bomba_plantada.empurrada:
                                existe_bloco = self.mapa.get_bloco_da_coord(bomba_plantada.center_x,bomba_plantada.center_y - 32)
                                if not existe_bloco and (bomba_plantada.center_y - 32) >= 0 and not bomba_plantada.empurrada:
                                    bomba_plantada.center_y -= 32
                                    bomba_plantada.empurrada = True
                                else:
                                    player.bottom = max(bomba_plantada.top, player.bottom)
                            else:
                                player.bottom = max(bomba_plantada.top, player.bottom)

                    explodiu = bomba_plantada.explodir(delta_time,self.texturas_totais_explosao)

                   
                    if explodiu is not None:
                        for pedaco_explosao in explodiu:
                            self.explosao_list.append(pedaco_explosao)

                if not self.morte_subita:
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
                        estado = player_atingido.esta_morto(delta_time)
                        if estado:
                            if player_atingido == self.player1:
                                self.player2.ganhou = True
                            else:
                                self.player1.ganhou = True
                            self.estado_atual = POS_PARTIDA

                #checar por colisões com powerups
                if self.power_up_list is not None:
                    for power_up in self.power_up_list:
                        power_up.update()
                        coletas = arcade.check_for_collision_with_list(power_up,self.player_list)
                        for coleta in coletas:
                            power_up.coletar_powerUp(coleta)

        if self.estado_atual == PAUSE:
            self.set_mouse_visible(True)

        if self.estado_atual == POS_PARTIDA:
            self.set_mouse_visible(True)

        if self.estado_atual == AJUDA:
            self.set_mouse_visible(True)

        if self.estado_atual == SAIR:
            self.close()

    #fim do update
 
    def on_key_press(self, key, key_modifiers):
        if self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.on_key_press(key,key_modifiers)
        
        if self.estado_atual == PARTIDA:
            if not self.pausado:
                for player in self.player_list:
                    bomba_solicitada = player.on_key_press(key,key_modifiers)
                    if bomba_solicitada:
                        bomba = player.plantar_bomba()
                        self.bomb_list.append(bomba)

    #fim do on_key_press
                
    def on_key_release(self, key, key_modifiers):
        if self.estado_atual == PARTIDA:
            if not self.pausado:
                for player in self.player_list:
                    player.on_key_release(key,key_modifiers)
                if key == arcade.key.ESCAPE:
                    self.pausado = True
            else:
                if key == arcade.key.ESCAPE:
                    self.pausado = False

        if self.estado_atual == OPCOES:
            self.configuracoes.on_key_release(key,key_modifiers)

    #fim do on_key_release

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.estado_atual == MENU:
            self.menu.on_mouse_press(x,y,button,key_modifiers)

        if self.estado_atual == SELECAO_PERSONAGEM:
            self.selecao_personagem.on_mouse_press(x,y,button,key_modifiers)

        if self.pausado:
            self.tela_pause.on_mouse_press(x,y,button,key_modifiers)
        
        if self.estado_atual == POS_PARTIDA:
            self.pos_partida.on_mouse_press(x,y,button,key_modifiers)
        
        if self.estado_atual == AJUDA:
            self.ajuda.on_mouse_press(x,y,button,key_modifiers)

        if self.estado_atual == OPCOES:
            self.configuracoes.on_mouse_press(x,y,button,key_modifiers)
        

    def on_mouse_release(self,x,y,button,key_modifiers):
        global config_atual,CONFIG_PADRAO

        if self.estado_atual == MENU:
            resultado = self.menu.on_mouse_release(x,y,button,key_modifiers)
            if resultado is not None:
                self.estado_atual = resultado

        if self.estado_atual == OPCOES:
            release = self.configuracoes.on_mouse_release(x,y,button,key_modifiers)
            if release is not None:
                if release == CONFIRMAR_CONFIGURACAO:
                    for chave in config_atual:
                        config_atual[chave] = self.configuracoes.config_atuais[chave]

                elif release == VOLTAR_PADRAO: 
                    for chave in self.configuracoes.config_atuais:
                        self.configuracoes.config_atuais[chave] = CONFIG_PADRAO[chave]
                else:
                    self.estado_atual = release
            
        if self.estado_atual == SELECAO_PERSONAGEM:
            resultado = self.selecao_personagem.on_mouse_release(x,y,button,key_modifiers)
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
                    self.player1.ganhou = None
                    self.player2.ganhou = None
                    self.estado_atual = PARTIDA
                    self.setup()
                else:
                    self.estado_atual = proxima_tela
        
        if self.estado_atual == AJUDA:
            proxima_tela = self.ajuda.on_mouse_release(x,y,button,key_modifiers)
            if proxima_tela is not None:
                if proxima_tela != PROXIMA_PAG_AJUDA and proxima_tela != VOLTAR_PAG_AJUDA:
                    self.ajuda.pagina_atual = 1
                    self.estado_atual = proxima_tela


def main():
    """ Main method """
    game = Jogo(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()