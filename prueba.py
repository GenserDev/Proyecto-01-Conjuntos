# Diccionarios vacíos para almacenar conjuntos
conjunto1 = {}
conjunto2 = {}

# Función para construir conjuntos
def construir_conjunto(conjunto, nombre_conjunto):
    print(f"\nConstruyendo {nombre_conjunto}:")
    while True:
        elemento = input(f"Ingrese un elemento para {nombre_conjunto} (o 'salir' para terminar): ")
        if elemento.lower() == 'salir':
            break
        conjunto[elemento] = True

# Función para operar conjuntos
def operar_conjuntos():
    print("\n----------Operaciones disponibles----------")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    
    operacion = int(input("Selecciona la operación que deseas realizar: "))
    
    # Convertir diccionarios en sets
    set1 = set(conjunto1.keys())
    set2 = set(conjunto2.keys())
    
    match operacion:
        case 1:  # Complemento (asumido con respecto a un universo)
            # Aquí asumimos un "universo" como la unión de ambos conjuntos.
            universo = set1.union(set2)
            complemento1 = universo - set1
            complemento2 = universo - set2
            print(f"Complemento de conjunto1: {complemento1}")
            print(f"Complemento de conjunto2: {complemento2}")
        case 2:  # Unión
            union = set1.union(set2)
            print(f"Unión: {union}")
        case 3:  # Intersección
            interseccion = set1.intersection(set2)
            print(f"Intersección: {interseccion}")
        case 4:  # Diferencia
            diferencia1 = set1.difference(set2)
            diferencia2 = set2.difference(set1)
            print(f"Diferencia (conjunto1 - conjunto2): {diferencia1}")
            print(f"Diferencia (conjunto2 - conjunto1): {diferencia2}")
        case 5:  # Diferencia Simétrica
            diferencia_simetrica = set1.symmetric_difference(set2)
            print(f"Diferencia Simétrica: {diferencia_simetrica}")
        case _:
            print("Opción no válida.")

# Función principal
def main():
    while True:
        print("\n----------Menu----------")
        print("1. Construir Conjunto")
        print("2. Operar Conjunto")
        print("3. Salir del programa")
        
        repUser = int(input("Ingresa una de las siguientes opciones: "))
        
        match repUser:
            case 1:
                conjunto_seleccionado = int(input("Selecciona el conjunto a construir (1 o 2): "))
                if conjunto_seleccionado == 1:
                    construir_conjunto(conjunto1, "conjunto1")
                elif conjunto_seleccionado == 2:
                    construir_conjunto(conjunto2, "conjunto2")
                else:
                    print("Conjunto no válido.")
            case 2:
                operar_conjuntos()
            case 3:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida.")

main()
