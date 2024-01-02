import sys
import pygame
import os
from pygame.locals import *
from projeto import *
from personagens import *
from inimigos import *
import csv

diretorio_principal = os.path.dirname(__file__)
diretorio_sprites = os.path.join(diretorio_principal, 'sprites')

pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Journey')
largura = 1100
altura = 600
tela = pygame.display.set_mode((largura, altura))
musica_de_fundo = pygame.mixer.music.load("audio/music/cloud-of-sorrow.wav")
pygame.mixer.music.play(-1)

# personagens
sprite_warrior = pygame.image.load(os.path.join(
    diretorio_sprites, 'warrior/warrior.png')).convert_alpha()
sprite_hunter = pygame.image.load(os.path.join(
    diretorio_sprites, 'hunter/hunter.png')).convert_alpha()
sprite_wizard = pygame.image.load(os.path.join(
    diretorio_sprites, 'wizard/wizard.png')).convert_alpha()


# inimigos
sprite_darkwarrior = pygame.image.load(os.path.join(
    diretorio_sprites, 'darkwarrior/darkwarrior.png')).convert_alpha()
sprite_evilwizard = pygame.image.load(os.path.join(
    diretorio_sprites, 'evilwizard/evilwizard.png')).convert_alpha()
sprite_evilwizardfire = pygame.image.load(os.path.join(
    diretorio_sprites, 'evilwizardfire/evilwizardfire.png')).convert_alpha()


todas_as_sprites = pygame.sprite.Group()

# instâncias

hunter = Hunter(sprite_hunter, -120, 60)
warrior = Warrior(sprite_warrior, -100, 100)
wizard = Wizard(sprite_wizard, -40, 100)
knight = Knight(-20, 250)

# backgrounds
menu = pygame.image.load("images/fundo/menu.png").convert()
menu = pygame.transform.scale(menu, (largura, altura))

battle1 = pygame.image.load("images/fundo/Battleground1.0.png").convert()
battle1 = pygame.transform.scale(battle1, (largura, altura))

battle2 = pygame.image.load("images/fundo/Battleground2.0.png").convert()
battle2 = pygame.transform.scale(battle2, (largura, altura))

battle3 = pygame.image.load("images/fundo/Battleground3.0.png").convert()
battle3 = pygame.transform.scale(battle3, (largura, altura))

battle4 = pygame.image.load("images/fundo/Battleground4.0.png").convert()
battle4 = pygame.transform.scale(battle4, (largura, altura))

escolha = pygame.image.load("images/fundo/escolha.png").convert()
escolha = pygame.transform.scale(escolha, (largura, altura))


# cores

black = (0, 0, 0)  # cor preta
white = (255, 255, 255)  # cor branca
yellow = (255, 255, 0)  # cor amarela
red = (255, 0, 0)  # cor vermelha

botao_warrior = pygame.Rect(largura // 2 - 100, altura // 2 - 25, 200, 50)
botao_hunter = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)
botao_wizard = pygame.Rect(largura // 2 - 100, altura // 2 + 125, 200, 50)
botao_knight = pygame.Rect(largura // 2 - 100, altura // 2 + 200, 200, 50)

fonte = pygame.font.Font("fonts/BerkshireSwash-Regular.ttf", 30)


class GameEngine:
    def __init__(self):
        self.dungeon = Dungeon()
        self.current_cena = "menu"

    def run(self):
        """
        basicamente, é o loop principal, onde troca de uma cena para a outra
        dependendo das escolhas do usuario
        """
        while True:
            if self.current_cena == "menu":
                self.current_cena = self.cena_menu()
            elif self.current_cena == "jogar":
                self.current_cena = self.cena_jogar()
            elif self.current_cena == "escolher_personagem":
                self.current_cena = self.cena_escolher_personagem()

    def cena_menu(self):
        """
        função onde é desenhada na tela a cena do menu principal
        contando com play e exit
        """
        play_botao = pygame.Rect(largura // 2 - 100, altura // 2 - 25, 200, 50)
        play_texto = "Play"

        continue_botao = pygame.Rect(
            largura // 2 - 100, altura // 2 + 50, 200, 50)
        continue_texto = "Continue Game"

        exit_botao = pygame.Rect(
            largura // 2 - 100, altura // 2 + 125, 200, 50)
        exit_texto = "Exit"

        if os.path.isfile('progresso.csv'):
            pygame.draw.rect(tela, black, continue_botao)
            continue_texto_renderizado = fonte.render(
                continue_texto, True, white)
            tela.blit(continue_texto_renderizado, (continue_botao.x + (continue_botao.width - continue_texto_renderizado.get_width()

                                                                       ) // 2, continue_botao.y + (continue_botao.height - continue_texto_renderizado.get_height()) // 2))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_botao.collidepoint(event.pos):
                        print("clicou em play")
                        return "escolher_personagem"
                    elif continue_botao.collidepoint(event.pos):
                        print("clicou em continuar")
                        self.carregar_progresso_csv()
                        return "jogar"
                    elif exit_botao.collidepoint(event.pos):
                        print("clicou em exit")
                        pygame.quit()
                        sys.exit()

            tela.blit(escolha, (0, 0))

            pygame.draw.rect(tela, black, play_botao)
            pygame.draw.rect(tela, black, continue_botao)
            pygame.draw.rect(tela, black, exit_botao)

            play_texto_renderizado = fonte.render(play_texto, True, white)
            continue_texto_renderizado = fonte.render(
                continue_texto, True, white)
            exit_texto_renderizado = fonte.render(exit_texto, True, white)

            tela.blit(play_texto_renderizado, (play_botao.x + (play_botao.width - play_texto_renderizado.get_width()
                                                               ) // 2, play_botao.y + (play_botao.height - play_texto_renderizado.get_height()) // 2))
            tela.blit(continue_texto_renderizado, (continue_botao.x + (continue_botao.width - continue_texto_renderizado.get_width()
                                                                       ) // 2, continue_botao.y + (continue_botao.height - continue_texto_renderizado.get_height()) // 2))
            tela.blit(exit_texto_renderizado, (exit_botao.x + (exit_botao.width - exit_texto_renderizado.get_width()
                                                               ) // 2, exit_botao.y + (exit_botao.height - exit_texto_renderizado.get_height()) // 2))

            pygame.display.flip()

    def cena_escolher_personagem(self):
        """
        cena que é desenhada na tela logo após o usuário apertar em "play"
        aqui, será possivel escolher entre os personagens que o usuário
        deseja utilizar no game
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_warrior.collidepoint(event.pos):
                        todas_as_sprites.add(warrior)
                        return ("jogar")
                    elif botao_hunter.collidepoint(event.pos):
                        todas_as_sprites.add(hunter)
                        return ("jogar")
                    elif botao_wizard.collidepoint(event.pos):
                        todas_as_sprites.add(wizard)
                        return ("jogar")
                    elif botao_knight.collidepoint(event.pos):
                        todas_as_sprites.add(knight)
                        return ("jogar")

            tela.blit(escolha, (0, 0))

            texto_escolha = fonte.render(
                "Choose your character", True, black)
            tela.blit(texto_escolha,
                      ((largura - texto_escolha.get_width()) // 2, 200))

            pygame.draw.rect(tela, black, botao_warrior)
            pygame.draw.rect(tela, black, botao_hunter)
            pygame.draw.rect(tela, black, botao_wizard)
            pygame.draw.rect(tela, black, botao_knight)

            texto_warrior = fonte.render("Warrior", True, white)
            texto_hunter = fonte.render("Hunter", True, white)
            texto_wizard = fonte.render("Wizard", True, white)
            texto_knight = fonte.render("Knight", True, white)

            tela.blit(texto_warrior, (botao_warrior.x + (botao_warrior.width - texto_warrior.get_width()) // 2,
                                      botao_warrior.y + (botao_warrior.height - texto_warrior.get_height()) // 2))
            tela.blit(texto_hunter, (botao_hunter.x + (botao_hunter.width - texto_hunter.get_width()) // 2,
                                     botao_hunter.y + (botao_hunter.height - texto_hunter.get_height()) // 2))
            tela.blit(texto_wizard, (botao_wizard.x + (botao_wizard.width - texto_wizard.get_width()) // 2,
                                     botao_wizard.y + (botao_wizard.height - texto_wizard.get_height()) // 2))
            tela.blit(texto_knight, (botao_knight.x + (botao_knight.width - texto_knight.get_width()) // 2,
                                     botao_knight.y + (botao_knight.height - texto_knight.get_height()) // 2))

            pygame.display.flip()

            pygame.time.Clock().tick(60)

    def cena_jogar(self):
        """
        nessa cena, é quando o usuário já escolheu seu personagem e ele é desenhado
        na tela, começando o game no primeiro Floor, com seu inimigo específico
        """
        battle_music = pygame.mixer.music.load(
            "audio/music/battle-of-the-dragons.wav")
        pygame.mixer.music.play(-1)

        relogio = pygame.time.Clock()
        FPS = 30

        battle_music = pygame.mixer.music.load(
            "audio/music/battle-of-the-dragons.wav")
        pygame.mixer.music.play(-1)

        # sprite_inimigos com o inimigo do primeiro andar
        sprite_inimigos = pygame.sprite.Group()
        self.dungeon.get_current_floor().create_enemy(sprite_inimigos)

        while True:
            relogio.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            tela.blit(self.dungeon.get_current_floor().image, (0, 0))

            if not sprite_inimigos:
                self.next_floor()
                return

            current_player = self.get_current_player()
            if current_player:
                self.dungeon.get_current_floor().get_current_enemy().auto_attack(tela, current_player) #chama a função "auto-atack" do inimigo
                self.draw_health_bar(current_player.health, 20, 20)
                self.draw_health_bar(
                    self.dungeon.get_current_floor().get_current_enemy().health, 680, 20)

                if self.dungeon.get_current_floor().get_current_enemy().alive() == False:
                    self.next_floor()
                    pygame.quit()
                    sys.exit()

                todas_as_sprites.draw(tela)
                sprite_inimigos.draw(tela)
                sprite_inimigos.update()
                todas_as_sprites.update()
                pygame.display.flip()  # atualiza a tela

    def cena_progresso(self):
        """
        cena que irá aparecer sempre que um andar for concluído, exceto se for o último andar.
        aqui vai ter na tela a lógica de leitura e escrita do arquivo csv para salvar o progresso.
        """

        texto_salvar = fonte.render(
            "Concluiu esse Floor! deseja salvar?", True, black)

        salvar_botao = pygame.Rect(
            largura // 2 - 100, altura // 2 - 25, 200, 50)
        salvar_texto = "Salvar"

        continue_botao = pygame.Rect(
            largura // 2 - 100, altura // 2 + 50, 200, 50)
        continue_texto = "Next Floor"

        exit_botao = pygame.Rect(
            largura // 2 - 100, altura // 2 + 125, 200, 50)
        exit_texto = "Exit"

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if salvar_botao.collidepoint(event.pos):
                        print("progresso salvo!")
                        self.salvar_progresso_csv()
                    elif continue_botao.collidepoint(event.pos):
                        print("clicou em continue")
                        return "jogar"
                    elif exit_botao.collidepoint(event.pos):
                        print("clicou em exit")
                        pygame.quit()
                        sys.exit()

            tela.blit(escolha, (0, 0))

            tela.blit(texto_salvar,
                      ((largura - texto_salvar.get_width()) // 2, 200))

            pygame.draw.rect(tela, black, salvar_botao)
            pygame.draw.rect(tela, black, continue_botao)
            pygame.draw.rect(tela, black, exit_botao)

            salvar_texto_renderizado = fonte.render(salvar_texto, True, white)
            continue_texto_renderizado = fonte.render(
                continue_texto, True, white)
            exit_texto_renderizado = fonte.render(exit_texto, True, white)

            tela.blit(salvar_texto_renderizado, (salvar_botao.x + (salvar_botao.width - salvar_texto_renderizado.get_width()
                                                                   ) // 2, salvar_botao.y + (salvar_botao.height - salvar_texto_renderizado.get_height()) // 2))
            tela.blit(continue_texto_renderizado, (continue_botao.x + (continue_botao.width - continue_texto_renderizado.get_width()
                                                                       ) // 2, continue_botao.y + (continue_botao.height - continue_texto_renderizado.get_height()) // 2))
            tela.blit(exit_texto_renderizado, (exit_botao.x + (exit_botao.width - exit_texto_renderizado.get_width()
                                                               ) // 2, exit_botao.y + (exit_botao.height - exit_texto_renderizado.get_height()) // 2))

            pygame.display.flip()

    def salvar_progresso_csv(self):
        """
        salva o progresso do jogo em um arquivo CSV chamado 'progresso.csv'.
        o progresso inclui o número do andar atual (current_floor) e informações do jogador atual (current_player).
        """
        with open('progresso.csv', 'w', newline='') as csvfile:
            fieldnames = ['current_floor', 'current_player']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            current_floor = self.dungeon.get_current_floor_number()
            current_player = self.get_current_player()

            if current_player:
                writer.writerow({
                    'current_floor': current_floor,
                    'current_player': str(current_player) # salva o nome do personagem de acordo  com seu método mágico __str__.
                })

    def carregar_progresso_csv(self):
        """
        carrega o progresso do jogo a partir do arquivo CSV 'progresso.csv'.
        Atualiza o andar atual (current_floor) e cria o jogador a partir das informações salvas no arquivo.
        """
        with open('progresso.csv', 'r') as csvfile:  # 'r' para ler o arquivo (read)
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Lendo progresso do arquivo...")
                self.dungeon.set_current_floor(int(row['current_floor'])) # pega a  informação do current_floor no arquivo e converte para int
                string_personagem = row['current_player'] # pega a informação do do player salva no arquivo para usar no método "criar_personagem_a_partir_de_string"
                print("Personagem do arquivo:", string_personagem)
                jogador = self.criar_personagem_a_partir_de_string(
                    string_personagem)
                if jogador:
                    todas_as_sprites.add(jogador)

    def criar_personagem_a_partir_de_string(self, string_personagem):
        """
        quando o arquivo é lido, cria o personagem de acordo com a sua string de identificação salva no seu método __str__ que foi salva no arquivo.
        recebe um argumento "string_personagem" que é essa informação salva no arquivo
        """
        if string_personagem == 'Warrior': 
            return Warrior(sprite_warrior, -100, 100)
        elif string_personagem == 'Hunter':
            return Hunter(sprite_hunter, -120, 60)
        elif string_personagem == 'Wizard':
            return Wizard(sprite_wizard, -40, 100)
        elif string_personagem == 'Knight':
            return Knight(-20, 250)
        else:
            print("Personagem não reconhecido:", string_personagem)
            return None

    def next_floor(self):
        """
        essa função verifica se o Floor não ultrapassou o numero existente de Floors,
        então chama novamente a função cena_jogar() e avança para o próximo floor
        """
        if self.dungeon.get_current_floor_number() < 3:
            self.dungeon.set_current_floor(1) # current_floor += 1.
            self.cena_progresso()
            self.cena_jogar()
        elif self.dungeon.get_current_floor_number() > 3: # se passou do último floor, o jogo fecha.
            pygame.quit()
            sys.exit()
        else:
            return None

    def draw_health_bar(self, health, x, y):
        """
        desenha as barras de saúde do personagem e do inimigo na tela
        recebe como argumento a vida do usuario (personagem ou inimigo) e a posição que a barra de vida irá ficar na tela.
        """
        ratio = health / 100
        pygame.draw.rect(tela, white, (x - 4, y - 4, 408, 38))
        pygame.draw.rect(tela, red, (x, y, 400, 30))
        pygame.draw.rect(tela, yellow, (x, y, 400 * ratio, 30))

    def get_current_player(self):
        for i in todas_as_sprites:
            i.move(tela, self.dungeon.get_current_floor().get_current_enemy())
            if isinstance(i, (Warrior, Hunter, Wizard, Knight)):
                return i
        return None


class Dungeon:
    def __init__(self):
        self.__floors = [Floor("Floor 1", battle1, "EvilWizard"),
                         Floor("Floor 2", battle2, "EvilWizardFire"),
                         Floor("Floor 3", battle3, "Cultist"),
                         Floor("Floor 4", battle4, "DarkWarrior")]
        self.__current_floor = 0

    def get_current_floor(self):
        """
        retorna o objeto floor de acordo com o número do floor atual.
        """
        if 0 <= self.__current_floor < len(self.__floors):
            return self.__floors[self.__current_floor]
        else:
            return None

    def get_current_floor_number(self):
        """
        retorna o número do andar atual.
        """
        return self.__current_floor

    def set_current_floor(self, new):
        """
        recebe o argumento "new" que sempre vai ser 1, para que assim que a função seja chamada ela incrementar + 1 no current floor
        (avançar um floor).
        """
        self.__current_floor += new




class Floor:
    def __init__(self, name, image, enemy_type):
        self.name = name
        self.image = image
        self.enemy_type = enemy_type
        self.__current_enemy = None

    def create_enemy(self, group):
        """
        recebe como argumento um group vazio e dependendo de qual floor estamos trabalhando,
        coloca o inimigo desse floor  no group e salva o mesmo em current_enemy.
        """
        if self.enemy_type == "EvilWizard":
            enemy = EvilWizard(sprite_evilwizard)
        elif self.enemy_type == "EvilWizardFire":
            enemy = EvilWizardFire(sprite_evilwizardfire)
        elif self.enemy_type == "Cultist":
            enemy = Cultist()
        elif self.enemy_type == "DarkWarrior":
            enemy = DarkWarrior(sprite_darkwarrior)
        else:
            enemy = None

        if enemy:
            group.add(enemy)
            self.__current_enemy = enemy
        return enemy

    def get_current_enemy(self):
        """
        retorna o current_enemy
        """
        return self.__current_enemy


run = GameEngine()
run.run()
