import platform
import sys
import os
from app.jogo import Jogo
from app.var import *


def configurar_env():
    if not is_venv():
        if platform.system() == 'Windows':
            os.system(f'python -m venv {NOME_VENV} && "{NOME_VENV}/Scripts/activate" && pip install -r requirements.txt')
            main()
            
        elif platform.system() == 'Linux':
            os.system(f'python3 -m venv {NOME_VENV} && . {NOME_VENV}/bin/activate && pip install -r requirements.txt')
            main()        
            
        else:
            print('\n\nPlataforma não suportada.')
            print('Crie e configure o ambiente virtual manualmente.\n\n')
    else:
        main()
         
def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
    
def main():
    game = Jogo(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    configurar_env()