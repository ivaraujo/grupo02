import random
import time

#FUNÇÕES
def sortearCenario(): #SORTEADOR DE CENÁRIO
    n = random.choice([1,2,3,4])#
    #print(f"Cenário: {n}")
    return n

def verificaPalavra(novaMatriz,vetor,n_sorteado,l):
    # CENÁRIOS
    #n_sorteado = 3
    cenario1 = [[" ","M"," ","V"],["C","A","J","A"],[" ","Ç"," ","S"],[" ","Ã"," ","O"]]
    cenario2 = [[" ","C"," "," "],["M","A","Ç","Ã"],[" ","J"," "," "],["V","A","S","O"]]
    cenario3 = [[" ","C"," "," "],["V","A","S","O"],[" ","J"," "," "],["M","A","Ç","Ã"]]
    cenario4 = [[" ","V"," ","M"],["C","A","J","A"],[" ","S"," ","Ç"],[" ","O"," ","Ã"]]
    v = 0
    x = 0
    y = 0
    if(n_sorteado == 1):
        for x in range(4):
            v = 0
            for y in range(4):
                for v in range(4):
                    if(vetor[v] == cenario1[x][y]):
                        if(vetor[0] == "V"):
                            novaMatriz[x][1] = vetor[v]
                        elif(vetor[0] == "M"):
                            novaMatriz[x][3] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 2):
        for x in range(4):
            v = 0
            for y in range(4):
                for v in range(4):
                    if(vetor[v] == cenario2[x][y]):
                        if(vetor[0] == "V"):
                            novaMatriz[3][y] = vetor[v]
                        elif(vetor[0] == "M"):
                            novaMatriz[1][y] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 3):
        for x in range(4):
            v = 0
            for y in range(4):
                for v in range(4):
                    if(vetor[v] == cenario3[x][y]):
                        if(vetor[0] == "M"):
                            novaMatriz[3][y] = vetor[v]
                        elif(vetor[0] == "V"):
                            novaMatriz[1][y] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]
                        l+=1
    if(n_sorteado == 4):
        #print(novaMatriz)
        for x in range (4):
            v = 0
            for y in range(4):
                for v in range(4):
                    if(cenario4[x][y] == vetor[v]):
                        #print(f"X: {x} Y: {y} V: {v}")
                        if(vetor[0] == "M"):
                            novaMatriz[x][3] = vetor[v]
                        elif(vetor[0] == "V"):
                            novaMatriz[x][1] = vetor[v]
                        else:
                            novaMatriz[x][y] = vetor[v]    
                        l+=1
    return novaMatriz, l

def jogar(n_sort):
    cPalav = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
    for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print("|",cPalav[i][j], end=" ")
            print("|")
    loop = 0
    while (True):
        #print("Loop:",loop)
        if(loop > 15):
            break
        print()
        #print(f"Cenário: {sortearCenario()}")
        print("| ++ Dicas ++ |")
        print("1 - É crocante ao dar uma mordida.")
        print("2 - Tem uma polpa suculenta de sabor relativamente azedo.")
        print("3 - É utilizado para diversos tipos de coisas, desde guardar itens de casa até decorações.", "\n")
        palavra = input("Digite a palavra: ")
        vet_palavra = list(palavra.upper())
        #print(vet_palavra)
        nMatriz, loop = verificaPalavra(cPalav, vet_palavra, n_sort, loop)
        for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print("|",nMatriz[i][j], end=" ")
            print("|")
# MENU

sorteado = sortearCenario()

while True:
    print("|SEJAM MUITO BEM-VINDOS|")
    time.sleep(1.5)
    print("|AO JOGO DE PALAVRAS-CRUZADAS!|\n")
    time.sleep(1.5)
    print("|ESCOLHA UMA DAS OPÇÕES ABAIXO!|")
    print("|1 - JOGAR|")
    print("|2 - SAIR DO JOGO|")
    opcao = int(input("--> "))
    if (opcao == 1):
       jogar(sorteado)
    elif (opcao == 2):
        break
    else:
        print("Opção inválida!")  
