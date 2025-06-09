def carga_participantes():
    nombres = []
    cantidad = input('Cuantos participantes habra?(minimo debe haber 5): ')
    while not cantidad.isdigit() or int(cantidad) < 5:
        cantidad = input('Error. Se debe ingresar 5 o mas participantes: ')
    cantidad = int(cantidad)

    i = 0
    while i < cantidad:
        nombre = input(f'Ingrese el nombre del participante {i + 1}: ')
        nombre_sin_espacios = nombre.replace(' ', '')
        if len(nombre_sin_espacios) >= 3 and nombre_sin_espacios.isalpha():
            nombres += [nombre]
            i += 1
        else:
            print('Error: nombre invalido. Debe tener al menos 3 letras y solo letras y espacios.')
    return nombres

def carga_puntajes(nombres):
    jurados= input('Cuantos jurados hay?(minimo debe haber 3): ')
    while not jurados.isdigit() or int(jurados) < 3:
        jurados= input('Error. Ingresa un numero valido de jurados(3 o mas): ')

    cantidad_jurados = int(jurados)

    cantidad_nombres = 0
    for i in nombres:
        cantidad_nombres += 1

    matriz_puntajes = []
    i = 0
    while i < cantidad_nombres:
        fila = []
        j = 0
        while j < cantidad_jurados:
            fila += [0] 
            j += 1
        matriz_puntajes += [fila]
        i += 1

    i = 0
    while i < cantidad_nombres:
        print(f'Notas del jurado para {nombres[i]}')
        j = 0
        while j < cantidad_jurados:
            nota_str = input(f'Ingrese nota del jurado {j + 1} para {nombres[i]} (1 a 10): ')
            while not nota_str.isdigit() or int(nota_str) < 1 or int(nota_str) > 10:
                nota_str = input('Error. Nota invalida. Ingresá un numero del 1 al 10: ')
            matriz_puntajes[i][j] = int(nota_str)
            j += 1
        i += 1

    return matriz_puntajes

