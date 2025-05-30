def pedir_nombre()-> str:
    while True:   
        nombre = input(f'Ingrese el nombre del participante: ')

        nombre_sin_espacios = nombre.replace(' ', '')

        es_alfabetico = True
        
        for caracter in nombre_sin_espacios:
            if not caracter.isalpha():
                es_alfabetico = False
                break
        
        if len(nombre_sin_espacios) >= 3 and es_alfabetico:
            return nombre
        else:
            print('ERROR: Nombre invalido. Debe tener al menos 3 letras y solo letras y espacios.')
    
def pedir_puntaje(jurado)-> int:
    while True:
        nota = int(input('Ingrese nota del jurado ' + str(jurado) + ' (1 a 10): '))
        if 1 <= nota <= 10:
            return nota
        else:
            print('ERROR: debe estar entre 1 y 10.')