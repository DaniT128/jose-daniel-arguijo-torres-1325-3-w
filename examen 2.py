print() #para dejar un espacio al moemnto de ejcuatr 
print("jose daniel arguijo torres")
print() #para dejar un espacioal momento de ejecutar 

# Diccionario con los créditos de las asignaturas
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Variable para almacenar el total de créditos
total_creditos = 0

# Mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos

# Mostrar el total de créditos del curso
print(f"El número total de créditos del curso es {total_creditos}")

