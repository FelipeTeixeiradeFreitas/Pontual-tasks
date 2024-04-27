import random
import time
import pyautogui
import keyboard
import sys
import cv2
import numpy as np

continuar_execucao = True



def check_banco():
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    mouse_banco_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\banco_ge.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, mouse_banco_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias >= 1:
        return True
    else:
        return False

#rodar scroll 7 vezes para zoom
def mover_mouse_rota_aleatoria(destino_x, destino_y):
    # Obtendo as coordenadas atuais do mouse
    x_inicial, y_inicial = pyautogui.position()

    # Gerando margens aleatórias para o ponto de controle, o número de passos e o tempo de espera
    margem_ponto_controle = random.randint(-200, 100)
    num_passos = random.randint(10, 30)
    margem_tempo_espera = random.uniform(0.01, 0.1)
    margem_tempo_duracao = random.uniform(0.01, 0.1)

    # Gerando o ponto de controle dentro da margem
    ponto_controle_x = random.uniform(min(x_inicial, destino_x) - margem_ponto_controle, (x_inicial + destino_x) / 2)
    ponto_controle_y = random.uniform(min(y_inicial, destino_y) - margem_ponto_controle, min(x_inicial, destino_x) - margem_ponto_controle)

    
    # Movendo o mouse ao longo da curva Bezier
    for i in range(num_passos):
        t = i / (num_passos - 1)  # Parâmetro de interpolação entre 0 e 1
        curva_x = (1 - t) ** 2 * x_inicial + 2 * (1 - t) * t * ponto_controle_x + t ** 2 * destino_x
        curva_y = (1 - t) ** 2 * y_inicial + 2 * (1 - t) * t * ponto_controle_y + t ** 2 * destino_y

        # Movendo o mouse para as novas coordenadas na curva Bezier
        pyautogui.moveTo(curva_x, curva_y, duration=random.uniform(0.01, margem_tempo_duracao))  # Tempo de duração aleatório
        time.sleep(random.uniform(0, margem_tempo_espera))  # Tempo de espera aleatório entre os passos

    # Movendo o mouse para o ponto final
    pyautogui.moveTo(destino_x, destino_y, duration=random.uniform(0.1, 0.5))


            



def repeticao():

    inicio = time.time()
    #pyautogui.moveTo(710, 3830)
    #mostrar_coordenadas_em_tempo_real()
    #funcao_acao(793, 816, 737, 752)
    #pyautogui.click()
    i=0
    quantidade_colares = 420
    repeticoes = quantidade_colares / 27
    while i < repeticoes:
        # abrir banco
        funcao_acao(279, 482, 313, 486)
        check_banco()
        pyautogui.click()
        tempo_aleatorio = random.uniform(1, 3)
        time.sleep(tempo_aleatorio)  
        #depositar aneis
        funcao_acao(1200, 1220, 437, 450)
        pyautogui.click() 
        tempo_aleatorio = random.uniform(0.1, 1)
        time.sleep(tempo_aleatorio)  
        # tirar diamante
        funcao_acao(424, 446, 289, 302)
        pyautogui.click()
        tempo_aleatorio = random.uniform(1, 3)
        time.sleep(tempo_aleatorio)  
        #sair banco
        pyautogui.press('esc')
        tempo_aleatorio = random.uniform(0.1, 2)
        time.sleep(tempo_aleatorio)  
        ################
        probabilidade=random.random()
        if probabilidade < 0.6:
            funcao_acao(200, 500, 200, 500)
            tempo_aleatorio = random.uniform(0.1, 0.5)
            time.sleep(tempo_aleatorio)  
        ################
        #fazer encantamento
        funcao_acao(1294, 1310, 530, 548)
        pyautogui.click() 
        tempo_aleatorio = random.uniform(0.1, 3)
        time.sleep(tempo_aleatorio) 
        funcao_acao(1225, 1241, 530, 550)
        pyautogui.click() 
        tempo_aleatorio = random.uniform(0.1, 2)
        time.sleep(tempo_aleatorio) 
        funcao_acao(1200, 1220, 437, 450)
        pyautogui.click()  
        tempo_aleatorio = random.uniform(120, 130)
        time.sleep(tempo_aleatorio)
        ################
        probabilidade=random.random()
        if probabilidade < 0.6:
            funcao_acao(200, 500, 200, 500)
            tempo_aleatorio = random.uniform(0.1, 3)
            time.sleep(tempo_aleatorio)  
        ################
        
        i= i+1


def exibe_coordenadas():
    x, y = pyautogui.position()
    # Exibe as coordenadas na tela
    print(f'Coordenadas do mouse: x={x}, y={y}')


# Chamada da função para mover o mouse usando uma curva de Bezier
#mover_mouse_curva_bezier(500, 500, 5)  # Exemplo: movimento usando curva de Bezier em direção ao ponto (500, 500) em 5 segundos


# Função para mostrar as coordenadas atuais do mouse em tempo real
def mostrar_coordenadas_em_tempo_real():
    try:
        while True:
            # Obtém as coordenadas atuais do cursor do mouse
            x, y = pyautogui.position()
            # Exibe as coordenadas na tela
            print(f'Coordenadas do mouse: x={x}, y={y}', end='\r')  # '\r' move o cursor de volta ao início da linha
    except KeyboardInterrupt:
        print("\nEncerrando a exibição das coordenadas.")

# Chamada da função para mostrar as coordenadas em tempo real
#mostrar_coordenadas_em_tempo_real()



def funcao_acao(x_min, x_max, y_min, y_max):
    
    # Espera um tempo aleatório antes de clicar
    tempo_aleatorio = random.uniform(0.5, 1)
    time.sleep(tempo_aleatorio)
    novo_x = random.randint(x_min, x_max)  # Substitua 1920 pela largura da sua tela
    #print(novo_x)
    novo_y = random.randint(y_min, y_max)  # Substitua 1080 pela altura da sua tela
    #print(novo_y)
    duração_aleatória = random.uniform(0.5, 2)

# Move o mouse para as coordenadas geradas aleatoriamente
    #pyautogui.moveTo(novo_x, novo_y, duration=duração_aleatória)  # Você pode ajustar a duração conforme necessário
    mover_mouse_rota_aleatoria(novo_x, novo_y)
# Espera um tempo aleatório antes de clicar
    tempo_aleatorio = random.uniform(0.5, 1)
    time.sleep(tempo_aleatorio)
    return novo_x

#mostrar_coordenadas_em_tempo_real()
repeticao()
    

    #pyautogui.click()

#while continuar_execucao:
#final = True
#while final == True:
    #repeticao()

