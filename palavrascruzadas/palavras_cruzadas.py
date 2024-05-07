
import random

#cPalavra = [["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"]]

#FUNÇÕES

def sortearCenario(): #SORTEADOR DE CENÁRIO
    n = random.choice([1,2,3,4])
    print(f"Cenário: {n}")
    return n

def verificaPalavra(novoVetor,vetor,n_sorteado,l):
    # CENÁRIOS
    cenario1 = [[" ","M"," ","V"],["C","A","J","A"],[" ","Ç"," ","S"],[" ","Ã"," ","O"]]
    cenario2 = [[" ","C"," "," "],["M","A","Ç","Ã"],[" ","J"," "," "],["V","A","S","O"]]
    cenario3 = [[" ","C"," "," "],["V","A","S","O"],[" ","J"," "," "],["M","A","Ç","Ã"]]
    cenario4 = [[" ","V"," ","M"],["C","A","J","A"],[" ","S"," ","Ç"],[" ","O"," ","Ã"]]
    #novoVetor = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
    v = 0
    x = 0
    y = 0   
    if(n_sorteado == 1):
        #print(cenario1)
        for x in range(4):
            for y in range(4):
                if(vetor[v] == cenario1[x][y]):                    
                    print("OK")
                    #print(vetor[v])
                    novoVetor[x][y] = vetor[v]
                    v+=1
                    l+=1
                    break
    if(n_sorteado == 2):
        #print(cenario2)
        for x in range(4):
            for y in range(4):
                if(vetor[v] == cenario2[x][y]):                    
                    print("OK")
                    #print(vetor[v])
                    novoVetor[x][y] = vetor[v]
                    v+=1
                    l+=1
                    break
    if(n_sorteado == 3):
        #print(cenario3)
        for x in range(4):
            for y in range(4):
                if(vetor[v] == cenario3[x][y]):
                    print("OK")
                    #print(vetor[v])
                    novoVetor[x][y] = vetor[v]
                    v+=1
                    l+=1
                    break
    if(n_sorteado == 4):
        #print(cenario4)
        for x in range(4):
            for y in range(4):
                if(vetor[v] == cenario4[x][y]):
                    print("OK")
                    #print(vetor[v])
                    novoVetor[x][y] = vetor[v]
                    v+=1
                    l+=1
                    break
    #print(novoVetor)
    return novoVetor, l

def jogar(n_sort):
    #cPalav = cPalavr.copy()
    cPalav = [["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"],["| |","| |","| |","| |"]]
    loop = 0
    while (True):
        print("Loop:",loop)
        for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print(cPalav[i][j], end=" ")                        
            print()
        if(loop > 6):
            break    
        #print("3º palavra:")
        #n_palavra = int(input("Nº da palavra: "))
        palavra = input("Digite a palavra: ")
        vet_palavra = list(palavra.upper())
        print(vet_palavra)
        nVetor, loop = verificaPalavra(cPalav, vet_palavra, n_sort, loop)
        cPalav = nVetor.copy()
                    
    
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