"""
Arquivo de Modulos
Data: 13/08/2024
Autor: Spencer Cenko
"""

# Bibliotecas
from random import choice #importa choice da biblioteca random
from time import sleep #importa sleep de time
# Constantes, Variáveis e Listas
TAM = 50 # Tamanho da Tela
CAR = choice(["+", "*", "!"]) #constante caracteres para desenho na tela
MAR = 4 #tamanho da margem
# Funções

def clrScreen(): #função para limpar a tela
  print("\n"*TAM) # mostra na tela \n == linha * TAM

def displayLine(): #função que mostra uma linha de caracteres
  print(CAR*TAM)

def displayMsg(msg): #mostra uma msg alinhada a esquerda entre CAR
  print(f"{CAR} {msg:<{TAM-MAR}} {CAR} ") #alinha msg pra esquerda usando a variável CAR

def displayMsgCenter(msg): #função para mostrar mensagem no centro
  print(f"{CAR} {msg:^{TAM-MAR}} {CAR} ") #mostra uma mensagem alinhada no centro

def displayHeader(msgs): #função do cabeçalho
  displayLine() #usa a função de linha
  for item in msgs: #para item em mensagens
    displayMsgCenter(item) #usa a função da mensagem no centro
  displayLine() #usa a função de linha
def displayHeaderT(msgs): #função do cabeçalho
  displayLine() #usa a função de linha
  for item in msgs: #para item em mensagens
    displayMsgCenter(item) #usa a função da mensagem no centro
    sleep(1)
  displayLine() #usa a função de linha
def getUserOption(msg): #define uma função para pegar a opção do usuario
  option = input(f"{CAR} {msg}: ").strip() #pega a opção do usuario
  return option #retorna a opção

def validateUserOption(option, listOptions): #valida a opção do usuario com base na lista de opções
  if option in listOptions: # se a opção estiver na lista de opções
    return True #retorna True
  else: #se não
    msgsErro = ["Opção Inválida!", "Escolha Novamente..."] #mostra a mensagem de erro
    displayHeader(msgsErro) #chama a função displayheader com a mensagem de erro dentro
    return False #retorna false
# Main