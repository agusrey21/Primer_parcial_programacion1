import Input
import Funciones

nombres = ['','','','','']
jurado1 = [0,0,0,0,0]
jurado2 = [0,0,0,0,0]
jurado3 = [0,0,0,0,0]

nombres_cargados = False
puntajes_cargados = False

while True:
    print('---- MENU ----')
    print('1. Cargar participantes')
    print('2. Cargar puntuaciones')
    print('3. Mostrar puntuaciones')
    print('4. Participantes con promedio menor a 4')
    print('5. Participantes con promedio menor a 8')
    print('6. Promedio de cada jurado')
    print('7. Jurado mas estricto')
    print('8. Jurado mas generoso')
    print('9. Participantes con puntuaciones iguales')
    print('10. Buscar participantes por nombres')
    print('11. TOP 3 Participantes')
    print('12. Ordenar alfabeticamente')
    print('0. Salir')

    opcion = input('Opcion: ')
    
    if opcion == '1':
        for i in range(5):
            nombres[i] = Input.pedir_nombre()
        nombres_cargados = True
    elif opcion == '2':
        if nombres_cargados == False:
            print('Primero se deben de cargar los nombres.')
            continue
        
        for i in range(5):
            print('Puntaje para', nombres[i])
            jurado1[i] = Input.pedir_puntaje(1)
            jurado2[i] = Input.pedir_puntaje(2)
            jurado3[i] = Input.pedir_puntaje(3)
        puntajes_cargados = True
        
    elif opcion == '3':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        Funciones.mostrar_participantes(nombres, jurado1, jurado2, jurado3)
        print('')
    elif opcion == '4':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        Funciones.mostrar_menores_a(nombres, jurado1, jurado2, jurado3, 4)
        print('')
    elif opcion == '5':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        Funciones.mostrar_menores_a(nombres, jurado1, jurado2, jurado3, 8)
        print('')
    elif opcion == '6':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        print(' Promedios de cada Jurado ')
        print('Promedio primer Jurado:', Funciones.promedio_jurado(jurado1))
        print('Promedio segundo Jurado:', Funciones.promedio_jurado(jurado2))
        print('Promedio tercer Jurado:', Funciones.promedio_jurado(jurado3))
        print('')
    elif opcion == '7':
            if puntajes_cargados == False:
                print('Primero hay que cargar los datos.')
                continue
            Funciones.jurado_estricto(jurado1, jurado2, jurado3)
            print('')
    elif opcion == '8':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        Funciones.jurado_generoso(jurado1, jurado2, jurado3)
        print('')
    elif opcion == '9':        
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        Funciones.participantes_puntaje_igual(nombres, jurado1, jurado2, jurado3)      
        print('')
    elif opcion == '10':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        nombre_a_buscar = input('Nombre a buscar: ')
        print('')
        Funciones.buscar_nombre(nombres, jurado1, jurado2, jurado3, nombre_a_buscar)
        print('')
    elif opcion == '11':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        Funciones.top_3(nombres, jurado1, jurado2, jurado3)
        print('')
    elif opcion == '12':
        if puntajes_cargados == False:
            print('Primero hay que cargar los datos.')
            continue
        
        Funciones.ordenar_alfabeticamente(nombres, jurado1, jurado2, jurado3)
        print('')
    elif opcion == '0':
        print('Saliendo del programa.')
        break
    else:
        print('Opcion incorrecta, vuelva a intentar')