import pygame
import random


class Inimigo:                    # Inimigo pai
    def __init__(self):
        self.health = 100
        self.power = 10
        self.is_alive = True
        self.cooldown = 0
        self.attack_cooldown_duration = random.randint(100, 200)
        self.sprites = []

    def pode_atacar(self):
        pass
    def update_cooldown(self):
        pass

    def auto_attack(self, surface, target):
        pass

    def attack(self, surface, target):
        pass

    def alive(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return False

class DarkWarrior(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.power = 10
        self.is_alive = True
        self.cooldown = 0
        self.attack_cooldown_duration = random.randint(100, 200)
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
        self.update_cooldown()

    def pode_atacar(self):
        return self.cooldown <= 0

    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            # Atualiza o cooldown aleatório após o ataque
            self.attack_cooldown_duration = random.randint(100, 200)

    def auto_attack(self, surface, target):
        # Verifica se pode atacar com base no cooldown
        if self.pode_atacar():
            self.attack(surface, target)
            # Reinicia o cooldown
            self.cooldown = self.attack_cooldown_duration

    def attack(self, surface, target):
        # coordenada x, y, largura e altura. será o alcance do ataque
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, self.rect.width * -1, self.rect.height)
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano
                print('inimigo acertou')
            else:
                print('inimigo errou')

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def alive(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return False


class EvilWizard(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.power = 10
        self.is_alive = True
        self.cooldown = 0
        self.attack_cooldown_duration = random.randint(100, 200)
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
        self.update_cooldown()

    def pode_atacar(self):
        return self.cooldown <= 0

    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            # Atualiza o cooldown aleatório após o ataque
            self.attack_cooldown_duration = random.randint(100, 200)

    def auto_attack(self, surface, target):
        # Verifica se pode atacar com base no cooldown
        if self.pode_atacar():
            self.attack(surface, target)
            # Reinicia o cooldown
            self.cooldown = self.attack_cooldown_duration

    def attack(self, surface, target):
        # coordenada x, y, largura e altura. será o alcance do ataque
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, self.rect.width * -1, self.rect.height)
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano
                print('inimigo acertou')
            else:
                print('inimigo errou')

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def alive(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return False


class EvilWizardFire(Inimigo, pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.power = 10
        self.is_alive = True
        self.cooldown = 0
        self.attack_cooldown_duration = random.randint(100, 200)
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
        self.update_cooldown()

    def pode_atacar(self):
        return self.cooldown <= 0

    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            # Atualiza o cooldown aleatório após o ataque
            self.attack_cooldown_duration = random.randint(100, 200)

    def auto_attack(self, surface, target):
        # Verifica se pode atacar com base no cooldown
        if self.pode_atacar():
            self.attack(surface, target)
            # Reinicia o cooldown
            self.cooldown = self.attack_cooldown_duration

    def attack(self, surface, target):
        # coordenada x, y, largura e altura. será o alcance do ataque
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, self.rect.width * -1, self.rect.height)
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano
                print('inimigo acertou')
            else:
                print('inimigo errou')

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def alive(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return False


class Cultist(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.power = 10
        self.is_alive = True
        self.cooldown = 0
        self.attack_cooldown_duration = random.randint(100, 200)
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
        self.index_lista = 0
        self.image = self.sprites[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.topleft = (650, 170)

    def update(self):
        self.index_lista += 0.50
        if self.index_lista >= len(self.sprites):
            self.index_lista = 0
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.scale(self.image, (200*1.5, 200*1.5))
        self.image = pygame.transform.flip(self.image, True, False)
        self.update_cooldown()

    def pode_atacar(self):
        return self.cooldown <= 0

    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            # atualiza o cooldown aleatório após o ataque
            self.attack_cooldown_duration = random.randint(100, 200)

    def auto_attack(self, surface, target):
        # aerifica se pode atacar com base no cooldown
        if self.pode_atacar():
            self.attack(surface, target)
            # reinicia o cooldown
            self.cooldown = self.attack_cooldown_duration

    def attack(self, surface, target):
        # coordenada x, y, largura e altura. será o alcance do ataque
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, self.rect.width * -1, self.rect.height)
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano
                print('inimigo acertou')
            else:
                print('inimigo errou')

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def alive(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return False
