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
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.attacking = False
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.power = 3
        self.sprites = []
        for i in range(6):
            img = sprite.subsurface((i * 231, 0), (231, 190))
            img = pygame.transform.scale(img, (231 * int(2.5), 231 * int(2.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.life = 100

    def update(self):
        if self.index_lista > 5:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.sprites[int(self.index_lista)]


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

        if self.rect.bottom + dy > 600 - 50:
            self.vel_y = 0
            self.jump = False
            dy = 600 - 50 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.2, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health -= dano   
            print('hit')
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False


class Warrior(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.power = 2.5
        for i in range(10):
            img = sprite.subsurface((i * 135, 0), (135, 135))
            img = pygame.transform.scale(img, (135 * 4, 135*4))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

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
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.2, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health -= dano   
            print('hit')
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False


class Hunter(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.power = 2
        for i in range(8):
            img = sprite.subsurface((i * 150, 0), (150, 150))
            img = pygame.transform.scale(img, (150 * int(4.5), 150 * int(4.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # -120, 60

    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

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
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.3, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health -= dano   
            print('hit')
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False


class Archer(Personagem, pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.power = 2
        for i in range(10):
            img = sprite.subsurface((i * 100, 0), (100, 100))
            img = pygame.transform.scale(img, (100 * int(4.5), 100 * int(4.5)))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        if self.index_lista > 9:
            self.index_lista = 0
        self.index_lista += 0.50
        self.image = self.sprites[int(self.index_lista)]

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

        if self.rect.bottom + dy > 600 - 0:
            self.vel_y = 0
            self.jump = False
            dy = 600 - 0 - self.rect.bottom

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 0.5, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health -= dano   
            print('hit')
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False


class Knight(Personagem, pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.power = 2.3
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
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (100*4, 55*4))

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
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height) #coordenada x, y, largura e altura. será o alcance do ataque
        if attacking_rect.colliderect(target.rect):
            dano = self.power
            target.health -= dano   
            print('hit')
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        self.attacking = False