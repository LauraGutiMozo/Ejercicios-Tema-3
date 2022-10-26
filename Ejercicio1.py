def torre (numero_discos, base_salida, base_final, base_auxiliar):
    if numero_discos ==1:
        print (f"mover disco desde la base inicial {base_salida} hasta la base final {base_final}")
        
    else:
        torre (numero_discos-1,base_salida, base_auxiliar, base_final)
        print (f"mover disco desde la base inicial {base_salida} hasta la base final {base_final}")
        torre (numero_discos-1,base_auxiliar,base_final,base_salida)




