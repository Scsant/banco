# ESSE SCRIPT PREENCHE O DIA DE HOJE

import tkinter as tk
import pyautogui
import time
import pyperclip
from datetime import datetime, timedelta

#mudata = "25/09/2024"



mudata = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
renderPage = 5





def verificar_e_executar():
    
    # Verifica se é dia de folga para motoristas com a letra fornecida
    escala_folga = entrada_folga.get().strip().upper()  # A variável deve conter o valor A, B ou C, garantimos que esteja em maiúscula e sem espaços

    for _ in range(580):
        

        # Verificar marcações
        pyautogui.moveTo(x=328, y=693, duration=1)
        

       
        pyautogui.mouseDown(button='left')
        # Mover para o fim do texto para selecioná-lo
        pyautogui.moveTo(x=464, y=692)

        # Soltar o botão do mouse para concluir a seleção
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        inserir_marcacoes = pyperclip.paste()
        
        if "Inserir marcações" not in inserir_marcacoes:
            pyautogui.click(x=105, y=275, duration=1) 
            time.sleep(renderPage)
            continue
        
                # Verificar afastados        
        pyautogui.moveTo(x=710, y=696, duration=0.5)
        
        pyautogui.mouseDown(button='left')

        # Mover para o fim do texto para selecioná-lo
        pyautogui.moveTo(x=816, y=696)

        # Soltar o botão do mouse para concluir a seleção
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        afast = pyperclip.paste()
       
        if "Afastamento" in afast:
            pyautogui.click(x=105, y=275, duration=0.5) 
            time.sleep(6)
            continue  
        
        pyautogui.scroll(500)
        time.sleep(2)
        pyautogui.click(x=1274, y=334)
        time.sleep(2)
        # Clique para selecionar o texto da escala
        pyautogui.click(x=796, y=368, clicks=7)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)  # Aguarda o texto ser copiado para a área de transferência
        
        # Ler o texto da área de transferência
        texto_copiado = pyperclip.paste()
        
            # Verifica se é dia de folga para motoristas com a letra "A"
        if  f" {escala_folga}" in texto_copiado or "513 - 4x2 adm rural a" in texto_copiado or "564 - 4x2 adm rural f" in texto_copiado or "516 - 4x2 adm rural d" in texto_copiado or "603 - MOT 4x2 - 02:00 x 11:00 A" in texto_copiado or "731 - 4x2 19:00 x 04:48 A" in texto_copiado or "608 - MOT 4x2 - 14:00 x 23:00 A" in texto_copiado or "627 - 6x4 B - Linha II" in texto_copiado or "501 - Adm papeleiro_M" in texto_copiado or "505 - Adm rural/trans comp" in texto_copiado or "19:00 x 04:48 D" in texto_copiado or " 02:00 x 11:00 C" in texto_copiado or "606 - MOT 4x2 - 14:00 x 23:00 B" in texto_copiado or "607 - MOT 4x2 - 14:00 x 23:00 C" in texto_copiado or "604 - MOT 4x2 - 02:00 x 11:00 B" in texto_copiado or "732 - 4x2 19:00 x 04:48 B" in texto_copiado or "563 - 4x2 adm rural e" in texto_copiado or "733 - 4x2 19:00 x 04:48 C" in texto_copiado or "501 - Adm papeleiro_M" in texto_copiado or "733 - 4x2 19:00 x 04:48 C" in texto_copiado:
            print("Hoje é dia de folga para este motorista:", texto_copiado)
            pyautogui.click(x=105, y=275, duration=0.5) 
            time.sleep(6)
            continue  # Pula para o próximo, não executa mais código abaixo
            


        # Rolar a tela para baixo333333333333333333
        #pyautogui.scroll(-600)
        pyautogui.click(x=379, y=694, duration=0.5)
        time.sleep(3)

        # Verifica o conteúdo copiado e chama a função correspondente
        if "MOT 4x2 - 02:00 x 14:00 A" in texto_copiado or "MOT 4x2 - 02:00 x 14:00 B" in texto_copiado or "MOT 4x2 - 02:00 x 14:00 C" in texto_copiado:
            horario_inicial = entrada_02.get().strip()
            dois(horario_inicial)   
        elif "MOT 4X2 - 04:00 X 16:00 C" in texto_copiado or "MOT 4X2 - 04:00 X 16:00 B" in texto_copiado or "MOT 4X2 - 04:00 X 16:00 A" in texto_copiado:
            horario_inicial = entrada_04.get().strip()
            quatro(horario_inicial)
        elif "MOT 4x2 - 06:00 x 18:00 A" in texto_copiado or "MOT 4x2 - 06:00 x 18:00 B" in texto_copiado or "MOT 4x2 - 06:00 x 18:00 C" in texto_copiado:
            horario_inicial = entrada_06.get().strip()
            seis(horario_inicial)
        elif "MOT 4X2 - 08:00 X 20:00 A" in texto_copiado or "MOT 4X2 - 08:00 X 20:00 B" in texto_copiado or "MOT 4X2 - 08:00 X 20:00 C" in texto_copiado:
            horario_inicial = entrada_08.get().strip()
            oito(horario_inicial)
        elif "MOT 4X2 - 10:00 X 22:00 B" in texto_copiado or "MOT 4X2 - 10:00 X 22:00 C" in texto_copiado or "MOT 4X2 - 10:00 X 22:00 A" in texto_copiado:
            horario_inicial = entrada_10.get().strip()
            dez(horario_inicial)
        elif "MOT 4x2 - 14:00 x 02:00 A" in texto_copiado or "MOT 4x2 - 14:00 x 02:00 B" in texto_copiado or "MOT 4x2 - 14:00 x 02:00 C" in texto_copiado:
            horario_inicial = entrada_14.get().strip()
            quatorze(horario_inicial)               
        elif "MOT 4x2 - 16:00 x 04:00 A" in texto_copiado or "MOT 4x2 - 16:00 x 04:00 B" in texto_copiado or "MOT 4x2 - 16:00 x 04:00 C" in texto_copiado:
            horario_inicial = entrada_16.get().strip()
            dezesseis(horario_inicial)
        elif "MOT 4X2 - 18:00 X 06:00 A" in texto_copiado or "MOT 4X2 - 18:00 X 06:00 B" in texto_copiado or "757 - MOT 4X2 - 18:00 X 06:00 C" in texto_copiado:
            horario_inicial = entrada_18.get().strip()
            dezoito(horario_inicial)
        elif "MOT 4X2 - 20:00 X 08:00 A" in texto_copiado or "MOT 4X2 - 20:00 X 08:00 B" in texto_copiado or "20:00 X 08:00 C" in texto_copiado:
            horario_inicial = entrada_20.get().strip()
            vinte(horario_inicial)
        elif "MOT 4X2 - 22:00 X 10:00 A" in texto_copiado or "MOT 4X2 - 22:00 X 10:00 B" in texto_copiado or "MOT 4X2 - 22:00 X 10:00 C" in texto_copiado:
            horario_inicial = entrada_22.get().strip()
            vinteDois(horario_inicial)
         
        else:
            print("Escala não reconhecida: ", texto_copiado)


def calcular_horarios(horario_inicial_str):
    formato_horario = "%H:%M"
    horario_inicio = datetime.strptime(horario_inicial_str, formato_horario)

    pausa = timedelta(hours=3, minutes=52)
    duracao_pausa = timedelta(hours=1)
    duracao_jornada = timedelta(hours=11, minutes=59)

    horario_pausa_inicio = horario_inicio + pausa
    horario_pausa_fim = horario_pausa_inicio + duracao_pausa
    horario_fim_jornada = horario_inicio + duracao_jornada

    horario_inicio_str = horario_inicio.strftime("%H%M")
    horario_pausa_inicio_str = horario_pausa_inicio.strftime("%H%M")
    horario_pausa_fim_str = horario_pausa_fim.strftime("%H%M")
    horario_fim_str = horario_fim_jornada.strftime("%H%M")
    
        # Sua lógica de cálculo de horários
    print(f"Horário inicial: {horario_inicial_str}")
    print(f"Horário de pausa início: {horario_pausa_inicio_str}")
    print(f"Horário de pausa fim: {horario_pausa_fim_str}")
    print(f"Horário de fim: {horario_fim_str}")
    return horario_inicio_str, horario_pausa_inicio_str, horario_pausa_fim_str, horario_fim_str


def dois(horario_inicial):
    # Recebe o horário inicial e verifica se está vazio
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)

        # Lógica de automação para 4:00 X 16:00 (ou horário inicial fornecido)
        pyautogui.click(x=311, y=348, clicks=4)
        time.sleep(1.5)
        
        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=380, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)



        # Continue a lógica de automação se necessário...
        # Você pode incluir a lógica de salvar, rolar a tela, etc.

    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
    #Hora a mais do feriado!!
    # pyautogui.click(x=389, y=597, duration=0.7)
    # pyautogui.write("1200")
    
    # pyautogui.click(x=388, y=631, duration=0.7)
    # pyautogui.write("1300")
    time.sleep(1)
    
    
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(2)
    #Botão Salvar
    pyautogui.click(x=1104, y=674)
     
    
    time.sleep(4)
    
    pyautogui.scroll(1500)
    time.sleep(2)
    pyautogui.click(x=105, y=275)
    time.sleep(6)


def quatro(horario_inicial):
    # Recebe o horário inicial e verifica se está vazio
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)

        # Lógica de automação para 4:00 X 16:00 (ou horário inicial fornecido)
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5)
        
        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)


        # Continue a lógica de automação se necessário...
        # Você pode incluir a lógica de salvar, rolar a tela, etc.

    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
    #Hora a mais do feriado!!
    # pyautogui.click(x=389, y=597, duration=0.7)
    # pyautogui.write("1200")
    
    # pyautogui.click(x=388, y=631, duration=0.7)
    # pyautogui.write("1300")
    time.sleep(3)
    
    
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)
    #Botão Salvar
    pyautogui.click(x=1104, y=674)
     
    
    time.sleep(6)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(6)
def seis(horario_inicial):
    
    
        # Recebe o horário inicial e verifica se está vazio
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:00
        
        
        
        
       # 6:00 X 18:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 
        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        
        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("1410")
        # #time.sleep(1)
        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("1510")
        #time.sleep(1)
    
    except ValueError as e:
            print(f"Erro ao calcular horários: {e}")
    
       
  
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)

    pyautogui.click(x=1104, y=674)
     
    
    time.sleep(5)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(renderPage)
def oito(horario_inicial): 
    
  
    
        # Recebe o horário inicial e verifica se está vazio
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:00
        
        
        
        
       # 6:00 X 18:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 
        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        
        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("1410")
        # #time.sleep(1)
        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("1510")
        #time.sleep(1)
    
    except ValueError as e:
            print(f"Erro ao calcular horários: {e}")
    
       
  
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)

    pyautogui.click(x=1104, y=674)
     
    
    time.sleep(5)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(renderPage)
def dez(horario_inicial):
    
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:0
    
        # 10:00 X 22:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 
        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        
    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)

    pyautogui.click(x=1104, y=674)
    
     
    
    time.sleep(6)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(6)


def quatorze(horario_inicial):
    
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:0
        
    
        #mudata = "18/04/2024"
        # 16:00 X 4:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 


        pyautogui.click(x=328, y=557, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)


        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

            
        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("2115")

        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("2215")
        time.sleep(3)
    
    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
       
         
             
  
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)
    
    pyautogui.click(x=1104, y=674)
    time.sleep(1)
    
    pyautogui.scroll(600)
    

    
    time.sleep(3)
    
    pyautogui.scroll(1500)
    time.sleep(1)
    pyautogui.click(x=105, y=275)
    time.sleep(6)



def dezesseis(horario_inicial):
    
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:0
        
    
        #mudata = "18/04/2024"
        # 16:00 X 4:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 


        pyautogui.click(x=328, y=557, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)


        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        
            
        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("2115")

        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("2215")
        time.sleep(1)
    
    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
       
         
             
  
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)
    
    pyautogui.click(x=1104, y=674)
    time.sleep(1)
    
    pyautogui.scroll(600)
    

    
    time.sleep(6)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(6)
def dezoito(horario_inicial):
    
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:0
        
        #mudata = "18/04/2024"
        # 18:00 X 6:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 


        pyautogui.click(x=328, y=557, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)

        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("2259")

        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("2359")
        time.sleep(1)
    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
       
         
              
  
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)

    pyautogui.click(x=1104, y=674)
    
    
    time.sleep(6)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(6)
def vinte(horario_inicial):
    
    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    
    # Calcula os outros horários (início, pausa e fim) com base no horário inicial
    horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
    # Sua lógica de automação para 6:00 X 18:0
    
    #mudata = "18/04/2024"
    # 20:00 X 8:00
    pyautogui.click(x=309, y=347, clicks=4)
    time.sleep(1.5) 


    pyautogui.click(x=328, y=557, duration=0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(mudata)

    pyautogui.click(x=337, y=524, duration=0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(mudata) 

    
    # pyautogui.click(x=337, y=597, duration=0.5)
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.write(mudata)


    # pyautogui.click(x=333, y=631, duration=0.5)
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.write(mudata)


    # Inserir horário de início
    pyautogui.click(x=379, y=453, duration=0.1)
    pyautogui.write(horario_inicio)
    time.sleep(1)
    pyautogui.click(x=379, y=491, duration=0.1)
    pyautogui.write(horario_pausa_inicio)
    time.sleep(1)
    pyautogui.click(x=379, y=524, duration=0.1)
    pyautogui.write(horario_pausa_fim)
    time.sleep(1)
    pyautogui.click(x=379, y=559, duration=0.1)
    pyautogui.write(horario_fim)
    time.sleep(1)

    
    # pyautogui.click(x=389, y=597, duration=0.7)
    # pyautogui.write("139")

    # pyautogui.click(x=389, y=631, duration=0.7)
    # pyautogui.write("239")
    time.sleep(1)

    
       
         
          
    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)

    pyautogui.click(x=1104, y=674)
    time.sleep(4)
    
    pyautogui.scroll(1500)
    time.sleep(1)
    pyautogui.click(x=105, y=275)
    time.sleep(2)
    
def vinteDois(horario_inicial):

    if not horario_inicial:
        print("Horário inicial não fornecido.")
        return

    try:
        # Calcula os outros horários (início, pausa e fim) com base no horário inicial
        horario_inicio, horario_pausa_inicio, horario_pausa_fim, horario_fim = calcular_horarios(horario_inicial)
        # Sua lógica de automação para 6:00 X 18:0
        
        #mudata = "18/04/2024"
        # 20:00 X 8:00
        pyautogui.click(x=309, y=347, clicks=4)
        time.sleep(1.5) 


        pyautogui.click(x=328, y=557, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)
        
        pyautogui.click(x=337, y=524, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)    
        
        pyautogui.click(x=333, y=491, duration=0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(mudata)
        
        # pyautogui.click(x=337, y=597, duration=0.5)
        # pyautogui.hotkey('ctrl', 'a')
        # pyautogui.write(mudata)


        # pyautogui.click(x=333, y=631, duration=0.5)
        # pyautogui.hotkey('ctrl', 'a')
        # pyautogui.write(mudata)

        # Inserir horário de início
        pyautogui.click(x=379, y=453, duration=0.1)
        pyautogui.write(horario_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=491, duration=0.1)
        pyautogui.write(horario_pausa_inicio)
        time.sleep(1)
        pyautogui.click(x=379, y=524, duration=0.1)
        pyautogui.write(horario_pausa_fim)
        time.sleep(1)
        pyautogui.click(x=379, y=559, duration=0.1)
        pyautogui.write(horario_fim)
        time.sleep(1)

        # pyautogui.click(x=389, y=597, duration=0.7)
        # pyautogui.write("139")

        # pyautogui.click(x=389, y=631, duration=0.7)
        # pyautogui.write("239")
        time.sleep(1)
        
    except ValueError as e:
        print(f"Erro ao calcular horários: {e}")
    
       
         
          

    # Hora espera
    pyautogui.click(x=718, y=482, duration=0.5)
    pyautogui.click(x=544, y=617, duration=0.5)
    time.sleep(1.5)
    pyautogui.click(x=719, y=519, duration=0.5)
    pyautogui.click(x=559, y=437, duration=0.5)
    time.sleep(1.5)
    

    pyautogui.click(x=1104, y=674)
    time.sleep(6)
    
    pyautogui.scroll(1500)
    time.sleep(1.5)
    pyautogui.click(x=105, y=275)
    time.sleep(5)

# Interface Tkinter para pegar a escala de folga
janela = tk.Tk()
janela.title("Formulário de Apontamentos")

# Adicionando o frame para rolagem
frame_principal = tk.Frame(janela)
frame_principal.pack(fill="both", expand=True)

# Canvas para o conteúdo
canvas = tk.Canvas(frame_principal)
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame interno que será rolado
frame_conteudo = tk.Frame(canvas)

# Configuração do canvas para rolar o frame_conteudo
canvas.create_window((0, 0), window=frame_conteudo, anchor="nw")

# Função para ajustar o canvas ao tamanho do frame interno
def ajustar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Ligar o evento de redimensionamento do frame_conteudo à função ajustar_scroll
frame_conteudo.bind("<Configure>", ajustar_scroll)

# Entrada para escala de folga
label_folga = tk.Label(frame_conteudo, text="Digite a letra da folga (A, B, ou C):")
label_folga.pack(pady=5)
entrada_folga = tk.Entry(frame_conteudo, width=10)
entrada_folga.pack(pady=5)


# Entrada e botão para cada horário
# 04:00
label_02 = tk.Label(frame_conteudo, text="Horário inicial para 02:00:")
label_02.pack(pady=5)
entrada_02 = tk.Entry(frame_conteudo, width=10)
entrada_02.pack(pady=5)
botao_02 = tk.Button(frame_conteudo, text="02:00", command=dois)
botao_02.pack(pady=5)

# 04:00
label_04 = tk.Label(frame_conteudo, text="Horário inicial para 04:00:")
label_04.pack(pady=5)
entrada_04 = tk.Entry(frame_conteudo, width=10)
entrada_04.pack(pady=5)
botao_04 = tk.Button(frame_conteudo, text="04:00", command=quatro)
botao_04.pack(pady=5)

# 06:00
label_06 = tk.Label(frame_conteudo, text="Horário inicial para 06:00:")
label_06.pack(pady=5)
entrada_06 = tk.Entry(frame_conteudo, width=10)
entrada_06.pack(pady=5)
botao_06 = tk.Button(frame_conteudo, text="06:00", command=seis)
botao_06.pack(pady=5)

# 08:00
label_08 = tk.Label(frame_conteudo, text="Horário inicial para 08:00:")
label_08.pack(pady=5)
entrada_08 = tk.Entry(frame_conteudo, width=10)
entrada_08.pack(pady=5)
botao_08 = tk.Button(frame_conteudo, text="08:00", command=oito)
botao_08.pack(pady=5)

# 10:00
label_10 = tk.Label(frame_conteudo, text="Horário inicial para 10:00:")
label_10.pack(pady=5)
entrada_10 = tk.Entry(frame_conteudo, width=10)
entrada_10.pack(pady=5)
botao_10 = tk.Button(frame_conteudo, text="10:00", command=dez)
botao_10.pack(pady=5)

# 14:00
label_14 = tk.Label(frame_conteudo, text="Horário inicial para 14:00:")
label_14.pack(pady=5)
entrada_14 = tk.Entry(frame_conteudo, width=10)
entrada_14.pack(pady=5)
botao_14 = tk.Button(frame_conteudo, text="14:00", command=quatorze)
botao_14.pack(pady=5)

# 16:00
label_16 = tk.Label(frame_conteudo, text="Horário inicial para 16:00:")
label_16.pack(pady=5)
entrada_16 = tk.Entry(frame_conteudo, width=10)
entrada_16.pack(pady=5)
botao_16 = tk.Button(frame_conteudo, text="16:00", command=dezesseis)
botao_16.pack(pady=5)

# 18:00
label_18 = tk.Label(frame_conteudo, text="Horário inicial para 18:00:")
label_18.pack(pady=5)
entrada_18 = tk.Entry(frame_conteudo, width=10)
entrada_18.pack(pady=5)
botao_18 = tk.Button(frame_conteudo, text="18:00", command=dezoito)
botao_18.pack(pady=5)

# 20:00
label_20 = tk.Label(frame_conteudo, text="Horário inicial para 20:00:")
label_20.pack(pady=5)
entrada_20 = tk.Entry(frame_conteudo, width=10)
entrada_20.pack(pady=5)
botao_20 = tk.Button(frame_conteudo, text="20:00", command=vinte)
botao_20.pack(pady=5)

# 22:00
label_22 = tk.Label(frame_conteudo, text="Horário inicial para 22:00:")
label_22.pack(pady=5)
entrada_22 = tk.Entry(frame_conteudo, width=10)
entrada_22.pack(pady=5)
botao_22 = tk.Button(frame_conteudo, text="22:00", command=vinteDois)
botao_22.pack(pady=5)

# Botão para verificar a escala e executar a função correspondente
botao_executar = tk.Button(frame_conteudo, text="Verificar Escala e Executar", command=verificar_e_executar)
botao_executar.pack(pady=20)

# Iniciar o loop da interface gráfica
janela.mainloop()