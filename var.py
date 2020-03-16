import arcade

#Constantes do jogo
SCREEN_WIDTH = HUD_WIDTH = 800
SCREEN_HEIGHT = 600
HUD_HEIGHT = 50
HUD_CENTER_X = SCREEN_WIDTH / 2
HUD_CENTER_Y = SCREEN_HEIGHT - HUD_HEIGHT//2
DURACAO_PARTIDA = 180.00
SCREEN_TITLE = "Bombanimal"
LIMITE_BOMBAS_MORTE_SUBITA = 5
MOVEMENT_SPEED = 5
NUM_DESTRUTIVOS = 10
EXPLOSION_TEXTURE_COUNT = 7


#Estados do Jogo
MENU = 0
SELECAO_PERSONAGEM = 1
PARTIDA = 2
PAUSE = 3 
POS_PARTIDA = 4
OPCOES = 5
SAIR = 6
AJUDA = 7
PROXIMA_PAG_AJUDA = 8
VOLTAR_PAG_AJUDA = 9
CONFIRMAR_CONFIGURACAO = 10
VOLTAR_PADRAO = 11


#Configuração de teclas
CONFIG_PADRAO = {
  "cima_p1": arcade.key.W,
  "direita_p1": arcade.key.D,
  "baixo_p1": arcade.key.S,
  "esquerda_p1": arcade.key.A,
  "bomba_p1": arcade.key.SPACE,
  "cima_p2":arcade.key.UP,
  "direita_p2":arcade.key.RIGHT,
  "baixo_p2":arcade.key.DOWN,
  "esquerda_p2":arcade.key.LEFT,
  "bomba_p2":arcade.key.ENTER
}

config_atual = {
  "cima_p1": arcade.key.W,
  "direita_p1": arcade.key.D,
  "baixo_p1": arcade.key.S,
  "esquerda_p1": arcade.key.A,
  "bomba_p1": arcade.key.SPACE,
  "cima_p2":arcade.key.UP,
  "direita_p2":arcade.key.RIGHT,
  "baixo_p2":arcade.key.DOWN,
  "esquerda_p2":arcade.key.LEFT,
  "bomba_p2":arcade.key.ENTER
}
