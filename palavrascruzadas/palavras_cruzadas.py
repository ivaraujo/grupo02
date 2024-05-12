import random
import time
import os

#FUNÇÕES
def sortearCenario(): #SORTEADOR DE CENÁRIO
    n = random.choice([1,2,3,4])
    print(f"Cenário: {n}")
    return n

def verificaPalavra(novaMatriz,vetor,n_sorteado,l):
    # CENÁRIOS
    #n_sorteado = 4
    cenario1 = [[" "," ","3"," ","2"],[" "," ","M"," ","V"],["1","C","A","J","A"],[" "," ","Ç"," ","S"],[" "," ","Ã"," ","O"]]
    cenario2 = [[" "," ","1"," "," "],[" "," ","C"," "," "],["3","M","A","Ç","Ã"],[" "," ","J"," "," "],["2","V","A","S","O"]]
    cenario3 = [[" "," ","1"," "," "],[" "," ","C"," "," "],["2","V","A","S","O"],[" "," ","J"," "," "],["3","M","A","Ç","Ã"]]
    cenario4 = [[" "," ","2"," ","3"],[" "," ","V"," ","M"],["1","C","A","J","A"],[" "," ","S"," ","Ç"],[" "," ","O"," ","Ã"]]
    v = 0
    x = 0
    y = 0    
    
    if(n_sorteado == 1):
        for x in range(5):
            v = 0
            for y in range(5):
                for v in range(len(vetor)):
                    if(vetor[v] == cenario1[x][y]):
                        if(vetor[0] == "V"):
                            novaMatriz[x][2] = vetor[v]
                        elif(vetor[0] == "M"):
                            novaMatriz[x][4] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 2):
        for x in range(5):
            v = 0
            for y in range(5):
                for v in range(len(vetor)):
                    if(vetor[v] == cenario2[x][y]):
                        if(vetor[0] == "V"):
                            novaMatriz[4][y] = vetor[v]
                        elif(vetor[0] == "M"):
                            novaMatriz[2][y] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 3):
        for x in range(5):
            v = 0
            for y in range(5):
                for v in range(len(vetor)):
                    if(vetor[v] == cenario3[x][y]):
                        if(vetor[0] == "M"):
                            novaMatriz[4][y] = vetor[v]
                        elif(vetor[0] == "V"):
                            novaMatriz[2][y] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 4):
        #print(novaMatriz)
        for x in range (5):
            v = 0
            for y in range(5):
                for v in range(4):
                    if(cenario4[x][y] == vetor[v]):
                        #print(f"X: {x} Y: {y} V: {v}")
                        if(vetor[0] == "M"):
                            novaMatriz[x][4] = vetor[v]
                        elif(vetor[0] == "V"):
                            novaMatriz[x][2] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]    
                        l+=1
    return novaMatriz, l

def jogar(n_sort):
    #n_sort = 4
    
    if(n_sort == 1):
        cPalav = [[" "," ","3"," ","2"],[" "," ","-"," ","-"],["1","-","-","-","-"],[" "," ","-"," ","-"],[" "," ","-"," ","-"]]
    if(n_sort == 2):
        cPalav = [[" "," ","1"," "," "],[" "," ","-"," "," "],["3","-","-","-","-"],[" "," ","-"," "," "],["2","-","-","-","-"]]
    if(n_sort == 3):
        cPalav = [[" "," ","1"," "," "],[" "," ","-"," "," "],["2","-","-","-","-"],[" "," ","-"," "," "],["3","-","-","-","-"]]
    if(n_sort == 4):
        cPalav = [[" "," ","2"," ","3"],[" "," ","-"," ","-"],["1","-","-","-","-"],[" "," ","-"," ","-"],[" "," ","-"," ","-"]]
    
    for i in range(5): #EXIBIR JOGO ATUAL
        for j in range(5):
            if(cPalav[i][j] != " "):
                if(cPalav[i][j] == "1" or cPalav[i][j] == "2" or cPalav[i][j] == "3"):
                    print(f"\033[30;40m {cPalav[i][j]} \033[m", end="")
                else:                
                    print(f"\033[31;41m {cPalav[i][j]} \033[m", end="")
            else:            
                print(f" {cPalav[i][j]} ", end="")
        print()
    loop = 0
    while (True):
        #print("Loop:",loop)
        if(loop > 15):
            print()
            print("PARABÉNS! VOCÊ TERMINOU!")
            print()
            break
        print()
        #print(f"Cenário: {sortearCenario()}")
        print("| ++ Dicas ++ |")        
        print("1º palavra -> É uma fruta que tem uma polpa suculenta de sabor relativamente azedo e uma grande semente.")
        print("2º palavra -> É utilizado para diversos tipos de coisas, desde guardar itens de casa até decorações. Geralmente reutilizado para guardar diversas coisas")
        print("3º palavra -> É uma fruta crocante ao dar uma mordida. E sua textura é macia por dentro.\n")
        palavra = input("Digite a palavra: ")        
        vet_palavra = list(palavra.upper())
        if(os.name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        nMatriz, loop = verificaPalavra(cPalav, vet_palavra, n_sort, loop)
        for i in range(5): #EXIBIR JOGO ATUAL
            for j in range(5):
                if(nMatriz[i][j] != " "):
                    if(nMatriz[i][j] == "1" or nMatriz[i][j] == "2" or nMatriz[i][j] == "3"):
                        print(f"\033[30;40m {nMatriz[i][j]} \033[m", end="")
                    else:                
                        print(f"\033[0;31;41m {nMatriz[i][j]} \033[m", end="")
                else:            
                    print(f" {nMatriz[i][j]} ", end="")
            print()   
# MENU
while True:
    sorteado = sortearCenario()
    print("|SEJAM MUITO BEM-VINDOS|")
    time.sleep(1.5)
    print("|AO JOGO DE PALAVRAS-CRUZADAS!|\n")
    time.sleep(1.5)
    print("|ESCOLHA UMA DAS OPÇÕES ABAIXO!|")
    print("|1 - JOGAR|")
    print("|2 - SAIR DO JOGO|")
    opcao = int(input("--> "))

    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

    if (opcao == 1):
       jogar(sorteado)
    elif (opcao == 2):
        break
    else:
        print("Opção inválida!")  
