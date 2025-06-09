def promedio(n1, n2, n3)->float:
    return (n1 + n2 + n3) / 3

def mostrar_participantes(nombres, j1, j2, j3)-> str:
    print()
    print('Puntajes: ')
    for i in range(5):
        prom = promedio(j1[i], j2[i], j3[i])
        print(f'''      {nombres[i]}:
        Jurado 1: {j1[i]}/10 
        Jurado 2: {j2[i]}/10 
        Jurado 3: {j3[i]}/10
        Promedio: {prom}/10
              ''')

def mostrar_menores_a(nombres, j1, j2, j3, limite)->str:
    hay_menores_a = False
    print('')
    for i in range(5):
        prom = promedio(j1[i], j2[i], j3[i])
        if prom < limite:
            print(f'{nombres[i]}, tuvo un promedio de: {prom}')
            hay_menores_a = True
    if hay_menores_a == False:
        print(f'No hay participantes con promedio menor a {limite}')

def promedio_jurado(jurado)->float:
    total = 0
    for i in range(5):
        total = total + jurado[i]
    return total / 5

def buscar_nombre(nombres, j1, j2, j3, nombre_buscado)->str:
    for i in range(5):
        if nombres[i].lower() == nombre_buscado.lower():
            print(f''' El participante {nombres[i]} tiene los siguientes puntajes: 
            Primer jurado: {j1[i]}
            Segundo jurado: {j2[i]}
            Tercer jurado: {j3[i]}
            y su promedio es de: {promedio(j1[i], j2[i], j3[i])}
            ''')
            return
    print('No se encontro ese participante.')
    
def jurado_estricto(j1,j2,j3)->str:
    promedio_estricto = [promedio_jurado(j1), promedio_jurado(j2), promedio_jurado(j3)]
    minimo = promedio_estricto[0]
    
    for i in range(3):
        if promedio_estricto[i] < minimo:
            minimo = promedio_estricto[i]
    
    print('JURADO MAS ESTRICTO: ')
    for i in range(3):
        if promedio_estricto[i] == minimo:
            if i == 0:
                print('El primer jurado es el mas estricto')
            elif i == 1:
                print('El segundo jurado es el mas estricto')
            else:
                print('el tercer jurado es el mas estricto')

def jurado_generoso(j1, j2, j3)->str:
    promedio_generoso = [promedio_jurado(j1), promedio_jurado(j2), promedio_jurado(j3)]
    maximo = promedio_generoso[0]
    
    for i in range(3):
        if promedio_generoso[i] > maximo:
            maximo = promedio_generoso[i]
    
    print('JURADO MAS GENEROSO: ')
    for i in range(3):
        if promedio_generoso[i] == maximo:
            if i == 0:
                print('El primer jurado es el mas generoso')
            elif i == 1:
                print('El segundo jurado es el mas generoso')
            else:
                print('el tercer jurado es el mas generoso')

def participantes_puntaje_igual(nombres, j1, j2, j3)->str:
    encontrados = False
    
    for i in range(5):
        if j1[i] == j2[i] == j3[i]:
            print(f'{nombres[i]} tiene el mismo puntaje de los 3 jurados. {j1[i]}/10')
            encontrados = True
    if not encontrados:
        print('No hay participantes con puntajes iguales de los 3 jurados.')
        
def top_3(nombres, j1, j2, j3)->str:
    nombres_ordenados = ['','','','','']
    promedios = [0,0,0,0,0]
    
    for i in range(5):
        nombres_ordenados[i] = nombres[i]
        prom = promedio(j1[i], j2[i], j3[i])
        promedios[i] = prom
    
    for i in range(4):
        for j in range(i+1, 5):
            if promedios[j] > promedios[i]:
                aux = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux
                
                aux_nombre = nombres_ordenados[i]
                nombres_ordenados[i] = nombres_ordenados[j]
                nombres_ordenados[j] = aux_nombre
    
    print(' TOP 3 PARTICIPANTES')
    for i in range(3):
        print(f' {nombres_ordenados[i]} - PROMEDIO = {promedios[i]}')
    
def ordenar_alfabeticamente(nombres, j1, j2, j3)->str:
    for i in range(4):
        for j in range(i+1, 5):
            if nombres[i].lower() > nombres[j].lower():
                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre
                
                aux_j1 = j1[i]
                j1[i] = j1[j]
                j1[j] = aux_j1
                
                aux_j2 = j2[i]
                j2[i] = j2[j]
                j2[j] = aux_j2
                
                aux_j3 = j3[i]
                j3[i] = j3[j]
                j3[j] = aux_j3
    
    print('Se ordenaron los Participantes de forma alfabetica:')
    mostrar_participantes(nombres, j1, j2, j3)