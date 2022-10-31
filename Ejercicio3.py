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



#Punto 0
lista_nom = []
lista_nom.append (A.nombre)
lista_nom.append (E.nombre)
lista_nom.append (L.nombre)
lista_nom.append (D.nombre)
lista_nom.append (X.nombre)
lista_nom.append (AT.nombre)
lista_nom.append (C.nombre)

def ordenando_alfabeticamente():
    lista_ascendente = lista_nom.sort( )
    lista_descendente = lista_nom.sort (reverse = True)
    print (lista_ascendente)
    print (lista_descendente)


#Punto 1
def navegando ():
    print(A)
    print (E)
    return A,E


#Punto 2
lista_pasaj = [("alcon_milenario",200,20,2000),("estrella de la muerte",500,50,50000),("lanzadera imperial", 300,30,3000),("Destructor estelar",400,50,5000),("Ala X",700,70,7000 ),("AT_AT",800,80,8000),("Nave controladora de dorides",100,10,1000)]

def ordenando_naves(item):
    error =10000 -item[1]
    cantidad_pasajeros = item[4]
    return (error, cantidad_pasajeros)
def pregunta_2 ():
    naves_ordenadas = sorted (lista_pasaj, key = ordenando_naves)
    print(naves_ordenadas)
    
#Punto 3 
def nave_mas_tripulacion(item):
    error =10000 -item[1]
    tripulacion = item[3]
    return (error, tripulacion)
def pregunta_3 ():
    tripulacion_ordenada = sorted (lista_pasaj, key = nave_mas_tripulacion)
    print(f"Estas son las naves ordenadas según la cantidad de tripulación: {tripulacion_ordenada}")



#punto 4
def buscador_AT (lista):
    AT =[]
    for n in lista:
        nombre = n
        if nombre[:2]== "AT":
            AT.append(n)
    for i in AT:
        print("nombre",i)


#Punto 5
def llevar_pasajeros():
    lista_más_seis = []
    lista_menos_seis = []
    if naves.cantidad_pasajeros >= 6:
        lista_más_seis.append =[]
        print (lista_más_seis)
    else:
        lista_menos_seis.append = []


