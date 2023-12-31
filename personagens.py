import pygame
from abc import ABC, abstractmethod



class Personagem(ABC):                # Personagem pai
    def __init__(self, nome):
        pygame.sprite.Sprite.__init__(self)
        self.jump = False
        self.attacking = False
        self.health = 100
        self.power = 10
        self.sprites = []

        
    def update_cooldown(self):
        """
        atualiza o cooldown
        """
        if self.cooldown > 0:
            self.cooldown -= 1

    def pode_atacar(self):
        """
        verifica se o personagem pode realizar um ataque
        """
        return self.cooldown <= 0
    
    
    @abstractmethod
    def move(self, surface, target):
        pass


    @abstractmethod
    def update(self):
        pass

class Wizard(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        """
        inicializa um wizard com sprite, posição inicial x e y.

        - x (int): Posição inicial x.
        - y (int): Posição inicial y.
        """
        pygame.sprite.Sprite.__init__(self)
        self.attacking = False
        self.vel_y = 0
        self.jump = False
        self.health = 100
        self.power = 30
        self.cooldown = 0
        self.cooldown_duration = 10
        self.sprites = []
        for i in range(6):
            img = sprite.subsurface((i * 231, 0), (231, 190))
            img = pygame.transform.scale(img, (231 * int(2.5), 231 * int(2.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def __str__(self):
        """
        retorna uma representação em string de wizard
        """
        return "Wizard"

    def update(self):
        """
        atualiza a velocidade de animação da sprite e o cooldown do personagem
        """
        if self.index_lista > 5:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.sprites[int(self.index_lista)]
        self.update_cooldown()
    
    def move(self, surface, target):
        """
        Move o feiticeiro na tela em resposta às teclas pressionadas.
:
        - surface (pygame.Surface): tela do jogo.
        - target (Personagem): alvo do personagem
        """
        SPEED = 10
        GRAVITY = 2
        dx = 0  # (direction x) nada muda, posição do jogador está parada
        dy = 0

        # press teclas
        key = pygame.key.get_pressed()
        
        # só realiza ações se não estiver atacando
        if self.attacking == False:
            # movimento
            if key[pygame.K_a]:
                dx = - SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # pulo
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # atacar
            if key[pygame.K_m]:
                self.attack_type = 1
                self.attack(surface, target)
                # se tiver mais de um ataque:
                # if key[pygame.K_m]:
                #     self.attack_type =1
                # if key[pygame.K_n]:
                #     self.attack_type =2

        # aplicar gravidade
        self.vel_y += GRAVITY
        dy += self.vel_y

        # permanacer na tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > 950:
            dx = 950 - self.rect.right

        if self.rect.bottom + dy > 600 - 50:
            self.vel_y = 0
            self.jump = False
            dy = 600 - 50 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        """
        realiza um ataque no alvo especificado.

        - surface (pygame.Surface): tela do jogo.
        - target (Personagem): alvo do ataque.
        """
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.3, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano   
                print('hit')
                self.cooldown = self.cooldown_duration
            else: 
                print('não acertou')
                self.cooldown = self.cooldown_duration
            
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)


class Warrior(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.health = 100
        self.power = 2.5
        self.cooldown = 0
        self.cooldown_duration = 10
        for i in range(10):
            img = sprite.subsurface((i * 135, 0), (135, 135))
            img = pygame.transform.scale(img, (135 * 4, 135*4))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def __str__(self):
        return "Warrior"


    def update(self):
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]
        self.update_cooldown()

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0  # (direction x) nada muda, posição do jogador está parada
        dy = 0

        # press teclas
        key = pygame.key.get_pressed()
        
        # só realiza ações se não estiver atacando
        if self.attacking == False:
            # movimento
            if key[pygame.K_a]:
                dx = - SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # pulo
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # atacar
            if key[pygame.K_m]:
                self.attack_type = 1
                self.attack(surface, target)
                # se tiver mais de um ataque:
                # if key[pygame.K_m]:
                #     self.attack_type =1
                # if key[pygame.K_n]:
                #     self.attack_type =2
      
        # aplicar gravidade
        self.vel_y += GRAVITY
        dy += self.vel_y

        # permanacer na tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > 950:
            dx = 950 - self.rect.right

        if self.rect.bottom + dy > 600 - -50:
            self.vel_y = 0
            self.jump = False
            dy = 600 - -50 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.2, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano   
                print('hit')
                self.cooldown = self.cooldown_duration
            else: 
                print('não acertou')
                self.cooldown = self.cooldown_duration

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)


class Hunter(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.health = 100
        self.power = 2
        self.cooldown = 0
        self.cooldown_duration = 10
        for i in range(8):
            img = sprite.subsurface((i * 150, 0), (150, 150))
            img = pygame.transform.scale(img, (150 * int(4.5), 150 * int(4.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # -120, 60

    def __str__(self):
        return "Hunter"


    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]
        self.update_cooldown()

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0  # (direction x) nada muda, posição do jogador está parada
        dy = 0

        # press teclas
        key = pygame.key.get_pressed()
        
        # só realiza ações se não estiver atacando
        if self.attacking == False:
            # movimento
            if key[pygame.K_a]:
                dx = - SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # pulo
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # atacar
            if key[pygame.K_m]:
                self.attack_type = 1
                self.attack(surface, target)
                # se tiver mais de um ataque:
                # if key[pygame.K_m]:
                #     self.attack_type =1
                # if key[pygame.K_n]:
                #     self.attack_type =2
   
        # aplicar gravidade
        self.vel_y += GRAVITY
        dy += self.vel_y

        # permanacer na tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > 950:
            dx = 950 - self.rect.right

        if self.rect.bottom + dy > 600 - -50:
            self.vel_y = 0
            self.jump = False
            dy = 600 - -50 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.2, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano   
                print('hit')
                self.cooldown = self.cooldown_duration
            else:
                print('não acertou')
                self.cooldown = self.cooldown_duration

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)



class Knight(Personagem, pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.health = 100
        self.power = 2.3
        self.cooldown = 0
        self.cooldown_duration = 10
        self.sprites = []
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_0.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_1.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_2.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_3.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_4.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_5.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_6.png"))
        self.sprites.append(pygame.image.load(
            "sprites/knight/HeroKnight_Idle_7.png"))
        self.index_lista = 0
        self.image = self.sprites[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def __str__(self):
        return "Knight"


    def update(self):
        self.index_lista = self.index_lista + 0.5
        if self.index_lista >= len(self.sprites):
            self.index_lista = 0
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.scale(self.image, (100*4, 55*4))
        self.update_cooldown()

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0  # (direction x) nada muda, posição do jogador está parada
        dy = 0

        # press teclas
        key = pygame.key.get_pressed()
        
        # só realiza ações se não estiver atacando
        if self.attacking == False:
            # movimento
            if key[pygame.K_a]:
                dx = - SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # pulo
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # atacar
            if key[pygame.K_m]:
                self.attack_type = 1
                self.attack(surface, target)
                # se tiver mais de um ataque:
                # if key[pygame.K_m]:
                #     self.attack_type =1
                # if key[pygame.K_n]:
                #     self.attack_type =2

        # aplicar gravidade
        self.vel_y += GRAVITY
        dy += self.vel_y

        # permanacer na tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > 950:
            dx = 950 - self.rect.right

        if self.rect.bottom + dy > 600 - 320:
            self.vel_y = 0
            self.jump = False
            dy = 600 - 320 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if self.pode_atacar():
            if attacking_rect.colliderect(target.rect):
                dano = self.power
                target.health -= dano   
                print('hit')
                self.cooldown = self.cooldown_duration
            else: 
                print('não acertou')
                self.cooldown = self.cooldown_duration

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
