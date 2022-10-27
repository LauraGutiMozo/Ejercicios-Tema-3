from turtle import Terminator


class Nodo (object):
    info,sig =None,None

class calculadora (object):
    def __init__(self,numero,termino):
        self.numero=numero
        self.termino=termino

class polinomio(object):
    def __init__(self):
        self.max_termino = None
        self.grado = -1

    def añadir_termino (polinomio, termino, numero):
        aux = Nodo ()
        calcular = calculadora(numero,termino) 

        aux.info = calcular
        if (termino > polinomio.grado):
            aux.sig = polinomio.max_termino
            polinomio.max_termino=aux
            polinomio.grado =termino

        else: actual = polinomio.max_termino
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual= actual.sig
        aux.sig = actual.sig
        actual.sig = aux
    
    def cambiar_termino(polinomio,termino):
        aux = polinomio.max_termino
        while aux is not None and aux.info.termino != termino:
            actual = actual.sig
        aux = aux.sig
        actual.sig = aux
    
    def obtener_numero (polinomio,termino):
        aux = polinomio.max_termino
        while aux is not None and aux.info.termino > termino:
            aux = aux.sig 
        if aux is not None and aux.info.termino == termino:
            return aux.info.valor
        else:
            return 0
    
    def mostrar (polinomio):
        aux = polinomio.max_termino
        pol = ""
        
        if aux is not None:
            while aux is not None:
                signo = ""
                if aux.info.valor >= 0:
                    signo += "+"
                pol + = signo + str(aux.info.valor)"x^"+str (aux.info.termino)
                aux =aux.sig

        return pol
        
    def restar ():
        
    def dividir (polinomio1,polinomio2):
        paux = polinomio()
        pol1=polinomio1.max_termino
        
        while pol1 is not None:
            pol2 =polinomio2.max_termino
            while pol2 is not None:
                termino = pol1.info.termino + pol2.info.termino 
                numero =pol1.info.numero / pol2.info.valor
                if obtener_numero (paux,termino)!=0:
                    valor += obtener_numero (paux,termino)
                    cambiar_termino(paux, termino,numero)
                else:
                    añadir_termino (paux, termino,numero)
                pol2 =pol2.sig
            pol1=pol1.sig
        return paux





    