class naves():
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidad_pasajeros = cantidad_pasajeros
    
    def __str__(self):
        return f"La nave {self.nombre} tiene un largo de {self.largo}, su tripulación es {self.tripulacion}y una capacidad de pasajeros de {self.cantidad_pasajeros}"

class alcon_milenario (naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 

class estrella_muerte(naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 

class lanzadera_imperial (naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 

class destructor_estelar(naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 

class ala_X(naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 

class AT_AT(naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 


class nave_control_droides(naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 


A = alcon_milenario ("alcon_milenario",200,20,2000)
E = estrella_muerte("estrella de la muerte",500,50,50000)
L = lanzadera_imperial("lanzadera imperial", 300,30,3000)
D = destructor_estelar("Destructor estelar",400,50,5000)
X = ala_X ("Ala X",700,70,7000 )
AT = AT_AT("AT_AT",800,80,8000)
C = nave_control_droides("Nave controladora de dorides",100,10,1000)

lista = []
lista.append (A)
lista.append (E)
lista.append (L)
lista.append (D)
lista.append (X)
lista.append (AT)
lista.append (C)
#Punto 1
def navegando ():
    print(A)
    print (E)
    return A,E


#Punto 2
lista_pasaj = []
lista_pasaj.append(A.cantidad_pasajeros)
lista_pasaj.append(E.cantidad_pasajeros)
lista_pasaj.append(L.cantidad_pasajeros)
lista_pasaj.append(D.cantidad_pasajeros)
lista_pasaj.append(X.cantidad_pasajeros)
lista_pasaj.append(AT.cantidad_pasajeros)
lista_pasaj.append(C.cantidad_pasajeros)
print (lista_pasaj)

def ordenando_naves():
    lista.sort()
    print(f"Estas son las naves ordenadas según la cantidad de pasajeros: {lista}")

#Punto 3 
lista_trip = []
lista.append(A.tripulacion)
lista.append(E.tripulacion)
lista.append(L.tripulacion)
lista.append(D.tripulacion)
lista.append(X.tripulacion)
lista.append(AT.tripulacion)
lista.append(C.tripulacion)
print (lista_trip)

def nave_mas_tripulacion():
    lista_trip.sort()
    print(f"Estas son las naves ordenadas según la cantidad de tripulación: {lista_trip}")

#punto 4
def buscador_AT (lista):
    AT =[]
    for n in lista:
        nombre = n
        if nombre[:2]== "AT":
            AT.append(n)
    for i in AT:
        print("nombre",i)

#def llevar_pasajeros():

#def 
