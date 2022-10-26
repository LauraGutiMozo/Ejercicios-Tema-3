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

class destructor_esteral(naves):
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

class destructro_estelar (naves):
    def __init__(self,nombre,largo, tripulacion,cantidad_pasajeros):
        naves.__init__(self,nombre,largo, tripulacion,cantidad_pasajeros)
    def __str__(self):
        return naves.__str__(self) 




def navegando ():
    A = alcon_milenario ("alcon_milenario",200,"cacas",54)
    print(A)
    E = estrella_muerte("estrella de la muerte",500,"mamuts",42)
    return A,E

class datos(naves):
    X = ala_X ("Ala X", )

def ordenando_naves(datos,pasajeros):
    D = self.pasajeros 
    D.sort(reverse=True)
    return 

#def nave_mas_tripulacion():

#def buscador_AT ():

#def llevar_pasajeros():

#def 
