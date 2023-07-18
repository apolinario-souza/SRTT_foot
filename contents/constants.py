#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:57:43 2023

@author: tercio
"""
import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da janela

#Configuration screen
screen = pygame.display.set_mode()
WIDTH, HEIGHT  = screen.get_size()

# Parâmetros da tarefa
SUJ = 1
N_TRIAL = 3
SEQUENCE = [0, 1, 2, 3, 4,5,6,7]  # Sequência de estímulos (exemplo com 4 posições + 0 =Warning; 1 = imperatus)
STIMULUS_SIZE = 100  # Tamanho do estímulo
INTERSTIMULUS_INTERVAL = [500,0,0,0,0,0,0,500]  # Intervalo entre os estímulos (em milissegundos)




# Cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128,128,128)

key_mapping_S = {
0: pygame.K_c, #botao centro
}


# Mapeamento das teclas para cada posição do estímulo
key_mapping = {
    0: pygame.K_b, #botao centro
    1: pygame.K_b, #botao centro
    
    2: pygame.K_a, #primeiro componente
    3: pygame.K_s,
    4: pygame.K_d,
    5: pygame.K_f,
    6: pygame.K_g,
    7: pygame.K_h,
}
