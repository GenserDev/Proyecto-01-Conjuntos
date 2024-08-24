# Sets vacíos para almacenar conjuntos
conjunto1 = set()
conjunto2 = set()

# Función para construir conjuntos
def construir_conjunto(conjunto, nombre_conjunto):
    print(f"\nConstruyendo {nombre_conjunto}:")
    while True:
        elemento = input(f"Ingrese un elemento para {nombre_conjunto} (o 'salir' para terminar): ").upper()
        if elemento.lower() == 'salir':
            break
        # Validar que el elemento sea una letra o un dígito
        if elemento.isalnum() and len(elemento) == 1:
            conjunto.add(elemento)
            print(f"Elemento '{elemento}' agregado a {nombre_conjunto}.")
        else:
            print("Por favor, ingrese un solo carácter alfanumérico (letra A-Z o dígito 0-9).")

# Función para operar conjuntos
def operar_conjuntos():
    if not conjunto1 or not conjunto2:
        print("Ambos conjuntos deben estar construidos antes de operar.")
        return
    
    print("\n----------Operaciones disponibles----------")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    
    try:
        operacion = int(input("Selecciona la operación que deseas realizar: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    
    match operacion:
        case 1:  # Complemento con respecto a un universo completo
            universo = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") # este maneja los elementos que son permitidos
            complemento1 = universo - conjunto1
            complemento2 = universo - conjunto2
            print(f"Complemento de conjunto1: {sorted(complemento1)}")
            print(f"Complemento de conjunto2: {sorted(complemento2)}")
        case 2:  # Unión
            union = conjunto1.union(conjunto2)
            print(f"Unión: {sorted(union)}")
        case 3:  # Intersección
            interseccion = conjunto1.intersection(conjunto2)
            print(f"Intersección: {sorted(interseccion)}")
        case 4:  # Diferencia
            diferencia1 = conjunto1.difference(conjunto2)
            diferencia2 = conjunto2.difference(conjunto1)
            print(f"Diferencia (conjunto1 - conjunto2): {sorted(diferencia1)}")
            print(f"Diferencia (conjunto2 - conjunto1): {sorted(diferencia2)}")
        case 5:  # Diferencia Simétrica
            diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
            print(f"Diferencia Simétrica: {sorted(diferencia_simetrica)}")
        case _:
            print("Opción no válida.")

# Función principal
def main():
    while True:
        print("\n----------Menú Principal----------")
        print("1. Construir Conjunto")
        print("2. Operar Conjunto")
        print("3. Salir del programa")
        
        try:
            repUser = int(input("Ingresa una de las siguientes opciones: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        match repUser:
            case 1:
                conjunto_seleccionado = int(input("Selecciona el conjunto a construir (1 o 2): "))
                if conjunto_seleccionado == 1:
                    construir_conjunto(conjunto1, "conjunto1")
                    print(f"Conjunto1 actual: {sorted(conjunto1)}")
                elif conjunto_seleccionado == 2:
                    construir_conjunto(conjunto2, "conjunto2")
                    print(f"Conjunto2 actual: {sorted(conjunto2)}")
                else:
                    print("Conjunto no válido.")
            case 2:
                operar_conjuntos()
            case 3:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()
