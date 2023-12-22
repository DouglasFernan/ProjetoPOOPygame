import pygame


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


class Wizard(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(6):
            img = sprite.subsurface((i * 231, 0), (231, 190))
            img = pygame.transform.scale(img, (231 * int(2.5), 231* int(2.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (-40, 100)

    def update(self):
        if self.index_lista > 5:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

    def ataque_basico(self, alvo):
        pass


# class Guerreiro(Personagem, pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.sprites = []
#         self.sprites.append(pygame.image.load("sprites/warrior/sprite_0.png"))
#         self.sprites.append(pygame.image.load("sprites/warrior/sprite_1.png"))
#         self.sprites.append(pygame.image.load("sprites/warrior/sprite_2.png"))
#         self.atual = 0
#         self.image = self.sprites[self.atual]
#         self.image = pygame.transform.scale(self.image, (32*6, 32*6))

#         self.rect = self.image.get_rect()
#         self.rect.topleft = 100, 250

#     def update(self):
#         self.atual = self.atual + 0.5
#         if self.atual >= len(self.sprites):
#             self.atual = 0
#         self.image = self.sprites[int(self.atual)]
#         self.image = pygame.transform.scale(self.image, (32*6, 32*6))

#     def ataque_basico(self, alvo):
#         pass


class Warrior(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(10):
            img = sprite.subsurface((i * 135, 0), (135, 135))
            img = pygame.transform.scale(img, (135 * 4, 135*4))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (450, 100)

    def update(self):
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

    def ataque_basico(self, alvo):
        pass


class Hunter(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(8):
            img = sprite.subsurface((i * 150, 0), (150, 150))
            img = pygame.transform.scale(img, (150 * int(4.5), 150 * int(4.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 60) #-120, 60

    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

    def ataque_basico(self, alvo):
        pass


class Archer(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(10):
            img = sprite.subsurface((i * 100, 0), (100, 100))
            img = pygame.transform.scale(img, (100 * int(4.5), 100* int(4.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = ( 100, 100) #-60

    def update(self):
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

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
