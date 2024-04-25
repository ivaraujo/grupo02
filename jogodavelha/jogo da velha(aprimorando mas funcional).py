velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
import random #quando for usar a maquina pra jogar
import os
import time
jogadas = 1
tentadenovo = 0
menu = 0
def limparjogo(jvelha):
    jvelha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for i in range (3):
        jvelha[i][i] = " "
        jvelha[0][i] = " "
        jvelha[i][0] = " "
        jvelha[1][i] = " "
        jvelha[i][1] = " "
        jvelha[2][i] = " "
        jvelha[i][2] = " "
    return jvelha
    #fazer retornar o jogo limpo pra poder jogar denovo

def sorteajogada():
    x = random.randint(1,2)
    if x == 1:
        j1 = True
        j2 = False
    if x == 2:
        j2 = True
        j1 = False
    return j1,j2

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

jogadadojogador1, jogadadojogador2 = sorteajogada() #soreteia o jogador q começa
while menu == 0: #ativação do menu
    mantemmenu = 0
    print("|Bem-Vindo|")
    print("|Ao|")
    print("|Jogo da Velha| \n")
    print("---Carregando---")
    time.sleep(1.5)
    os.system('cls')
    for i in range (3):
        print(".")
        time.sleep(1.5)
    os.system('cls')
    while mantemmenu == 0 or irpromenu == True:
        os.system('cls')
        print("---------MENU---------")
        print("|[1] - Iniciar jogo!|")
        print("|[2] - Sair. |")
        opcao = int(input("\n--->"))
        if opcao == 1:
            vitorioso = False
            irpromenu = False
            jogadas = 1
            velha = limparjogo(velha)
            while irpromenu == False:
                os.system('cls') #limpa tela
                if jogadas >= 9: #caso as jogadas acabem mostra isso
                        print("DEU VÉA!")
                        print("---------------------------------------------")
                        print("      0    1    2") #para ver as ultima modificação
                        print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
                        print("   ----------------")
                        print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])
                        print("   ----------------")
                        print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
                        print("---------------------------------------------")
                        time.sleep(5)
                        irpromenu = True
                print("      0    1    2")
                print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
                print("   ----------------")
                print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])#o visual do jogo da velha(melhorar isso :D)
                print("   ----------------")
                print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
                print("Estamos na jogada: ",jogadas)
                print("---------------------------------------------")
                if jogadadojogador1 == True:
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
                        os.system('cls')
                        print("--------------PARABÉNS JOGADOR 1--------------")
                        print("-----------------VOCÊ GANHOU------------------")
                        print("---------------------------------------------")
                        print("      0    1    2") #para ver as ultima modificação
                        print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
                        print("   ----------------")
                        print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])
                        print("   ----------------")
                        print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
                        print("---------------------------------------------")
                        time.sleep(5)
                        irpromenu = True
                elif jogadadojogador2 == True:
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
                        os.system('cls')
                        print("--------------PARABÉNS JOGADOR 2--------------")
                        print("-----------------VOCÊ GANHOU------------------")
                        print("---------------------------------------------")
                        print("      0    1    2") #para ver as ultima modificação
                        print("0:  ",velha[0][0]," | ",velha[0][1]," | ",velha[0][2])
                        print("   ----------------")
                        print("1:  ", velha[1][0]," | ",velha[1][1]," | ",velha[1][2])
                        print("   ----------------")
                        print("2:  ",velha[2][0]," | ",velha[2][1]," | ",velha[2][2])
                        print("---------------------------------------------")
                        time.sleep(5)
                        irpromenu = True
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
        elif opcao == 2:
            print("saiu do jogo.")
            menu = 1
            break
        else:
            print("digite uma opçao valida!")