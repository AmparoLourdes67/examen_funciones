def validador(datos):
    if datos[1] >= 2010:
        edad_persona = True
    else:
        edad_persona = False
    if datos[2] >= 180:
        altura_persona = True
    else:
        altura_persona = False
    return [edad_persona, altura_persona]

