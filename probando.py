def dibujar_la_matriz (matriz):
    for i in range (len(matriz)):
        print ("["),
        for j in range (len (matriz [i])):
            print("{:>3s}".format(str(matriz[i][j]))),
            print("]")
dibujar_la_matriz(matriz)
    
def sarrus():
    multiplicar = [[0:0]*[1:1]*[2:2]]
    print(multiplicar)
