nMatriz = [[" "," ","-"," "," "],
           [" "," ","-"," "," "],
           [" ","-","-","-","-"],
           [" "," ","-"," "," "],
           [" ","-","-","-","-"]]

for i in range(5): #EXIBIR JOGO ATUAL
    for j in range(5):
        if(nMatriz[i][j] != " "):                
            print(f"\033[31;41m {nMatriz[i][j]} \033[m", end="")
        else:            
            print(f" {nMatriz[i][j]} ", end="")
    print()