import pygame
from projeto import sprite_sheet_w

class Personagem:                # Personagem pai
    def __init__(self, nome):
        self._nome = nome
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ''
        self._xp = 0

    def ataque_basico(self, alvo):
        pass



class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 15
        self._defesa = 5
        self._vida = 80
        self._maxVida = 80
        self._descricao = (
            'Mago Elementarista -> Versado nos elementos, controlando fogo, água, terra e ar com seu cajado')
        self._mana = 20
        self._maxMana = self._mana
        self._xp = 0

    def ataque_basico(self, alvo):
        pass
    def recuperar_mana(self):
        pass


class Guerreiro(Personagem, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(9):
            img = sprite_sheet_w.subsurface((i * 38,0), (26, 38))
            self.sprites.append(img)
            
        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 250

        
    def update(self):
        self.index_lista = self.index_lista + 0.25
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.sprites[int(self.index_lista)]


    def ataque_basico(self, alvo):
        pass


class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 12
        self._defesa = 5
        self._vida = 70
        self._maxVida = 70
        self._descricao = (
            'Arqueiro Mestre -> Atirador habilidoso, especializado em acertar alvos à distância')
        self._xp = 0

    def ataque_basico(self, alvo):
        pass


class Clerigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 5
        self._defesa = 5
        self._vida = 70
        self._maxVida = 70
        self._descricao = (
            'Clérigo -> Utiliza poderes divinos para curar feridas e proteger contra os males')
        self._fe = 20
        self.maxFe = self._fe
        self._xp = 0

    def ataque_basico(self, alvo):
        pass
    def curar(self, alvo):
        pass
    def recuperar_fe(self):
        pass


class Anao(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 7
        self._defesa = 15
        self._vida = 100
        self._maxVida = 100
        self._descricao = (
            'Anão -> Um guerreiro resistente e habilidoso em combate corpo a corpo')
        self._xp = 0

    def ataque_basico(self, alvo):
        pass


class Elfo(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 10
        self._defesa = 7
        self._vida = 80
        self._maxVida = 80
        self._descricao = (
            'Elfo -> Especializado em técnicas marciais, usando agilidade e destreza em conjunto de armas')
        self._xp = 0

    def ataque_basico(self, alvo):
        pass











