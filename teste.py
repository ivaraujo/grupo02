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

    #1 caja
    #2 vaso
    #3 maçã

    cenario1 = [[" "," ","3"," ","2"],
                [" "," ","M"," ","V"],
                ["1","C","A","J","A"],
                [" "," ","Ç"," ","S"],
                [" "," ","Ã"," ","O"]]
    cenario2 = [[" "," ","1"," "," "],
                [" "," ","C"," "," "],
                ["3","M","A","Ç","Ã"],
                [" "," ","J"," "," "],
                ["2","V","A","S","O"]]
    cenario3 = [[" "," ","1"," "," "],
                [" "," ","C"," "," "],
                ["2","V","A","S","O"],
                [" "," ","J"," "," "],
                ["3","M","A","Ç","Ã"]]
    cenario4 = [[" "," ","2"," ","3"],
                [" "," ","V"," ","M"],
                ["1","C","A","J","A"],
                [" "," ","S"," ","Ç"],
                [" "," ","O"," ","Ã"]]

    cPalav = [[" "," ","3"," ","2"],[" "," ","-"," ","-"],["1","-","-","-","-"],[" "," ","-"," ","-"],[" "," ","-"," ","-"]]
    cPalav = [[" "," ","1"," "," "],[" "," ","-"," "," "],["3","-","-","-","-"],[" "," ","-"," "," "],["2","-","-","-","-"]]
    cPalav = [[" "," ","1"," "," "],[" "," ","-"," "," "],["2","-","-","-","-"],[" "," ","-"," "," "],["3","-","-","-","-"]]
    cPalav = [[" "," ","2"," ","3"],[" "," ","-"," ","-"],["1","-","-","-","-"],[" "," ","-"," ","-"],[" "," ","-"," ","-"]]