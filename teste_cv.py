import cv2
import pyautogui
import numpy as np
import time
import random



#mover_mouse_rota_aleatoria(novo_x, novo_y, 10, 30)

def cortar_arvore():
    print('aoba')
    time.sleep(4)
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    madeira_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\madeira.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, madeira_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias >= 26:
        print("Dropar! O atalho foi encontrado", quantidade_ocorrencias, "vezes.")
    else:
        print('cortar!')
        arvore_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\objeto2.png')
        procurar_arvore=cv2.matchTemplate(screenshot_cv, madeira_img, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(procurar_arvore)
        x, y = max_loc
        quantidade_ocorrencias = np.sum(procurar_arvore >= 0.9)  # Defina um threshold adequado
        if quantidade_ocorrencias > 0:
            largura, altura = arvore_img.shape[1], arvore_img.shape[0]
            centro_x = x + largura // 2
            centro_y = y + altura // 2
            x_min = centro_x - 7
            x_max = centro_x + 7
            y_min = centro_y - 7
            y_max = centro_y + 7

            funcao_acao(x_min, x_max, y_min, y_max)

            # Mover o mouse para o centro do retângulo delimitador
            #pyautogui.moveTo(centro_x, centro_y, duration=0.5)







def teste2():
    time.sleep(4)
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    atalho_img = cv2.imread('C:\\Users\\Suiany\\Documents\\python project\\madeira.png')  # Carregar a imagem em escala de cinza
    resultado=cv2.matchTemplate(screenshot_cv, atalho_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)
    x, y = max_loc


    # Contar o número de ocorrências do atalho
    quantidade_ocorrencias = np.sum(resultado >= 0.9)  # Defina um threshold adequado
    if quantidade_ocorrencias >= 4:
        print("Dropar! O atalho foi encontrado", quantidade_ocorrencias, "vezes.")
    else:
        print("Continuar! O atalho foi encontrado apenas", quantidade_ocorrencias, "vezes.")





    # Calcular as coordenadas do centro do retângulo delimitador
    largura, altura = atalho_img.shape[1], atalho_img.shape[0]
    centro_x = x + largura // 2
    centro_y = y + altura // 2

    # Mover o mouse para o centro do retângulo delimitador
    pyautogui.moveTo(centro_x, centro_y, duration=0.5) 

    # Desenhar o retângulo delimitador na captura de tela
    atalho_width, atalho_height = atalho_img.shape[1], atalho_img.shape[0]
    top_left = max_loc
    botton_right = (top_left[0] + atalho_width, top_left[1] + atalho_height)
    cv2.rectangle(screenshot_cv, top_left, botton_right, (0, 255, 0), 2)

    cv2.imshow('Captura de Tela com Atalho Marcado', screenshot_cv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#teste2()


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

teste2()