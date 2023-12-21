import sys
import pygame
import os
from pygame.locals import *
from personagens import *

diretorio_principal = os.path.dirname(__file__)
diretorio_sprites = os.path.join(diretorio_principal, 'sprites')




pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Journey')
largura = 1000
altura = 550
tela = pygame.display.set_mode((largura, altura))
musica_de_fundo = pygame.mixer.music.load("audio/music/cloud-of-sorrow.wav")
# com o -1 a musica reinicia quando acabar, ou seja ela fica em looping
pygame.mixer.music.play(-1)


# Sprites
sprite_warrior = pygame.image.load(os.path.join(diretorio_sprites, 'warrior/warrior.png')).convert_alpha()
sprite_hunter = pygame.image.load(os.path.join(diretorio_sprites, 'hunter/hunter.png')).convert_alpha()
sprite_wizard = pygame.image.load(os.path.join(diretorio_sprites, 'wizard/wizard.png')).convert_alpha()


todas_as_sprites = pygame.sprite.Group()
hunter = Hunter(sprite_hunter)
warrior = Warrior(sprite_warrior)
wizard = Wizard(sprite_wizard)
# todas_as_sprites.add(wizard)
# todas_as_sprites.add(hunter)
# todas_as_sprites.add(warrior)


menu = pygame.image.load("images/fundo/menu.png").convert()
menu = pygame.transform.scale(menu, (largura, altura))

battle1 = pygame.image.load("images/fundo/Battleground1.png").convert()
battle1 = pygame.transform.scale(battle1, (largura, altura))

fundo_best = pygame.image.load("images/fundo/best01.jpg").convert()

# cores

cor_botao = (0, 0, 0)  # cor preta
cor_texto = (255, 255, 255)  # cor branca

# Configurações do botão "Play"
play_botao = pygame.Rect(largura // 2 - 100, altura // 2 - 25, 200, 50)
play_cor = cor_botao
play_texto = "Play"

# Configurações do botão "Bestiary"
best_botao = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)
best_cor = cor_botao
best_texto = "Bestiary"

# Configurações do botão "Exit"
exit_botao = pygame.Rect(largura // 2 - 100, altura // 2 + 125, 200, 50)
exit_cor = cor_botao
exit_texto = "Exit"

# Configurações do texto
fonte = pygame.font.Font("fonts/BerkshireSwash-Regular.ttf", 30)


def cena_menu():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_botao.collidepoint(event.pos):
                    print("clicou em play")
                    return "jogar"  # mudar para a cena de jogar
                elif best_botao.collidepoint(event.pos):
                    print('clicou em bestiary')
                    return "best"  # mudar para a cena bestiário
                elif exit_botao.collidepoint(event.pos):
                    print("clicou em exit")
                    pygame.quit()
                    sys.exit()

        # Preencher a tela
        tela.blit(menu, (0, 0))

        # Desenhar os botões retangulos
        pygame.draw.rect(tela, play_cor, play_botao)
        pygame.draw.rect(tela, best_cor, best_botao)
        pygame.draw.rect(tela, exit_cor, exit_botao)

        # Adicionar texto nos botões
        play_texto_renderizado = fonte.render(play_texto, True, cor_texto)
        best_texto_renderizado = fonte.render(best_texto, True, cor_texto)
        exit_texto_renderizado = fonte.render(exit_texto, True, cor_texto)

        tela.blit(play_texto_renderizado, (play_botao.x + (play_botao.width - play_texto_renderizado.get_width()
                                                           ) // 2, play_botao.y + (play_botao.height - play_texto_renderizado.get_height()) // 2))
        tela.blit(best_texto_renderizado, (best_botao.x + (best_botao.width - best_texto_renderizado.get_width()
                                                           ) // 2, best_botao.y + (best_botao.height - best_texto_renderizado.get_height()) // 2))
        tela.blit(exit_texto_renderizado, (exit_botao.x + (exit_botao.width - exit_texto_renderizado.get_width()
                                                           ) // 2, exit_botao.y + (exit_botao.height - exit_texto_renderizado.get_height()) // 2))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização
        # pygame.time.Clock().tick(60)


def cena_jogar():
    relogio = pygame.time.Clock()
    while True:
        relogio.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        tela.blit(battle1, (0, 0))
        todas_as_sprites.add(wizard)
        todas_as_sprites.draw(tela)
        todas_as_sprites.update()

        # atualizar a tela
        pygame.display.flip()


def cena_bestiario():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # preencher com preto, para limpar a tela
        tela.fill((0, 0, 0))

        # preencher a tela com a cor de fundo da cena de jogar
        tela.blit(fundo_best, (0, 0))

        # atualizar a tela
        pygame.display.flip()


# Iniciar a cena do menu
cena_atual = "menu"

while True:
    if cena_atual == "menu":
        cena_atual = cena_menu()
    elif cena_atual == "jogar":
        cena_atual = cena_jogar()
    elif cena_atual == "best":
        cena_atual = cena_bestiario()
