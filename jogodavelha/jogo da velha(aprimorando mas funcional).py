velha = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
import random #quando for usar a maquina pra jogar
import os
jogadas = 1
tentadenovo = 0
def sorteajogada(): #fazer combinar com a funcao de baixo
    x = random.randint(1,2)
    if x == 1:
        jogadadojogador1 = True
        return jogadadojogador1
    if x == 2:
        jogadadojogador2 = True
        return jogadadojogador2

#verificação da vitoria pro jogador NUMERO 1

def verificarvitoriaO():#verificar vitoria
    vitoriaO = False
    if velha[0][0] == "O" and velha[0][1] == "O" and velha[0][2] == "O":
                vitoriaO = True
    elif velha[1][0] == "O" and velha[1][1] == "O" and velha[1][2] == "O":
                vitoriaO = True
    elif velha[2][0] == "O" and velha[2][1] == "O" and velha[2][2] == "O":
                vitoriaO = True
        #
    elif velha[0][0] == "O" and velha[1][0] == "O" and velha[2][0] == "O":
                vitoriaO = True
    elif velha[0][1] == "O" and velha[1][1] == "O" and velha[2][1] == "O":
                vitoriaO = True
    elif velha[0][2] == "O" and velha[1][2] == "O" and velha[2][2] == "O":
                vitoriaO = True
        #
    elif velha[0][0] == "O" and velha[1][1] == "O" and velha[2][2] == "O":
                vitoriaO = True
    elif velha[0][2] == "O" and velha[1][1] == "O" and velha[2][0] == "O":
                vitoriaO = True
    return vitoriaO
    
#verificação de vitoria do jogador NUMERO 2

def verificarvitoriax():#verificar vitoria
    vitoriax = False
    if velha[0][0] == "X" and velha[0][1] == "X" and velha[0][2] == "X":
                vitoriax = True
    elif velha[1][0] == "X" and velha[1][1] == "X" and velha[1][2] == "X":
                vitoriax = True
    elif velha[2][0] == "X" and velha[2][1] == "X" and velha[2][2] == "X":
                vitoriax = True
        #
    elif velha[0][0] == "X" and velha[1][0] == "X" and velha[2][0] == "X":
                vitoriax = True
    elif velha[0][1] == "X" and velha[1][1] == "X" and velha[2][1] == "X":
                vitoriax = True
    elif velha[0][2] == "X" and velha[1][2] == "X" and velha[2][2] == "X":
                vitoriax = True
        #
    elif velha[0][0] == "X" and velha[1][1] == "X" and velha[2][2] == "X":
                vitoriax = True
    elif velha[0][2] == "X" and velha[1][1] == "X" and velha[2][0] == "X":
            vitoriax = True
    return vitoriax
while jogadas <= 9: #enquanto nao atingirem o limite de jogadas vai continuar aqui
    jogadadojogador1 = True #isso decide quem joga primeiro
    jogadadojogador2 = False#isso tbm
    sorteajogada() #soreteia o jogador q começa
    os.system('cls') #limpa tela
    if jogadas <= 2:
        print("----------BEM VINDO AO JOGO DA VELHA---------")
    print("      0    1    2")
    print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
    print("   ----------------")
    print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])#o visual do jogo da velha(melhorar isso :D)
    print("   ----------------")
    print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
    print("Estamos na jogada: ",jogadas)
    print("---------------------------------------------")
    if jogadadojogador1 == True and jogadas < 9: #jogada do jogador 1
        print("--------------SUA VEZ JOGADOR 1--------------")
        print("---------------------------------------------")
        tentadenovo = 0 # variavel pra caso o usuario digite uma jogada que ja foi feita
        while tentadenovo == 0: #enquanto nao digitar a jogada correta
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if velha[linha][coluna] == " ": #se a jogada que foi inserida nao tiver ocupada...
                velha[linha][coluna] = "X" #vai marcar com o simbolo
                tentadenovo = 1 #para ele sair do laço de jogada invalida
                jogadas += 1 #contar a quantidade de jogadas que foram feitas
                jogadadojogador1 = False #termina a jogada do jogador 1
                jogadadojogador2 = True #passa a vez pro jogador 2
            else: #se a jogada for invalida repete o if
                print("Jogada invalida!")
                tentadenovo = 0
    if verificarvitoriax() == True:
        print("--------------PARABENS JOGADOR 1--------------")
        print("-----------------VOCE GANHOU------------------")
        break
    os.system('cls')
    print("---------------------------------------------")
    print("      0    1    2")
    print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
    print("   ----------------")
    print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])
    print("   ----------------")
    print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
    print("Estamos na jogada: ",jogadas)
    print("---------------------------------------------")
    if jogadadojogador2 == True and jogadas < 9:#jogada do jogador 2(basicamente a mesma coisa do jogador 1)
        print("--------------SUA VEZ JOGADOR 2--------------")
        print("---------------------------------------------")
        tentadenovo = 0
        while tentadenovo == 0:
            linha2 = int(input("Digite a linha: "))
            coluna2 = int(input("Digite a coluna: "))
            if velha[linha2][coluna2] == " ":
                velha[linha2][coluna2] = "O"
                tentadenovo = 1
                jogadas += 1
                jogadadojogador1 = True #passa a jogada para o jogador 1
                jogadadojogador2 = False #termina a jogada do jogador 2
            else:
                print("Jogada invalida!")
                tentadenovo = 0
    if verificarvitoriaO() == True:
        print("--------------PARABENS JOGADOR 2--------------")
        print("-----------------VOCE GANHOU------------------")
        break
if jogadas == 9: #caso as jogadas acabem mostra isso
    print("Deu velha!")
print("---------------------------------------------")
print("      0    1    2") #para ver as ultima modificação
print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
print("   ----------------")
print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])
print("   ----------------")
print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
print("---------------------------------------------")