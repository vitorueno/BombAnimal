import arcade
from ajuda import Ajuda
from configuracoes import Configuracoes


"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

config = {"cima_p1": arcade.key.W,
        "direita_p1": arcade.key.D,
        "baixo_p1": arcade.key.S,
        "esquerda_p1": arcade.key.A,
        "bomba_p1": arcade.key.SPACE,
        "cima_p2":arcade.key.UP,
        "direita_p2":arcade.key.RIGHT,
        "baixo_p2":arcade.key.DOWN,
        "esquerda_p2":arcade.key.LEFT,
        "bomba_p2":arcade.key.ENTER}

config_padrao = {
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

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.ajuda = None
        self.configuracoes = None

    def setup(self):
        self.ajuda = Ajuda(SCREEN_WIDTH,SCREEN_HEIGHT)
        
        self.configuracoes = Configuracoes(SCREEN_WIDTH,SCREEN_HEIGHT,config)

    def on_draw(self):
        arcade.start_render()
        #self.ajuda.draw()
        self.configuracoes.draw()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        self.configuracoes.on_key_release(key,key_modifiers)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        #self.ajuda.on_mouse_press(x,y,button,key_modifiers)
        self.configuracoes.on_mouse_press(x,y,button,key_modifiers)

    def on_mouse_release(self, x, y, button, key_modifiers):
        global config
        #self.ajuda.on_mouse_release(x,y,button,key_modifiers)
        release = self.configuracoes.on_mouse_release(x,y,button,key_modifiers)
        if release is not None:
            print(release)
            if release == CONFIRMAR_CONFIGURACAO:
                for chave in config:
                    config[chave] = self.configuracoes.config_atuais[chave]
                #config = self.configuracoes.config_atuais
                print(config)
            elif release == VOLTAR_PADRAO: 
                
                for chave in self.configuracoes.config_atuais:
                    self.configuracoes.config_atuais[chave] = config_padrao[chave]
                '''
                self.configuracoes.config_atuais["cima_p1"] = config_padrao["cima_p1"]
                self.configuracoes.config_atuais["direita_p1"] = config_padrao["direita_p1"]
                self.configuracoes.config_atuais["baixo_p1"] = config_padrao["baixo_p1"]
                self.configuracoes.config_atuais["esquerda_p1"] = config_padrao["esquerda_p1"]
                self.configuracoes.config_atuais["bomba_p1"] = config_padrao["bomba_p1"] 

                self.configuracoes.config_atuais["cima_p2"] = config_padrao["cima_p2"]
                self.configuracoes.config_atuais["direita_p2"] = config_padrao["direita_p2"]
                self.configuracoes.config_atuais["baixo_p2"] = config_padrao["baixo_p2"]
                self.configuracoes.config_atuais["esquerda_p2"] = config_padrao["esquerda_p2"]
                self.configuracoes.config_atuais["bomba_p2"] = config_padrao["bomba_p2"] 
                '''
                #config = config_padrao
                print( config)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
