import sys
import pygame
import os
from pygame.locals import *
from projeto import *
from personagens import *
from inimigos import *

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
sprite_archer = pygame.image.load(os.path.join(
    diretorio_sprites, 'archer/archer.png')).convert_alpha()


# inimigos
sprite_darkwarrior = pygame.image.load(os.path.join(
    diretorio_sprites, 'darkwarrior/darkwarrior.png')).convert_alpha()
sprite_evilwizard = pygame.image.load(os.path.join(
    diretorio_sprites, 'evilwizard/evilwizard.png')).convert_alpha()
sprite_evilwizardfire = pygame.image.load(os.path.join(
    diretorio_sprites, 'evilwizardfire/evilwizardfire.png')).convert_alpha()


todas_as_sprites = pygame.sprite.Group()

# Instâncias

hunter = Hunter(sprite_hunter, -120, 60)
warrior = Warrior(sprite_warrior, -100, 100)
wizard = Wizard(sprite_wizard, -40, 100)
archer = Archer(sprite_archer, -20, 170)
knight = Knight(-20, 250)



# darkwarrior = DarkWarrior(sprite_darkwarrior)
# evilwizard = EvilWizard(sprite_evilwizard)
# evilwizardfire = EvilWizardFire(sprite_evilwizardfire)
# cultist = Cultist()


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

fundo_best = pygame.image.load("images/fundo/best01.jpg").convert()
fundo_best = pygame.transform.scale(fundo_best, (largura, altura))

escolha = pygame.image.load("images/fundo/escolha.png").convert()
escolha = pygame.transform.scale(escolha, (largura, altura))


# cores

black = (0, 0, 0) # cor preta
white = (255, 255, 255) # cor branca
yellow = (255, 255, 0)  # cor amarela
red = (255, 0, 0) # cor vermelha

cor_botao = black
cor_texto = white  

play_botao = pygame.Rect(largura // 2 - 100, altura // 2 - 25, 200, 50)
play_cor = cor_botao
play_texto = "Play"

best_botao = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)
best_cor = cor_botao
best_texto = "Bestiary"

exit_botao = pygame.Rect(largura // 2 - 100, altura // 2 + 125, 200, 50)
exit_cor = cor_botao
exit_texto = "Exit"

botao_archer = pygame.Rect(largura // 2 - 100, altura // 2 - 100, 200, 50)
botao_warrior = pygame.Rect(largura // 2 - 100, altura // 2 - 25, 200, 50)
botao_hunter = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)
botao_wizard = pygame.Rect(largura // 2 - 100, altura // 2 + 125, 200, 50)
botao_knight = pygame.Rect(largura // 2 - 100, altura // 2 + 200, 200, 50)

fonte = pygame.font.Font("fonts/BerkshireSwash-Regular.ttf", 30)


class GameEngine:
    def __init__(self):
        self.player = None
        self.dungeon = Dungeon()
        # self.backgrounds = [menu, battle1, battle2,
        #                     battle3, battle4, fundo_best, escolha]
        self.current_cena = "menu"
        self.floor_in_progress = False

    def run(self):

        while True:
            if self.current_cena == "menu":
                self.current_cena = self.cena_menu()
            elif self.current_cena == "jogar":
                self.current_cena = self.cena_jogar()
            elif self.current_cena == "escolher_personagem":
                self.current_cena = self.cena_escolher_personagem()


    def cena_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_botao.collidepoint(event.pos):
                        print("clicou em play")
                        return "escolher_personagem"
                    elif best_botao.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif exit_botao.collidepoint(event.pos):
                        print("clicou em exit")
                        pygame.quit()
                        sys.exit()

            tela.blit(escolha, (0, 0))

            pygame.draw.rect(tela, play_cor, play_botao)
            pygame.draw.rect(tela, best_cor, best_botao)
            pygame.draw.rect(tela, exit_cor, exit_botao)

            play_texto_renderizado = fonte.render(play_texto, True, cor_texto)
            best_texto_renderizado = fonte.render(best_texto, True, cor_texto)
            exit_texto_renderizado = fonte.render(exit_texto, True, cor_texto)

            tela.blit(play_texto_renderizado, (play_botao.x + (play_botao.width - play_texto_renderizado.get_width()
                                                               ) // 2, play_botao.y + (play_botao.height - play_texto_renderizado.get_height()) // 2))
            tela.blit(best_texto_renderizado, (best_botao.x + (best_botao.width - best_texto_renderizado.get_width()
                                                               ) // 2, best_botao.y + (best_botao.height - best_texto_renderizado.get_height()) // 2))
            tela.blit(exit_texto_renderizado, (exit_botao.x + (exit_botao.width - exit_texto_renderizado.get_width()
                                                               ) // 2, exit_botao.y + (exit_botao.height - exit_texto_renderizado.get_height()) // 2))

            pygame.display.flip()

    def cena_escolher_personagem(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_archer.collidepoint(event.pos):
                        todas_as_sprites.add(archer)
                        return ("jogar")
                    elif botao_warrior.collidepoint(event.pos):
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
                "Choose your character", True, cor_botao)
            tela.blit(texto_escolha,
                      ((largura - texto_escolha.get_width()) // 2, 90))

            pygame.draw.rect(tela, cor_botao, botao_archer)
            pygame.draw.rect(tela, cor_botao, botao_warrior)
            pygame.draw.rect(tela, cor_botao, botao_hunter)
            pygame.draw.rect(tela, cor_botao, botao_wizard)
            pygame.draw.rect(tela, cor_botao, botao_knight)

            texto_archer = fonte.render("Archer", True, cor_texto)
            texto_warrior = fonte.render("Warrior", True, cor_texto)
            texto_hunter = fonte.render("Hunter", True, cor_texto)
            texto_wizard = fonte.render("Wizard", True, cor_texto)
            texto_knight = fonte.render("Knight", True, cor_texto)

            tela.blit(texto_archer, (botao_archer.x + (botao_archer.width - texto_archer.get_width()) // 2,
                                     botao_archer.y + (botao_archer.height - texto_archer.get_height()) // 2))
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

        relogio = pygame.time.Clock()
        FPS = 30
        
        

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
                if self.dungeon.advance_to_next_floor():
                    tela.blit(self.dungeon.get_current_floor().image, (0, 0))
                    # cria os inimigos para o novo andar
                    sprite_inimigos = pygame.sprite.Group()
                    self.dungeon.get_current_floor().create_enemy(sprite_inimigos)

            # esse for não tinha esperança de dar certo, mas deu, puthon é surreal kkkkkkk
            for i in todas_as_sprites:
                i.move(tela, self.current_enemy())
                
                if isinstance(i,(Archer, Warrior, Hunter, Wizard, Knight)):
                    current_player = i  
                    
                    
                self.draw_health_bar(current_player.health, 20, 20)  
                self.draw_health_bar(self.current_enemy().health, 680, 20)

            if self.current_enemy().alive() == False:
                self.dungeon.current_floor += 1
                self.next_floor()

            todas_as_sprites.draw(tela)
            sprite_inimigos.draw(tela)
            sprite_inimigos.update()
            todas_as_sprites.update()


    def next_floor(self):
        if self.dungeon.current_floor <= 3:
            self.cena_jogar()
        elif self.dungeon.current_floor > 3:
            pygame.quit()
            sys.exit()
        else:
            return None
            
    def draw_health_bar(self, health, x, y):
        ratio = health / 100
        pygame.draw.rect(tela, white, (x - 4, y - 4, 408, 38))
        pygame.draw.rect(tela, red, (x, y, 400, 30))
        pygame.draw.rect(tela, yellow, (x, y, 400 * ratio, 30))


    def current_enemy(self):
        return self.dungeon.get_current_floor().get_current_enemy()

class Dungeon:
    def __init__(self):
        self.floors = [Floor("Floor 1", battle1, "EvilWizard"),
                       Floor("Floor 2", battle2, "EvilWizardFire"),
                       Floor("Floor 3", battle3, "Cultist"),
                       Floor("Floor 4", battle4, "DarkWarrior")]
        self.current_floor = 0

    def get_current_floor(self):
        if 0 <= self.current_floor < len(self.floors):
            return self.floors[self.current_floor]
        else:
            return None

    def to_next_floor(self):
        # verifica se há um próximo andar disponível
        if self.current_floor + 1 < len(self.floors):
            self.current_floor += 1
            return True
        else:
            return False


class Floor:
    def __init__(self, name, image, enemy_type):
        self.name = name
        self.image = image
        self.enemy_type = enemy_type
        self.current_enemy = None

    def create_enemy(self, group):
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
            self.current_enemy = enemy
        return enemy

    def get_current_enemy(self):
        return self.current_enemy


run = GameEngine()
run.run()
