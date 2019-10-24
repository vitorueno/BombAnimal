import arcade
import random
from blocos.grama import Grama
from blocos.arvore_verde import Arvore_verde
from blocos.arvore_dourada import Arvore_dourada
from blocos.arvore_rosa import Arvore_rosa
from blocos.arvore_vermelha import Arvore_vermelha
from blocos.parede import Parede

class Mapa():
    def __init__(self,map_width,map_height,img_width,img_height):
        self.__map_height = map_height
        self.__map_width = map_width
        self.__background_list = arcade.SpriteList()
        self.__indestrutiveis = arcade.SpriteList()
        self.__destrutiveis = arcade.SpriteList()
        self.__parede = arcade.SpriteList()
        self.__img_width = img_width
        self.__img_height = img_height

        #width 25
        #height 18
        #a primeira lista é só pra não ficar uma faixa vazia perto da hud
        #observação: as listas estão invertidas em relação a forma como aparecem no jogo

        #P = parede
        #g = grama
        #a = arvore
        self.__map_matriz = [
            ["g","g","g","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","g","g","g"],
            ["g","p","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","p","g"],
            ["g","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","g"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["a","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","a"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["a","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","a"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["a","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","a"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["a","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","a"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["a","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","a"],
            ["a","a","a","a","p","a","a","a","p","a","a","a","a","a","a","a","p","a","a","a","p","a","a","a","a"],
            ["g","p","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","p","g"],
            ["g","p","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","a","p","p","g"],
            ["g","g","g","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","g","g","g"],
            ["g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g"]
        ]

        grama_mapa = Grama(map_width/2,map_height/2)
        self.__background_list.append(grama_mapa)

        y1 = self.__img_height / 2
        for matriz in self.__map_matriz:
            x1 = self.__img_width / 2

            for elemento in matriz:

                #cria grama sozinha
                #if elemento == "g":
                    #objeto = Grama(x1,y1)
                    #self.__background_list.append(objeto)
                #cria arvores com grama de fundo
                if elemento == "a":
                    tipo = random.randint(1,100)
                    #objeto2 = Grama(x1,y1)
                    #self.__background_list.append(objeto2)
                
                    if tipo > 0 and tipo <= 75:
                        objeto = Arvore_verde(x1,y1)
                        self.__destrutiveis.append(objeto)
                        self.__parede.append(objeto)

                    elif tipo > 75 and tipo <= 92:
                        objeto = Arvore_rosa(x1,y1)
                        self.__destrutiveis.append(objeto)
                        self.__parede.append(objeto)

                    if tipo > 92 and tipo <= 99:
                        objeto = Arvore_vermelha(x1,y1)
                        self.__destrutiveis.append(objeto)
                        self.__parede.append(objeto)

                    if tipo == 100:
                        objeto = Arvore_dourada(x1,y1)
                        self.__destrutiveis.append(objeto)
                        self.__parede.append(objeto)
                    

                #cria paredes com grama de fundo
                if elemento == "p":
                    objeto = Parede(x1,y1)
                    self.__indestrutiveis.append(objeto)
                    self.__parede.append(objeto)
                    #objeto2 = Grama(x1,y1)
                    #self.__background_list.append(objeto2)
                    
                    
                x1 += self.__img_width
            y1 += self.__img_height 

    def get_background(self):
        return self.__background_list
    
    def get_destrutiveis(self):
        return self.__destrutiveis
    
    def get_indestrutiveis(self):
        return self.__indestrutiveis

    def get_paredes(self):
        return self.__parede
    
    def get_bloco_da_coord(self,x,y):
        pos_x = ((x // 32) * 32) + 16 
        pos_y = ((y // 32) * 32) + 16
        paredes = self.get_paredes()
        for parede in paredes:
            if parede.center_x == pos_x and parede.center_y == pos_y:
                return parede