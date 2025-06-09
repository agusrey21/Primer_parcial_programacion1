import Input
import Funciones

nombres = []
matriz_puntajes = []

while True:
    print('---- MENU ----')
    print('1. Cargar participantes')
    print('2. Cargar puntuaciones')
    print('3. Mostrar puntuaciones')
    print('4. Participantes con promedio menor a 4')
    print('5. Participantes con promedio menor a 8')
    print('6. Buscar participante por nombre')
    print('7. Top 3 mejores promedios')
    print('8. Participantes ordenados alfabeticamente')
    print('9. Jurado mas estricto')
    print('10. Jurado mas generoso')
    print('11. Participantes con puntuaciones iguales')
    print('12. Mostrar ganador')
    print('0. Salir')

    opcion = input('Opcion: ')

    if opcion == '1':
        nombres = Input.carga_participantes()

    elif opcion == '2':
        if nombres == []:
            print('Primero se deben cargar los nombres.')
        else:
            matriz_puntajes = Input.carga_puntajes(nombres)

    elif opcion == '3':
        if matriz_puntajes:
            booleano = Funciones.mostrar_participantes(nombres, matriz_puntajes)
            if booleano == True:
                print()
                print("Se mostraron todos los participantes.")
        else:
            print('Primero carga los puntajes.')

    elif opcion == '4':
        if matriz_puntajes:
            resultado = Funciones.mostrar_menores_a(nombres, matriz_puntajes, 4)
            if not resultado:
                print('No hay participantes con promedio menor a', 4)
        else:
            print('Primero carga los puntajes.')

    elif opcion == '5':
        if matriz_puntajes:
            hay = Funciones.mostrar_menores_a(nombres, matriz_puntajes, 8)
            if not hay:
                print('No hay participantes con promedio menor a', 8)
        else:
            print('Primero carga los puntajes.')

    elif opcion == '6':
        if matriz_puntajes:
            nombre = input('Nombre a buscar: ')
            esta = Funciones.buscar_nombre(nombres, matriz_puntajes, nombre)
            if esta == False:
                print('Participante no encontrado')
        else:
            print('Primero carga los puntajes')


    elif opcion == '7':
        if matriz_puntajes:
            indices, valores = Funciones.top_3(nombres, matriz_puntajes)
            print("--- Top 3 Participantes ---")
            for k in range(3):
                print(nombres[indices[k]], "- Promedio:", valores[k])
        else:
            print('Primero carga los puntajes.')


    elif opcion == '8':
        if matriz_puntajes:
            nombres, matriz_puntajes = Funciones.ordenar_alfabeticamente(nombres, matriz_puntajes)
            Funciones.mostrar_participantes(nombres, matriz_puntajes)
        else:
            print('Primero carga los puntajes.')


    elif opcion == '9':
        if matriz_puntajes:
            jurado_estricto = Funciones.jurado_mas_estricto(matriz_puntajes)
            print(f'jurado(s) mas estricto(s): {jurado_estricto}')
        else:
            print('Primero carga los puntajes.')

    elif opcion == '10':
        if matriz_puntajes:
            jurado_generoso = Funciones.jurado_mas_generoso(matriz_puntajes)
            print(f'jurado(s) mas generoso(s): {jurado_generoso}')
        else:
            print('Primero carga los puntajes.')

    elif opcion == '11':
        if matriz_puntajes:
            iguales = Funciones.participantes_con_puntajes_iguales(nombres, matriz_puntajes)
        
            if iguales:
                for nombre, puntos in iguales:
                    print(f"{nombre} tiene puntajes iguales de todos los jurados: {puntos}")
            else:
                print("No hay participantes con puntajes iguales entre todos los jurados.")
        else:
            print('Primero carga los puntajes.')
    
    elif opcion == "12":
        if matriz_puntajes:
            ganadores = Funciones.mostrar_ganador(matriz_puntajes)
            if len(ganadores) == 1:
                print(f"El ganador es: {nombres[ganadores[0]]}")
            else:
                print("Empate entre:")
                for i in ganadores:
                    print(nombres[i])
        else:
            print('Primero carga los puntajes.')


    elif opcion == '0':
        print('Fin del programa.')
        break

    else:
        print('Opcion invalida.')