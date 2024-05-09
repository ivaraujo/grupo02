cPalavra = [[" ","C"," "," "],["M","A","Ç","Ã"],[" ","J"," "," "],["V","A","S","O"]]
v = 0
for i in range(4):
    for j in range(4):
        print(cPalavra[i][j],end="")
    print()

for i in range(4):
    for j in range(4):
        letra = input("Dite a letra: ")
        cPalavra[i][j] = letra
        v+=1

for i in range(4):
    for j in range(4):
        print(cPalavra[i][j],end="")
    print()