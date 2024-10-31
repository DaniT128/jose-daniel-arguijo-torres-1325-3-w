print() #para dejar un espacio al momento de ejecutar 
print("jose daniel arguijo torres")
print() #para dejar un espacio al momento de ejcutar 

usuario = {} #indica los usuarios 

usuario['nombre'] = input("¿Cuál es tu nombre? ") #indica tu nombre 
usuario['edad'] = input("¿Cuál es tu edad? ") #indica tu edad 
usuario['dirección'] = input("¿Cuál es tu dirección? ") #indica tu direccion 
usuario['teléfono'] = input("¿Cuál es tu número de teléfono? ") #indica tu numero de telefono 

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['dirección']} y su número de teléfono es {usuario['teléfono']}.")
#muestra los datos del usuario seleccionados 