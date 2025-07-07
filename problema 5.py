def contar_digito_en_numero(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    
    cantidad = numero_str.count(digito_str)
    
    return cantidad

# Ejemplo de uso
numero_ingresado = 157890000
digito_ingresado = 0

resultado = contar_digito_en_numero(numero_ingresado, digito_ingresado)
print(f"Cantidad de veces {digito_ingresado} en el número: {resultado}")
