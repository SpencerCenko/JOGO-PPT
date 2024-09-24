"""
Jogo do Pedra-Papel-Tesoura
13/08/2024
Autor: Spencer Cenko
"""

# bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT #importa funções do arquivo modules.py
from random import randint #importa o randint de random
# constante, variáveis e listas
from time import sleep
msgsInicio = ["Seja bem vindo ao", "jogo do PEDRA-PAPEL-TESOURA", "desenvolvido por: Spencer Cenko", "Boa sorte"] 
msgs = []
#define a constante de mensagem do inicio
playAgain = "" #define a variável playagain
playerScore = 0
computerScore = 0
# funções
def displayScore(typeScore, playerScore, computerScore): #define a função displayScore com 3 argumentos
  msgs = []
  msgs.append(typeScore)
  msgs.append(f"Player:  {playerScore} --- PC: {computerScore}")
  displayHeaderT(msgs)
def determineWinner(playerChoice, computerChoice): #define a função determinewinner com 2 argumentos
  play = "" #define a variavel play
  result = "" #define a variavel result
  choices = ["PEDRA", "PAPEL", "TESOURA"] #define as escolhas pedra, papel e tesoura
  playerChoiceStr = choices[int(playerChoice)] #transforma choices em inteiro e associa a playerchoicestr
  computerChoiceStr = choices[int(computerChoice)] #transforma choices em inteiro e associa a computerchoicestr
  if playerChoice == computerChoice: #se player choice for igual a computer choice
    result = "Empate!" #define o resultado como empate
  elif (playerChoice == "0" and computerChoice == "2") or (playerChoice == "1" and computerChoice == "0") or (playerChoice == "2" and computerChoice == "1"): #testa a resposta do usuario, por exemplo, se a do player for 0 e a do computador for 2 o resultado é voce ganhou e assim para os outros que foram definidos
    play = f"{playerChoiceStr} vence {computerChoiceStr}" #player vence computador
    result = "Você Ganhou!" #resulta é você ganhou
  else: #se não
    play = f"{computerChoiceStr} vence {playerChoiceStr}" #computador vence player
    result = "Você Perdeu!" #resultado você perdeu
  msgs = ["Jogada do Player: " + playerChoiceStr, "Jogada do PC: " + computerChoiceStr, play, result] #define as msgs
  displayHeaderT(msgs) #coloca as msgs no displayHeader
  return result #retorna o result
  
def startPPT(): #define a função startPPT
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
    msgs = ["Escolha:", "[0] --> Pedra", "[1] --> Papel", "[2] --> Tesoura"] #define as msgs
    displayLine() #abre uma linha
    for msg in msgs: #
      displayMsg(msg) #coloca msg em displaymsg
      displayLine() #abre uma linha
def playPPT(): #define o playPPT
  playerScore = 0 #define o playscore como 0
  computerScore = 0 #define o computerscore com 0
  while playerScore < 2 and computerScore < 2: #enquanto playerscore e computerscore forem menores que 2
     displayMenu() #chama a função displayMenu
     playerChoice = getUserOption("Sua Escolha") #pega sua escolha e armazena em playerChoice
     while not validateUserOption(playerChoice, ["0", "1", "2"]): #enquanto não validar a opção do usuario com 0 1 e 2
       displayMenu() #chama display menu
       playerChoice = getUserOption("Sua Escolha") #pega sua escolha
     computerChoice = str(randint(0, 2)) #define a escolha do computador
     result = determineWinner(playerChoice, computerChoice) #armazena o vencedor em result
     if "Ganhou" in result: #se ganhou em result
      playerScore += 1 #player score aumenta 1
     elif "Perdeu" in result: #se perdeu no resultado
      computerScore += 1 #computerscore ganha 1
     if playerScore < 2 and computerScore < 2: #se playerscore e computerscore forem menores que 2
      displayScore("PLACAR", playerScore, computerScore) #mostra o placar com os pontos
     sleep(1) #demora um segundo por linha
  displayScore("PLACAR FINAL", playerScore, computerScore) #mostra o placar
  if playerScore > computerScore: #se playerscore for maior que computerscore
    displayHeaderT(["Parabéns", "YOU WIN!"]) #mostra essa mensagem
  else:#se não
    displayHeader(["Parabéns", "YOU LOSE!"]) #mostra essa mensagem
# main
