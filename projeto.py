import sys
import pygame
from pygame.locals import *
from sys import exit

pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Journey')
largura = 1000
altura = 550
tela = pygame.display.set_mode((largura, altura))
musica_de_fundo = pygame.mixer.music.load("audio/music/cloud-of-sorrow.wav")
# com o -1 a musica reinicia quando acabar, ou seja ela fica em looping
pygame.mixer.music.play(-1)






fundo = pygame.image.load("images/fundo/image01.jpg")
fundo2 = pygame.image.load("images/fundo/image02.jpg")
fundo_best = pygame.image.load("images/fundo/best01.jpg")

# cores

cor_botao = (0, 0, 0)
cor_texto = (255, 255, 255)

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
                    return "best" # mudar para a cena bestiário
                elif exit_botao.collidepoint(event.pos):
                    print("clicou em exit")
                    pygame.quit()
                    sys.exit()

        # Preencher a tela
        tela.blit(fundo, (0, 0))

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
        pygame.display.update()

        # Controlar a taxa de atualização
        # pygame.time.Clock().tick(60)


def cena_jogar():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # preencher com preto, para limpar a tela
        tela.fill((0, 0, 0))

        # preencher a tela com a cor de fundo da cena de jogar
        tela.blit(fundo2, (0, 0))

        # atualizar a tela
        pygame.display.update()

        
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
        pygame.display.update()

        
        
# Iniciar a cena do menu
cena_atual = "menu"

while True:
    if cena_atual == "menu":
        cena_atual = cena_menu()
    elif cena_atual == "jogar":
        cena_atual = cena_jogar()
    elif cena_atual == "best":
        cena_atual = cena_bestiario()
