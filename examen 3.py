print() #para dejar un espacio al momento de ejecutar 
print("jode daniel arguijo torres")
print() # para dejar un espaco al momento de ejecutar 

# Lista de asignaturas
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Diccionario para almacenar las notas
notas = {}

# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas[asignatura] = nota

# Mostrar las notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
