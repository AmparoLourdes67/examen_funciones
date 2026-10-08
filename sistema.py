from funciones import validador
respuesta = validador(jugador)
if respuesta[0] == True:
    print("Nacido en 2010 o mas")
if respuesta[1] == True:
    print("Cumple con la altura")