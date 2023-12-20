from random import choice
from classes import *





class GameEngine:
    def __init__(self, player, andarAtual):
        self.player = player
        self.atual_floor = andarAtual
        self.dungeon = Dungeon()

    def run(self):
        pass
            # lógica para subir os floor da dungeon

            # enquanto tiver monstros e enquanto player_continua_vivo:
            # self.battle(player, monster)

            # se player continua vivo irá enfrentar o boss
                #battle(player, monstro)


    def battle(self, player, monster):
        pass


class Dungeon:
    def __init__(self):
        self.floors = []

    def gerar_monsters(self):
        pass

    def get_boss(self):
        pass

    def get_monster(self):
        pass


class Floor:
    def __init__(self, numAndar):
        self.numAndar = numAndar
        self.monstros = {}

    def add_monstros(self, nome):
        if nome == 'orc':
            monstro = Orc()
            self.monstros.update({nome: monstro})
        elif nome == 'dragao':
            monstro = Dragao()
            self.monstros.update({nome: monstro})
        elif nome == 'troll':
            monstro = Troll_de_pedra()
            self.monstros.update({nome: monstro})
        elif nome == 'goblin':
            monstro = Goblin_das_sombras()
            self.monstros.update({nome: monstro})
        elif nome == 'invasor_orc':
            monstro = Invasor_orc()
            self.monstros.update({nome: monstro})
        elif nome == 'guardiao_draconico':
            monstro = Guardiao_draconico()
            self.monstros.update({nome: monstro})
        elif nome == 'guardiao_montanha':
            monstro = Guardiao_da_montanha()
            self.monstros.update({nome: monstro})
        elif nome == 'goblin_furtivo':
            monstro = Goblin_furtivo()
            self.monstros.update({nome: monstro})
        else:
            return f"não existe nenhum monstro com esse nome: {nome} "
            
    def get_todos_os_monstros(self):
        return self.monstros

floor1 = Floor(1)
floor1.add_monstros('dragao')
floor1.add_monstros('orc')
print(floor1.monstros)


# módulo pickle













