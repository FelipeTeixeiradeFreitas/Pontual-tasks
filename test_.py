import random
import time
import pyautogui
import keyboard
import sys
import cv2
import numpy as np

coordenadas_anel_safira = {'BANCO': [424, 446, 289, 302], 'MOLDAR': [408, 416, 222, 229]}
coordenadas_amuleto_safira = {'BANCO': [424, 446, 289, 302], 'MOLDAR': [415, 417, 338, 347]}
coordenadas_amuleto_esmeralda = {'BANCO': [476, 487, 289, 302], 'MOLDAR': [461, 469, 338, 347]}
coordenadas_amuleto_ruby = {'BANCO': [525, 527, 289, 302], 'MOLDAR': [512, 517, 341, 345]}

continuar_execucao = True





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

def on_esc_press(event):
    if event.name == 'esc':
        KeyboardInterrupt
        try:
            print('bull')
            time.sleep(10)
        except:
            print("Programa interrompido pelo usuário")
            

# Adicione um manipulador de eventos para a tecla "Esc"
keyboard.on_press(on_esc_press)





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
#repeticao()
   

    #pyautogui.click()

#while continuar_execucao:
#final = True
#while final == True:
    #repeticao()

def evolucao(x_min, x_max, y_min, y_max):
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    level_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\evolucao_criacao.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, level_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias > 0:
        tempo_aleatorio = random.uniform(1, 3)
        time.sleep(tempo_aleatorio)
        #funcao_acao(693, 695, 359, 372)
        #pyautogui.click() 
        pyautogui.press('space')
        tempo_aleatorio = random.uniform(1, 3)
        time.sleep(tempo_aleatorio)
        #funcao_acao(x_min, x_max, y_min, y_max)
        #pyautogui.click() 
        tempo_aleatorio = random.uniform(30, 33)
        time.sleep(tempo_aleatorio)
        return True
            # Mover o mouse para o centro do retângulo delimitador
            #pyautogui.moveTo(centro_x, centro_y, duration=0.5)
    else:
        return False


def check_fornalha():
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    mouse_banco_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\checar_fornalha.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, mouse_banco_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc
    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias == 1:
        return True
    else:
        return False
    




def check_bancoaberto():
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    mouse_banco_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\checar_banco_aberto.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, mouse_banco_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc
    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias == 1:
        return True
    else:
        return False

def check_banco():
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    mouse_banco_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, mouse_banco_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias == 1:
        return True
    else:
        return False



def check(endereco):
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    mouse_banco_img = cv2.imread(endereco)  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, mouse_banco_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc
    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias == 1:
        return True
    else:
        return False


def safespot():
    time.sleep(4)
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    atalho_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\safespot.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, atalho_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.8)  # Defina um threshold adequado
    if quantidade_ocorrencias == 1:

        largura, altura = atalho_img.shape[1], atalho_img.shape[0]
        centro_x = x + largura // 2
        centro_y = y + altura // 2
        x_min = centro_x-3
        x_max = centro_x+3
        y_min = centro_y-3
        y_max = centro_y+3
    # Mover o mouse para o centro do retângulo delimitador
    #funcao_acao(centro_x-3, centro+3)
        funcao_acao(x_min, x_max, y_min, y_max)
        tempo_aleatorio = random.uniform(12, 15)
        pyautogui.click()
        time.sleep(tempo_aleatorio)
        funcao_acao(658, 674, 388, 405)
        pyautogui.click()
        tempo_aleatorio = random.uniform(0.1, 1)
        time.sleep(tempo_aleatorio)
        funcao_acao(736, 747, 527, 540)
        pyautogui.click()
        tempo_aleatorio = random.uniform(0.1, 1)
        time.sleep(tempo_aleatorio)
        funcao_acao(380, 392, 249, 264)
        pyautogui.click()
        tempo_aleatorio = random.uniform(0.1, 1)
        time.sleep(tempo_aleatorio)
        funcao_acao(429, 437, 253, 264)
        pyautogui.click()
        return True
    else:
        return False

    



def repeticao_anel(quantidade_colar):

    inicio = time.time()
    #pyautogui.moveTo(710, 3830)
    #mostrar_coordenadas_em_tempo_real()
    #funcao_acao(793, 816, 737, 752)
    #pyautogui.click()
    time.sleep(2)
    #banco_init
    funcao_acao(658, 674, 388, 405)
    pyautogui.click()
    i=0
    continuar = True
    quantidade_repeticoes = quantidade_colar / 27
    while i < quantidade_repeticoes and continuar:
        probabilidade=random.random()
            # tirar ouro e diamante
        funcao_acao(380, 394, 289, 302)
        pyautogui.click()
        tempo_aleatorio = random.uniform(0.5, 1.5)
        time.sleep(tempo_aleatorio)
        pyautogui.click()
        #fornalha
        funcao_acao(1006, 1010, 256, 261)
        pyautogui.click()
        tempo_aleatorio = random.uniform(8, 10)
        ################
        probabilidade=random.random()
        if probabilidade < 0.2:
            funcao_acao(200, 500, 200, 500)
        ################
        time.sleep(tempo_aleatorio)
        #fazer anel
        #funcao_acao(461, 469, 338, 347)#esmeralda
        #funcao_acao(512, 517, 341, 345) #roby
        funcao_acao(359, 363, 221, 229) #anel
        pyautogui.click() 
        tempo_aleatorio = random.uniform(60, 63)
        time.sleep(tempo_aleatorio)
        evolucao(359, 363, 221, 229)  
        #banco
        funcao_acao(220, 225, 544, 546)
        tempo_aleatorio = random.uniform(1, 1.5)
        time.sleep(tempo_aleatorio)
        continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')
        #continuar = check_banco()
        if continuar == False:
            tempo_aleatorio = random.uniform(1, 1.5)
            time.sleep(tempo_aleatorio)
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')
            #continuar = check_banco()
        pyautogui.click()
        tempo_aleatorio = random.uniform(7, 9)
        ################
        probabilidade=random.random()
        if probabilidade < 0.6:
            funcao_acao(200, 500, 200, 500)
        ################
        time.sleep(tempo_aleatorio) 
        continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco_aberto.png')
        #continuar = check_bancoaberto()
        if continuar == False:
            time.sleep(20)
            #continuar = check_bancoaberto()
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco_aberto.png') 
        #depositar aneis
        funcao_acao(1200, 1220, 437, 450)
        pyautogui.click() 
        i= i+1





def repeticao(tipo_joia, quantidade_colar):

    inicio = time.time()
    #pyautogui.moveTo(710, 3830)
    #mostrar_coordenadas_em_tempo_real()
    #funcao_acao(793, 816, 737, 752)
    #pyautogui.click()
    time.sleep(2)
    #banco_init
    funcao_acao(658, 674, 388, 405)
    pyautogui.click()
    i=0
    continuar = True
    quantidade_repeticoes = quantidade_colar / 13
    while i < quantidade_repeticoes and continuar:
        probabilidade=random.random()
            # tirar ouro e diamante
        if probabilidade < 0.3:
            funcao_acao(380, 394, 289, 302)
            pyautogui.click()
            funcao_acao(tipo_joia['BANCO'][0], tipo_joia['BANCO'][1], tipo_joia['BANCO'][2], tipo_joia['BANCO'][3])
            pyautogui.click()
        else:
            funcao_acao(tipo_joia['BANCO'][0], tipo_joia['BANCO'][1], tipo_joia['BANCO'][2], tipo_joia['BANCO'][3])
            pyautogui.click()
            funcao_acao(380, 394, 289, 302)
            pyautogui.click()
        #fornalha
        funcao_acao(1006, 1010, 256, 261)
        for _ in range(4):
            #continuar = check_fornalha()
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_fornalha.png')
            if continuar == True:
                break
            else:
                time.sleep(20)
                funcao_acao(1006, 1010, 256, 261)
        pyautogui.click()
        tempo_aleatorio = random.uniform(9, 11)
        ################
        probabilidade=random.random()
        if probabilidade < 0.2:
            funcao_acao(200, 500, 200, 500)
        ################
        time.sleep(tempo_aleatorio)
        #fazer ruby
        for _ in range(2):
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_fornalhaaberta.png')
            if continuar == True:
                break
            else:
                time.sleep(20)
        funcao_acao(tipo_joia['MOLDAR'][0], tipo_joia['MOLDAR'][1], tipo_joia['MOLDAR'][2], tipo_joia['MOLDAR'][3])
        pyautogui.click() 
        tempo_aleatorio = random.uniform(30, 33)
        time.sleep(tempo_aleatorio)
        evl = evolucao(tipo_joia['MOLDAR'][0], tipo_joia['MOLDAR'][1], tipo_joia['MOLDAR'][2], tipo_joia['MOLDAR'][3])  
        #banco
        funcao_acao(220, 225, 544, 546)
        tempo_aleatorio = random.uniform(1, 1.5)
        time.sleep(tempo_aleatorio)
        if evl == False:
            #continuar = check_banco()
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')
        if evl == True:

            #continuar = check_banco()
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')
            evl = False
        if continuar == False:
            tempo_aleatorio = random.uniform(1, 1.5)
            time.sleep(tempo_aleatorio)
            continuar = check('C:\\Users\\Suiany\\Documents\\python project\\checar_banco.png')
            #continuar = check_banco()
        pyautogui.click()
        tempo_aleatorio = random.uniform(9, 11)
        ################
        probabilidade=random.random()
        if probabilidade < 0.6:
            funcao_acao(200, 500, 200, 500)
        ################
        if continuar == False:
            continuar = safespot()
        time.sleep(tempo_aleatorio)  
        #depositar aneis
        funcao_acao(1248, 1256, 437, 450)
        pyautogui.click() 
        i= i+1
#teste2()
#mostrar_coordenadas_em_tempo_real()

def inicio():
    tempo_aleatorio = random.uniform(6, 10)
    time.sleep(tempo_aleatorio)
    cod = ['F', 'e', 'l', 'i', 'p', 'e', '1', '8']
    funcao_acao(713, 772, 304, 314)
    pyautogui.click()
    tempo_aleatorio = random.uniform(0.5, 1.5)
    time.sleep(tempo_aleatorio)
    for i in range(8):
        pyautogui.press(cod[i])
        tempo_aleatorio = random.uniform(0.1, 0.5)
        time.sleep(tempo_aleatorio)
    pyautogui.press('enter')
    tempo_aleatorio = random.uniform(20, 25)
    time.sleep(tempo_aleatorio)
    funcao_acao(618, 724, 333, 344)
    pyautogui.click()
    tempo_aleatorio = random.uniform(1, 2)
    time.sleep(tempo_aleatorio)
    pyautogui.press('c')
    tempo_aleatorio = random.uniform(1, 2)
    time.sleep(tempo_aleatorio)
    pyautogui.press('c')
    safespot()


def fim():
    funcao_acao(1314, 1324, 25, 35)
    pyautogui.click()
    tempo_aleatorio = random.uniform(1, 1.5)
    time.sleep(tempo_aleatorio)
    funcao_acao(1201, 1266, 643, 646)
    pyautogui.click()

def acao():
    #repeticao(coordenadas_amuleto_esmeralda, 1000)
    fim()
    
    inicio()
    repeticao(coordenadas_amuleto_ruby, 1300)
    fim()
    inicio()
    repeticao(coordenadas_anel_safira, 1300)
    repeticao(coordenadas_amuleto_esmeralda, 1000)
    fim()
    inicio()
    repeticao(coordenadas_amuleto_ruby, 2500)
    fim()
    
acao()

#mostrar_coordenadas_em_tempo_real()
#inicio()
#693, 695, 359, 372
#time.sleep(1)
#pyautogui.moveTo(693, 359)
#pyautogui.moveTo(695, 359)
#pyautogui.moveTo(693, 372)
#pyautogui.moveTo(695, 372)