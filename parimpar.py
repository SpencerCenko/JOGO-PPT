"""
Jogo do Par ou Impar
20/08/2024
Autor: Spencer Cenko
"""


# bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT #importa funções do arquivo modules.py
from random import randint #importa o randint de random
# constante, variáveis e listas
from time import sleep
msgsInicio = ["Seja bem vindo ao", "jogo do Par ou Impar", "desenvolvido por: Spencer Cenko", "Boa sorte"] 
msgs = []
#define a constante de mensagem do inicio
playAgain = "" #define a variável playagain
playerScore = 0 #pontos do player
computerScore = 0 #pontos do com
# funções
def displayScore(typeScore, playerScore, computerScore): #define a função displayScore com 3 argumentos
  msgs = []
  msgs.append(typeScore)
  msgs.append(f"Player:  {playerScore} --- PC: {computerScore}")
  displayHeaderT(msgs)
def determineWinner(playerJog, computerJog): #define a função determinewinner com 2 argumentos
  result = "" #define a variavel result
  juncaonum = playerJog + computerJog

  if (juncaonum % 2 == 0): #testa a resposta do usuario, por exemplo, se a do player for 0 e a do computador for 2 o resultado é voce ganhou e assim para os outros que foram definidos
    result = "Você Ganhou!" #resulta é você ganhou
  else: #se não
    result = "Você Perdeu!" #resultado você perdeu
  msgs = ["Jogada do Player: ", {playerJog}, "Jogada do PC: ", {computerJog} , result] #define as msgs
  displayHeaderT(msgs) #coloca as msgs no displayHeader
  return result #retorna o result

def startParImpar(): #define a função startPPT
  while(True): #se for verdade
    playPPT()
    clrScreen() #chama a função clrscreen
    displayHeader(msgsInicio) #chama a função displayHeader com a mensagem de inicio dentro dela
    playAgain = getUserOption("Deseja jogar novamente [s/n]") #define que a constante playagain pergunta para o usuário se ele deseja jogar novamente e abre possibilidade dele responder
    while not validateUserOption(playAgain, ["s", "n", "S", "N"]): #enquanto a opção do usurio não for validada pela validateuseroption
      playAgain = getUserOption("Deseja jogar novamente [s/n]") #pergunta se deseja jogar novamente e abre a opção para o usuario responder
    if playAgain.lower() != "s": #se playagain for diferente de s
      break #interrompe a repetição

def displayMenu(): #define o displayMenu
    msgs = ["Escolha:", "[0] --> Par", "[1] --> Impar"] #define as msgs
    displayLine() #abre uma linha
    for msg in msgs: #
      displayMsg(msg) #coloca msg em displaymsg
      displayLine() #abre uma linha
def playPPT(): #define
  playerScore = 0 #PONTUAÇÃO JOGADOR
  computerScore = 0 #PONTUAÇÃO PC
  while playerScore < 2 and computerScore < 2: #enquanto score do pc e jogar for abaixo de 2
     displayMenu() #chama display menu
     playerChoice = getUserOption("Sua Escolha") #atribui a sua resposta a playerchoice
     while not validateUserOption(playerChoice, ["0", "1"]): #enquanto não validar a opção do player como o e 1
       displayMenu() #chama o menu
       playerChoice = getUserOption("Sua Escolha") #atribui a sua resposta a playerchoice

  playerJog = int(input("escolha seu número de 1 a 9")) #atribui a sua resposta a playerchoice
  computerJog = randint(1, 9) #escolhe um numero de 1 a 9
  result = determineWinner(playerJog, computerJog) #determina o vencedor entre player jogo e computerjog
  if "Ganhou" in result: #se ganhou no resultado
    playerScore += 1 #pontuação do jogador aumenta em 1
  elif "Perdeu" in result: #se perdeu no resultado
    computerScore += 1 #pontuação do computador aumenta em 1
  if playerScore < 2 and computerScore < 2: #se pontuação do jogador e do pc for menor que 2
    displayScore("PLACAR", playerScore, computerScore) #mostra a pontuação
  sleep(1) #espera um segundo por linha
  displayScore("PLACAR FINAL", playerScore, computerScore) #mostra o placar final
  if playerScore > computerScore: #se pontuação do jogador for maior que do pc
    displayHeaderT(["Parabéns", "YOU WIN!"]) #diz que você venceu
  else: #se não
    displayHeader(["Parabéns", "YOU LOSE!"]) #diz que você perdeu
# main
