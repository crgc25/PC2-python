numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if respuesta == "NO":
        break
    elif respuesta == "SI":
        while True:
            try:
                num = int(input("Ingrese el número: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    else:
        print("Respuesta no reconocida. Por favor, ingrese SI o NO.")

print(f"Números ingresados: {numeros}")

cantidad_pares = sum(1 for n in numeros if n % 2 == 0)
cantidad_impares = len(numeros) - cantidad_pares

print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")
