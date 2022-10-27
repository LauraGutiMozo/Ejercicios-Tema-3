class tabla_Hash():
    def __init__(self):
        self.tabla = [None]*8

    def __format__(self,valor):
        key =0
        for i in range (0,len(valor)):
            key += ord (valor[i])
            return key %8

    def 

