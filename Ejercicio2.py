import numpy as np

def Matriz():
    m = np.array([(1,2,3,4),(1,2,3,4),(1,2,3,4)])

    det = ((m[0][0] * m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])) - ((m[2][0] * m[1][1] * m[0][2]) + (m[2][1]  * m[1][2] * m[0][0]) + (m[2][2] * m[1][0] * m[0][1]))

    print (f"El determinante de la matriz será:{det}")


Matriz()