def seleccionar_palabras_largas(palabras, longitud_minima):
    # Validar que longitud_minima es un entero
    if type(longitud_minima) is not int:
        raise TypeError("El parámetro longitud_minima debe ser un entero.")

    # Validar que palabras es una lista
    if type(palabras) is not list:
        raise TypeError("El parámetro palabras debe ser una lista.")

    # Preparar la lista de resultado
    resultado = []

    # Recorrer la lista de palabras
    for palabra in palabras:
        # Verificar que cada elemento sea una cadena
        if type(palabra) is not str:
            raise TypeError("Todos los elementos de la lista deben ser cadenas.")

        # Comprobar la longitud mínima
        if len(palabra) >= longitud_minima:
            resultado.append(palabra)

    return resultado
