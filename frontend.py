import pygame,sys
from backend import *

pygame.init()
size = largura,altura = 400,200
tela = pygame.display.set_mode(size)
fonte = pygame.font.SysFont("Areal",52, True)
R = Relogio()

while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): sys.exit()
    R.atualiza()
    tela.fill((255,255,255))
    hora = fonte.render('{:02d}:{:02d}:{:02d}'.format(R.get_hora(),R.get_minuto(),R.get_segundo()),1,(255,0,0))
    tela.blit(hora,(115,75))
    pygame.display.update()
