# Inimigos
import pygame


class Inimigo:                    # Inimigo pai
    def __init__(self):
        self._nome = ''
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ''

    def ataque_basico(self, alvo):
        pass


class DarkWarrior(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.sprites = []
        for i in range(8):
            img = sprite.subsurface((i * 100, 0), (100, 100))
            img = pygame.transform.scale(img, (100 * 4.5, 100*4.5))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (520, 30)

    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.flip(self.image, True, False)

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health = - dano     
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False


class EvilWizard(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.sprites = []
        for i in range(8):
            img = sprite.subsurface((i * 250, 0), (250, 250))
            img = pygame.transform.scale(img, (250 * 4, 250*4))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, -220)

    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.flip(self.image, True, False)

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health = - dano     
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False

class EvilWizardFire(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.sprites = []
        for i in range(8):
            img = sprite.subsurface((i * 150, 0), (150, 150))
            img = pygame.transform.scale(img, (150 * 5, 150*5))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (450, -50)

    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.flip(self.image, True, False)

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health = - dano     
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False

class Cultist(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.sprites = []
        self.sprites.append(pygame.image.load(
            "sprites/cultist/cultist_priest_idle_1.png"))
        self.sprites.append(pygame.image.load(
            "sprites/cultist/cultist_priest_idle_2.png"))
        self.sprites.append(pygame.image.load(
            "sprites/cultist/cultist_priest_idle_3.png"))
        self.sprites.append(pygame.image.load(
            "sprites/cultist/cultist_priest_idle_4.png"))
        self.sprites.append(pygame.image.load(
            "sprites/cultist/cultist_priest_idle_5.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = (650, 170)

    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (200*1.5, 200*1.5))
        self.image = pygame.transform.flip(self.image, True, False)

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health = - dano     
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False
