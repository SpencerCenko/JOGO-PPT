"""
Projeto jogo pedra-papel-tesoura
Data: 13/08/2024
Autor: Spencer Cenko
"""

# Bibliotecas
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT #importa funções do arquivo modules.py
from ppt import startPPT, playPPT #importa funções do arquivo ppt.py
from parimpar import startParImpar
# Constantes, Variáveis e Listas
# Funções

# Main
msgs = ["seja bem-vindo aos Jogos", "PEDRA-PAPEL-TESOURA", "PAR OU ÍMPAR"]
displayHeader(msgs)
msgs = ["Digite 0 --> sair", "Digite 1 --> Pedra-Papel-Tesoura", "Digite 2 --> Par ou ímpar"]
displayHeaderT(msgs)
opUser = getUserOption("Sua Escolha")
while not validateUserOption(opUser, ["0", "1", "2"]):
  opUser = getUserOption("Sua escolha")
if(opUser == "1"):
  startPPT() #começa ppt
elif (opUser == "2"):
  startParImpar()
else:
  displayMsg("Até a Próxima")
  
