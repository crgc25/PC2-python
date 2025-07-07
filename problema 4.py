def ingresar_alumnos():
    alumnos = [] 
    n = int(input("Ingrese la cantidad de alumnos: "))
    
    for i in range(n):
        print(f"\nIngresando datos del alumno {i+1}:")
        nombre = input("Nombre: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1}: "))
            notas.append(nota)
        alumno = {
            "nombre": nombre,
            "notas": notas
        }
        alumnos.append(alumno)
    return alumnos

def mostrar_alumnos(alumnos):
    print("\nListado de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['nombre']}")
        print(f"Notas: {alumno['notas']}")
        print("-" * 30)

def main():
    alumnos = ingresar_alumnos()
    mostrar_alumnos(alumnos)

if __name__ == "__main__":
    main()
