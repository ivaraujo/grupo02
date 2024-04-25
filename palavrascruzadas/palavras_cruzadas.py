import random



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

def jogar(n_sort):
    while True:
        print("3º palavra:")
        n_palavra = int(input("Nº da palavra: "))
        palavra = input("Digite a palavra: ")
        vet_palavra = list(palavra)
        verificaPalavra(vet_palavra,n_sort)
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
        #imprimir(sorteado)
        jogar(sorteado)
    elif (opcao == 2):
        break
    else:
        print("Opção inválida!")
