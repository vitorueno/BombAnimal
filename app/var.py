import arcade

NOME_VENV = 'env'

#Constantes do jogo
SCREEN_WIDTH = HUD_WIDTH = 800
SCREEN_HEIGHT = 600
HUD_HEIGHT = 50
HUD_CENTER_X = CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2 
HUD_CENTER_Y  = SCREEN_HEIGHT - HUD_HEIGHT//2
MAP_HEIGHT = SCREEN_HEIGHT- HUD_HEIGHT
DURACAO_PARTIDA = 180.00
SCREEN_TITLE = "Bombanimal"
LIMITE_BOMBAS_MORTE_SUBITA = 5
MOVEMENT_SPEED = 5
NUM_DESTRUTIVOS = 10
EXPLOSION_TEXTURE_COUNT = 7
BLOCK_SIZE = 32

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

dict_modifiers = {
  1: 'MOD_SHIFT',
  2: 'MOD_CTRL', 
  4: 'MOD_ALT', 
  8: 'MOD_CAPSLOCK',
  16: 'MOD_NUMLOCK', 
  32: 'MOD_WINDOWS', 
  32: 'MOD_COMMAND', 
  128: 'MOD_OPTION', 
  256: 'MOD_SCROLLLOCK', 
  2: 'MOD_ACCEL' 
}

dict_teclas = {
  # Keys
  65288: 'BACKSPACE',
  65289: 'TAB', 
  65290: 'LINEFEED',
  65291: 'CLEAR', 
  65293: 'RETURN', 
  65293: 'ENTER',
  65299: 'PAUSE', 
  65300: 'SCROLLLOCK', 
  65301: 'SYSREQ', 
  65307: 'ESCAPE' ,
  65360: 'HOME' ,
  65361: 'LEFT' ,
  65362: 'UP' ,
  65363: 'RIGHT', 
  65364: 'DOWN' ,
  65365: 'PAGEUP', 
  65366: 'PAGEDOWN', 
  65367: 'END' ,
  65368: 'BEGIN', 
  65535: 'DELETE', 
  65376: 'SELECT' ,
  65377: 'PRINT' ,
  65378: 'EXECUTE', 
  65379: 'INSERT' ,
  65381: 'UNDO' ,
  65382: 'REDO' ,
  65383: 'MENU' ,
  65384: 'FIND',
  65385: 'CANCEL', 
  65386: 'HELP' ,
  65387: 'BREAK' ,
  65406: 'MODESWITCH', 
  65406: 'SCRIPTSWITCH', 
  65362: 'MOTION_UP' ,
  65363: 'MOTION_RIGHT', 
  65364: 'MOTION_DOWN' ,
  65361: 'MOTION_LEFT' ,
  1: 'MOTION_NEXT_WORD' ,
  2: 'MOTION_PREVIOUS_WORD' ,
  3: 'MOTION_BEGINNING_OF_LINE' ,
  4: 'MOTION_END_OF_LINE' ,
  65366: 'MOTION_NEXT_PAGE' ,
  65365: 'MOTION_PREVIOUS_PAGE', 
  5: 'MOTION_BEGINNING_OF_FILE',
  6: 'MOTION_END_OF_FILE' ,
  65288: 'MOTION_BACKSPACE', 
  65535: 'MOTION_DELETE' ,
  65407: 'NUMLOCK' ,
  65408: 'NUM_SPACE', 
  65417: 'NUM_TAB' ,
  65421: 'NUM_ENTER', 
  65425: 'NUM_F1' ,
  65426: 'NUM_F2' ,
  65427: 'NUM_F3' ,
  65428: 'NUM_F4' ,
  65429: 'NUM_HOME', 
  65430: 'NUM_LEFT' ,
  65431: 'NUM_UP' ,
  65432: 'NUM_RIGHT', 
  65433: 'NUM_DOWN' ,
  65434: 'NUM_PRIOR' ,
  65434: 'NUM_PAGE_UP', 
  65435: 'NUM_NEXT' ,
  65435: 'NUM_PAGE_DOWN' ,
  65436: 'NUM_END' ,
  65437: 'NUM_BEGIN', 
  65438: 'NUM_INSERT', 
  65439: 'NUM_DELETE' ,
  65469: 'NUM_EQUAL' ,
  65450: 'NUM_MULTIPLY', 
  65451: 'NUM_ADD' ,
  65452: 'NUM_SEPARATOR',
  65453: 'NUM_SUBTRACT' ,
  65454: 'NUM_DECIMAL' ,
  65455: 'NUM_DIVIDE' ,

  # Numbers on the numberpad
  65456: 'NUM_0' ,
  65457: 'NUM_1' ,
  65458: 'NUM_2' ,
  65459: 'NUM_3' ,
  65460: 'NUM_4' ,
  65461: 'NUM_5' ,
  65462: 'NUM_6' ,
  65463: 'NUM_7' ,
  65464: 'NUM_8' ,
  65465: 'NUM_9' ,

  65470: 'F1' ,
  65471: 'F2' ,
  65472: 'F3' ,
  65473: 'F4' ,
  65474: 'F5' ,
  65475: 'F6' ,
  65476: 'F7' ,
  65477: 'F8' ,
  65478: 'F9' ,
  65479: 'F10' ,
  65480: 'F11' ,
  65481: 'F12' ,
  65482: 'F13' ,
  65483: 'F14' ,
  65484: 'F15' ,
  65485: 'F16' ,
  65505: 'LSHIFT', 
  65506: 'RSHIFT' ,
  65507: 'LCTRL' ,
  65508: 'RCTRL' ,
  65509: 'CAPSLOCK' ,
  65511: 'LMETA' ,
  65512: 'RMETA' ,
  65513: 'LALT' ,
  65514: 'RALT' ,
  65515: 'LWINDOWS', 
  65516: 'RWINDOWS' ,
  65517: 'LCOMMAND' ,
  65518: 'RCOMMAND' ,
  65488: 'LOPTION' ,
  65489: 'ROPTION' ,
  32: 'SPACE' ,
  33: 'EXCLAMATION' ,
  34: 'DOUBLEQUOTE' ,
  35: 'HASH',
  35: 'POUND' ,
  36: 'DOLLAR' ,
  37: 'PERCENT' ,
  38: 'AMPERSAND', 
  39: 'APOSTROPHE', 
  40: 'PARENLEFT' ,
  41: 'PARENRIGHT' ,
  42: 'ASTERISK' ,
  43: 'PLUS' ,
  44: 'COMMA' ,
  45: 'MINUS' ,
  46: 'PERIOD' ,
  47: 'SLASH' ,

  # Numbers on the main keyboard
  48: 'KEY_0' ,
  49: 'KEY_1' ,
  50: 'KEY_2' ,
  51: 'KEY_3' ,
  52: 'KEY_4' ,
  53: 'KEY_5' ,
  54: 'KEY_6' ,
  55: 'KEY_7' ,
  56: 'KEY_8' ,
  57: 'KEY_9' ,
  58: 'COLON' ,
  59: 'SEMICOLON',
  60: 'LESS' ,
  61: 'EQUAL' ,
  62: 'GREATER', 
  63: 'QUESTION', 
  64: 'AT' ,
  91: 'BRACKETLEFT' ,
  92: 'BACKSLASH' ,
  93: 'BRACKETRIGHT' ,
  94: 'ASCIICIRCUM' ,
  95: 'UNDERSCORE' ,
  96: 'GRAVE' ,
  96: 'QUOTELEFT',
  97: 'A' ,
  98: 'B' ,
  99: 'C' ,
  100: 'D' ,
  101: 'E' ,
  102: 'F' ,
  103: 'G' ,
  104: 'H' ,
  105: 'I' ,
  106: 'J' ,
  107: 'K' ,
  108: 'L' ,
  109: 'M' ,
  110: 'N' ,
  111: 'O' ,
  112: 'P' ,
  113: 'Q' ,
  114: 'R' ,
  115: 'S' ,
  116: 'T' ,
  117: 'U' ,
  118: 'V' ,
  119: 'W' ,
  120: 'X' ,
  121: 'Y' ,
  122: 'Z' ,
  123: 'BRACELEFT' ,
  124: 'BAR' ,
  125: 'BRACERIGHT', 
  126: 'ASCIITILDE' ,
}