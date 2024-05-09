
import random

#cPalavra = [["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"]]

#FUNÇÕES

def sortearCenario(): #SORTEADOR DE CENÁRIO
    n = random.choice([1,2,3,4])
    print(f"Cenário: {n}")
    return n

def verificaPalavra(novaMatriz,vetor,n_sorteado,l):
    # CENÁRIOS
    #n_sorteado = 4
    cenario1 = [[" ","M"," ","V"],["C","A","J","A"],[" ","Ç"," ","S"],[" ","Ã"," ","O"]]
    cenario2 = [[" ","C"," "," "],["M","A","Ç","Ã"],[" ","J"," "," "],["V","A","S","O"]]
    cenario3 = [[" ","C"," "," "],["V","A","S","O"],[" ","J"," "," "],["M","A","Ç","Ã"]]
    cenario4 = [[" ","V"," ","M"],["C","A","J","A"],[" ","S"," ","Ç"],[" ","O"," ","Ã"]]
    v = 0
    x = 0
    y = 0   
    if(n_sorteado == 1):
        #print(cenario1)
        for x in range(4):
            v = 0
            for y in range(4):
                if(vetor[v] == cenario1[x][y]):                    
                    print("OK")
                    #print(vetor[v])
                    novaMatriz[x][y] = vetor[v]
                    v+=1
                    l+=1
    if(n_sorteado == 2):
        #print(cenario2)
        for x in range(4):
            v = 0
            for y in range(4):
                if(vetor[v] == cenario2[x][y]):                    
                    print("OK")
                    #print(vetor[v])
                    novaMatriz[x][y] = vetor[v]
                    v+=1
                    l+=1
    if(n_sorteado == 3):
        #print(cenario3)
        for x in range(4):
            v = 0
            for y in range(4):
                if(vetor[v] == cenario3[x][y]):
                    print("OK")
                    #print(vetor[v])
                    novaMatriz[x][y] = vetor[v]
                    v+=1
                    l+=1
    if(n_sorteado == 4):
        #print(cenario4)
        print(novaMatriz)
        for x in range(4):
            v = 0            
            for y in range(4):
                #print(f"X: {x} Y: {y} V: {v}")
                #v+=1  
                if(vetor[v] == cenario4[x][y]):
                    #print("OK")
                    print(f"X: {x} Y: {y} V: {v}")  
                    print(f"Lista: {vetor[v]} Cénario: {cenario4[x][y]} novaMatriz: {novaMatriz[x][y]}")                   
                    novaMatriz[x][y] = vetor[v]                                       
                    v+=1
                    l+=1
    #print(novoVetor)
    return novaMatriz, l

def jogar(n_sort):
    cPalav = [["","","",""],["","","",""],["","","",""],["","","",""]]
    for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print(cPalav[i][j], end=" ")                        
            print()
    loop = 0
    while (True):
        print("Loop:",loop)        
        if(loop > 6):
            break    
        #print("3º palavra:")
        #n_palavra = int(input("Nº da palavra: "))
        palavra = input("Digite a palavra: ")
        vet_palavra = list(palavra.upper())
        print(vet_palavra)
        nMatriz, loop = verificaPalavra(cPalav, vet_palavra, n_sort, loop)
        for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print(nMatriz[i][j], end=" ")                        
            print()
                    
    
# MENU

sorteado = sortearCenario()

while True:
    print("1 - Jogar")
    print("2 - Sair")
    opcao = int(input("--> "))
    if (opcao == 1):        
       jogar(sorteado)
    elif (opcao == 2):
        break
    else:
        print("Opção inválida!")