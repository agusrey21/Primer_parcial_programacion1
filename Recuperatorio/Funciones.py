def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)

def promedio_jurado(matriz, indice_jurado):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][indice_jurado]
    return suma / len(matriz)

def mostrar_participantes(nombres, matriz):
    print('--- Puntajes ---')
    for i in range(len(nombres)):
        print(nombres[i])
        for j in range(len(matriz[i])):
            print(f'Jurado N°{j+1}: {matriz[i][j]} ')
        prom = promedio(matriz[i])
        print(f'Promedio: {prom}')
    return True

def mostrar_menores_a(nombres, matriz, limite):
    hay = False
    print()
    print("--- Participantes con promedio menor a", limite, "---")
    for i in range(len(nombres)):
        prom = promedio(matriz[i])
        if prom < limite:
            print(nombres[i], 'Promedio:', prom)
            hay = True
    print()
    return hay

def buscar_nombre(nombres, matriz, nombre_buscado):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscado.lower():
            print(f"Se busco al participante: {nombres[i]}")
            print("Sus putajes fueron los siguientes: ")
            for j in range(len(matriz[i])):
                print(f"Jurado N°{j+1}: {matriz[i][j]}")
            prom = promedio(matriz[i])
            print(f"Su promedio fue de: {prom}")
            return True  
    return False  


def burbujeo(valores):
    indices = list(range(len(valores)))
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            if valores[j] > valores[i]:
                valores[i], valores[j] = valores[j], valores[i]
                indices[i], indices[j] = indices[j], indices[i]
    return indices, valores

def top_3(nombres, matriz):
    promedios = []
    for i in range(len(nombres)):
        prom = promedio(matriz[i])
        promedios += [prom]
    indices, ordenados = burbujeo(promedios)

    return indices, ordenados

def ordenar_alfabeticamente(nombres, matriz):
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i].lower() > nombres[j].lower():
                nombres[i], nombres[j] = nombres[j], nombres[i]
                matriz[i], matriz[j] = matriz[j], matriz[i]
    return nombres, matriz

def jurado_mas_estricto(matriz):
    jurados = len(matriz[0])
    promedios = []
    for j in range(jurados):
        prom = promedio_jurado(matriz, j)
        promedios += [prom]
    minimo = promedios[0]
    resultado = "Jurado N° 1"
    for j in range(1, jurados):
        if promedios[j] < minimo:
            minimo = promedios[j]
            resultado = "Jurado N°" + str(j+1)
        elif promedios[j] == minimo:
            resultado += ", Jurado N°" + str(j+1)
    return resultado

def jurado_mas_generoso(matriz):
    jurados = len(matriz[0])
    promedios = []
    for j in range(jurados):
        prom = promedio_jurado(matriz, j)
        promedios += [prom]
    maximo = promedios[0]
    resultado = "Jurado N° 1"
    for j in range(1, jurados):
        if promedios[j] > maximo:
            maximo = promedios[j]
            resultado = "Jurado N°" + str(j+1)
        elif promedios[j] == maximo:
            resultado += ", Jurado N°" + str(j+1)
    return resultado

def participantes_con_puntajes_iguales(nombres, matriz):
    resultados = []

    for i in range(len(matriz)):
        iguales = True
        primero = matriz[i][0]
        for j in range(1, len(matriz[i])):
            if matriz[i][j] != primero:
                iguales = False
        if iguales:
            resultados += [(nombres[i], primero)]

    return resultados

def mostrar_ganador(matriz):
    mayor = promedio(matriz[0])
    ganadores = [0]
    for i in range(1, len(matriz)):
        p = promedio(matriz[i])
        if p > mayor:
            mayor = p
            ganadores = [i]
        elif p == mayor:
            ganadores += [i]
    return ganadores