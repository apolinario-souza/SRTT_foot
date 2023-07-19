import pygame
import random
import numpy as np
import time
import sys
from contents.constants import WIDTH, HEIGHT, INTERSTIMULUS_INTERVAL, RED, key_mapping
from contents.constants import BLACK, GRAY, STIMULUS_SIZE, SEQUENCE, N_TRIAL, SUJ, GREEN,key_mapping_S 


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foot serial reaction time task")


# Variável de controle

reaction_times = []  # Lista para armazenar os tempos de reação
 
    
def draw_warning (text, WIDTH, HEIGHT,cor_texto):
    
    cor_fundo = (0, 0, 0)  # preto

    fonte = pygame.font.Font(None, 100)  # define a fonte e o tamanho

    texto = fonte.render(text, True, cor_texto, cor_fundo)

    largura_texto = texto.get_width()
    altura_texto = texto.get_height()
    

    x = (WIDTH - largura_texto) // 2
    y = (HEIGHT - altura_texto) // 2

    screen.fill(cor_fundo)
    screen.blit(texto, (x, y))
    pygame.display.flip()

def draw_button(check, cor):
    #draw_backgroud()
    size_x = WIDTH*.12
    size_y = HEIGHT*.25
    
    fator_centro_esq = 0.89
    fator_centro_dir = 1.21
    
    if check==2:
        #Lateral direito
        x = (WIDTH // 2  - (size_x//2))*1.53
        y = HEIGHT // 2 - (size_y//2)     
        
    elif check==3:
        #Superior direito
        x = (WIDTH // 2  - (size_x//2))*fator_centro_dir
        y = (HEIGHT // 2 - (size_y//2))*.25 #Ajustar a altura, quanto maior menor a distância
        
    elif check==4:
        #Superior esquerdo
        x = (WIDTH // 2  - (size_x//2))*fator_centro_esq 
        y = (HEIGHT // 2 - (size_y//2))*.25  
                
        
    elif check==5:
        #Lateral Esquerdo
        x = (WIDTH // 2  - (size_x//2))*.57
        y = HEIGHT // 2 - (size_y//2)        
               
    elif check==6:
        #Inferior Esquerdo
        x = (WIDTH // 2  - (size_x//2))*fator_centro_esq 
        y = (HEIGHT // 2 - (size_y//2))*1.75 #Ajustar a altura, a logica do y é invertida        
        
    elif check==7:
        #Inferior direito
        x = (WIDTH // 2  - (size_x//2))*fator_centro_dir
        y  = (HEIGHT // 2 - (size_y//2))*1.75 #Ajustar a altura, a logica do y é invertida
    elif check == 8:
        #centro esquerdo  
        x = (WIDTH // 2  - (size_x//2))*fator_centro_esq 
        y = HEIGHT // 2 - (size_y//2)
        pygame.draw.rect(screen, GRAY, (x, y, size_x,size_y))
    elif check == 9:
        #centro direito   
        x = (WIDTH // 2  - (size_x//2))*fator_centro_dir
        y = HEIGHT // 2 - (size_y//2)
        pygame.draw.rect(screen, GRAY, (x, y, size_x,size_y)) 
       
        
        
        
        
    
        
    pygame.draw.rect(screen, cor, (x, y, size_x,size_y))
    
        
 
def draw_stimulus(position,interstimulus):
    start_time = time.time()
    draw_button(2, GRAY) #background
    draw_button(3, GRAY) #background
    draw_button(4, GRAY) #background
    draw_button(5, GRAY) #background
    draw_button(6, GRAY) #background
    draw_button(7, GRAY) #background
    #draw_button(8, GRAY) #background
    #draw_button(9, GRAY) #background
    
    '''
    Função para desenhar os estímulos na tela
    '''  
    if position >=2:        
        draw_button(position,RED)
        
    elif position==0:
        end_time = time.time()        
        draw_warning ("Prepara!",WIDTH, HEIGHT, RED)
    elif position==1:
        end_time = time.time()        
        draw_warning ("Vai!",WIDTH, HEIGHT, GREEN)
            
# Função para apresentar um estímulo e registrar a resposta do participante
def present_stimulus(position,interstimulus):
    draw_stimulus(position,interstimulus)
    pygame.display.flip()
    start_time = time.time()
    
    
    response = True
    while response:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == key_mapping[position] and position>=2:
                    
                    response = False
                    end_time = time.time()
                    reaction_time = end_time - start_time 
                    reaction_times.append(reaction_time) #adiciona o tempo que pressionou
                    
                if event.key==key_mapping[position] or event.key==key_mapping_S[0] and position<2:
                    response = False
                    #aqui eu não adicino nada pois e o tempo que apertou a 1vez
                                
            elif event.type==pygame.KEYUP: #liberou
                if event.key == key_mapping[position] or event.key == key_mapping_S[0]:
                    response = False
                    end_time = time.time()
                    reaction_time = end_time - start_time 
                    reaction_times.append(reaction_time) #adiciona o tempo de soltar
                    
            
                
    
    
    screen.fill(BLACK)
    pygame.display.flip()
   
    time.sleep(interstimulus/1000.0)
    
    

# Loop principal do jogo

running = True
trial = 0
while running:
    
    for event in pygame.event.get():
        if N_TRIAL == trial:
            running = False
            reaction_times  = np.array(reaction_times)
            pygame.quit()
            sys.exit()
    cont = 0
    
    for k, position in enumerate(SEQUENCE):
        present_stimulus(position,INTERSTIMULUS_INTERVAL[k])
        cont =+1   
    trial +=1
    
    pygame.display.flip()
    
    ind = (len(SEQUENCE)-1)*-1
    save = np.array(reaction_times[ind:])
    
    np.savetxt('trials/SUJ'+str(SUJ)+'_trial'+str(trial)+'.csv', save, delimiter=',')
    
    print(reaction_times[ind:])
        
    