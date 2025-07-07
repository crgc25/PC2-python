MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def obtener_mes_por_nombre(nombre_mes):
    """
    Devuelve el número del mes (1-12) dado el nombre del mes en español.
    La comparación no distingue mayúsculas/minúsculas.
    """
    nombre_mes = nombre_mes.strip().lower()
    for i, mes in enumerate(MESES, start=1):
        if mes.lower() == nombre_mes:
            return i
    return None  # En caso de que no se encuentre

def parsear_fecha(fecha_str):
    """
    Intenta parsear la fecha en diferentes formatos y devuelve (año, mes, día)
    en formato numérico.
    """
    fecha_str = fecha_str.strip()
   
    if '/' in fecha_str:
        partes = fecha_str.split('/')
        if len(partes) == 3:
            mes_str, dia_str, año_str = partes
            try:
                mes = int(mes_str)
                dia = int(dia_str)
                año = int(año_str)
                return año, mes, dia
            except ValueError:
                pass  
    
    else:
        
        if ',' in fecha_str:
            parte1, año_str = fecha_str.split(',', 1)
            año_str = año_str.strip()
            
            partes = parte1.strip().split()
            if len(partes) >= 2:
                mes_str = ' '.join(partes[:-1])  
                dia_str = partes[-1]
                
                try:
                    año = int(año_str)
                except ValueError:
                    return None
                
                try:
                    mes = int(mes_str)
                except ValueError:
                    
                    mes = obtener_mes_por_nombre(mes_str)
                try:
                    dia = int(dia_str)
                except ValueError:
                    return None
                if mes is not None:
                    return año, mes, dia
    
    return None

def formatear_fecha(año, mes, día):
    """
    Devuelve la fecha en formato AAAA-MM-DD, con ceros a la izquierda si es necesario.
    """
    return f"{año}-{mes:02}-{día:02}"

def main():
    fecha_input = input("Ingrese la fecha (ejemplo: 8/9/1636 o Septiembre 8, 1636): ")
    resultado = parsear_fecha(fecha_input)
    if resultado:
        año, mes, día = resultado
        fecha_formateada = formatear_fecha(año, mes, día)
        print(fecha_formateada)
    else:
        print("Fecha inválida o en formato no reconocido.")

if __name__ == "__main__":
    main()
