print()
print("jose daniel arguijo torres")
print()

# Lista de asignaturas 
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas
notas = {}

# Preguntar al usuario por las notas
for asignatura in asignaturas:
    try:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas[asignatura] = nota
    except ValueError:
        print("Por favor, ingrese un número válido.")
        notas[asignatura] = None  # Asignar None en caso de error

# Eliminar asignaturas aprobadas
asignaturas_repetir = [asignatura for asignatura, nota in notas.items() if nota is None or nota < 6]

# Mostrar las asignaturas que el usuario tiene que repetir
if asignaturas_repetir:
    print("Asignaturas que tienes que repetir:")
    for asignatura in asignaturas_repetir:
        print(f"- {asignatura}")
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
