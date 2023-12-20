
class Personagem:                # Personagem pai
    def __init__(self, nome):
        self._nome = nome
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ''
        self._xp = 0
        
# class Personagem:                
#     def __init__(self, nome, x, y):
#         self.rect = pygame.Rect((x, y, 120, 180))
#         self._nome = nome
#         self._ataque = 1
#         self._defesa = 1
#         self._vida = 1
#         self._maxVida = self._vida
#         self._descricao = ''
#         self._xp = 0
        

    def ataque_basico(self, alvo):
        pass


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


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._ataque = 10
        self._defesa = 10
        self._vida = 100
        self._maxVida = 100
        self._descricao = (
            'Guerreiro -> Combatente habilidoso e destemido, armado com uma espada afiada e vestindo uma armadura robusta')
        self._xp = 0

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


# Inimigos


class Orc(Inimigo):                               # BOSS
    def __init__(self):
        self._nome='Orc'
        self._ataque = 16
        self._defesa = 8
        self._vida = 100
        self._maxVida = 100
        self._descricao = ('O chefe da tribo dos orcs')
        self.boss = True
    
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass
    def habilidade_unica(self):
        pass


class Invasor_orc(Inimigo):                           # subclasse de orc, um orc menor
    def __init__(self):
        self._nome='Invasor Orc'
        self._ataque = 8
        self._defesa = 8
        self._vida = 80
        self._maxVida = 80
        self._descricao = ('Orcs de grande estatura, guerreiros do chefe Orc')
        self.boss = False
        
    def get_nome(self):
        return self._nome
    
    def ataque_basico(self, alvo):
        pass


class Goblin_das_sombras(Inimigo):                 # BOSS
    def __init__(self):
        self._nome = 'Goblin das Sombras'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = (
            'Chefe dos goblins, um atacante furtivo e das trevas')
        self.boss = True

    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass
    def habilidade_unica(self):
        pass


class Goblin_furtivo(Inimigo):                 # subclasse de goblin, um goblin menor
    def __init__(self):
        self._nome = 'Goblin Thief'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ('Criaturas astutas e que vivem nas sombras')
        self.boss = False
        
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass


class Troll_de_pedra(Inimigo):                      # BOSS
    def __init__(self):
        self._nome = 'Troll de Pedra'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ('Troll gigante e poreroso feito de pedra')
        self.boss = True
        
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass
    def habilidade_unica(self):
        pass


class Guardiao_da_montanha(Inimigo):         # subclasse de troll
    def __init__(self):
        self._nome = 'Guardião da Montanha'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = (
            ' Trolls pequenos e resistentes que se camuflam entre as rochas')
        self.boss = False
        
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass


class Dragao(Inimigo):                      # BOSS
    def __init__(self):
        self._nome = 'Dragão'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = ('A besta de chamas ardentes')
        self.boss = True
        
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass
    def habilidade_unica(self):
        pass


class Guardiao_draconico(Inimigo):                      # subclasse de Dragao
    def __init__(self):
        self._nome = 'Guardião Dracônico'
        self._ataque = 1
        self._defesa = 1
        self._vida = 1
        self._maxVida = self._vida
        self._descricao = (
            'Defensores ferozes dedicados a proteger seu mestre')
        self.boss = False
        
    def get_nome(self):
        return self._nome

    def ataque_basico(self, alvo):
        pass


# boss






