# Inimigos


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