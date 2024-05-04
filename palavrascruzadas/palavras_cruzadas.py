import random

cPalavra = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]

#FUNÇÕES

def sortearCenario(): #SORTEADOR DE CENÁRIO
    n = random.choice([1,2,3,4])
    print(f"Cenário: {n}")
    return n



def verificaPalavra(vetor,n_sorteado):
    # CENÁRIOS
    cenario1 = [[" ","M"," ","V"],["C","A","J","A"],[" ","Ç"," ","S"],[" ","Ã"," ","O"]]
    cenario2 = [[" ","C"," "," "],["M","A","Ç","Ã"],[" ","J"," "," "],["V","A","S","O"]]
    cenario3 = [[" ","C"," "," "],["V","A","S","O"],[" ","J"," "," "],["M","A","Ç","Ã"]]
    cenario4 = [[" ","V"," ","M"],["C","A","J","A"],[" ","S"," ","Ç"],[" ","O"," ","Ã"]]
    novoVetor = []
    for x in range(4):
        for y in range(4):
            if(vetor[x][y] == cenario1[x][y]):
                novoVetor[x][y] = cenario1[x][y]
                print(novoVetor)
    return novoVetor

def jogar(n_sort,cPalav):
    while True:
        print("_"*13)
        for i in range(4): #EXIBIR JOGO ATUAL
            for j in range(4):
                print("|",cPalav[i][j], end="")                        
            print("|")
            print("¯"*13)
        print("3º palavra:")
        n_palavra = int(input("Nº da palavra: "))
        palavra = input("Digite a palavra: ")
        vet_palavra = list(palavra)
        cPalav = verificaPalavra(vet_palavra,n_sort)
'''
def imprimir(cenario):
    for i in range(4): #EXIBIR CENÁRIO
        for j in range(4):
            if (cenario == 1):
                print(cenario1[i][j], end=" ")
            if (cenario == 2):
                print(cenario2[i][j], end=" ")
            if (cenario == 3):
                print(cenario3[i][j], end=" ")
            if (cenario == 4):
                print(cenario4[i][j], end=" ")        
        print()'''
    
# MENU

sorteado = sortearCenario()

while True:
    print("1 - Jogar")
    print("2 - Sair")
    opcao = int(input("--> "))
    if (opcao == 1):        
        jogar(sorteado,cPalavra)
    elif (opcao == 2):
        break
    else:
        print("Opção inválida!")
