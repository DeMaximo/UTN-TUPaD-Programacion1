# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 


# notas=[5.3 , 6.7 , 8.6 , 9 , 4 , 4.5 , 7 , 8.5 , 6]
# mayor_nota=-100
# menor_nota=100
# suma=0
# largo = len(notas)

# for i in range(0, largo):
#     print(notas[i])
#     suma=suma + notas[i]
#     if notas[i] > mayor_nota:
#         mayor_nota = notas[i]
#     elif notas[i] < menor_nota:
#         menor_nota = notas[i]

# print(f"La mejor nota es: {mayor_nota} y la nota mas baja es : {menor_nota}\n" ) 
# print(f"el promedio de la lista es {suma/largo}")

# ////////////////////////////////////////////////////////////////////////////////////////

# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

# list = []
# productos=input("Ingrese 5 productos a la lista: ")
# list.append(productos)
# largo=len(list)

# while largo < 5:
#     productos=input("Ingrese los productos restantes a la lista: ")
#     list.append(productos)
#     largo=len(list)

# print(f"La lista ordenada seria {sorted(list)}")

# descicion=int(input("Que desea hacer con la lista restante: \n 1 - Borrar\n 2 - Actualizar:"))
# if descicion == 1:
#     list.clear()
#     print("Lista borrada!")
# elif descicion == 2:

#     print(f" {sorted(list)} \n")


#     opcion=int(input("de la lista ordenada elija la posicion del producto que desea actualizar (recordando que empieza de 0 [cero]): "))
#     if opcion <= largo:    
#         for i in range (largo):
#              cambio = input("Ingrese el producto nuevo: ")
#              list[i]=cambio
#     elif opcion > largo or opcion < 0:
#         print("Opcion incorrecta")

# print(f"la lista actualizada es la siguiente {sorted(list)}")

# ////////////////////////////////////////////////////////////////////////////////////////

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.

# import random
# num = []
# par = []
# impar = []
# num=random.sample(range(1,100), 15)

# print(f"{num}")



# for i in num:
#     if i % 2 == 0:
#         par.append(i)
#     else:
#         impar.append(i)

# num_par = len(par)
# num_impar = len(impar)

# print(f"Hay {num_par} numeros par y {num_impar} numeros impares.")

# ////////////////////////////////////////////////////////////////////////////////////////

# 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# largo = len(datos)
# i = 0

# while i < len(datos):
#     j = i + 1
#     while j < len(datos):
#         if datos[i] == datos[j]:
#             datos.pop(j)  
#         else:
#             j += 1
#     i += 1

# print(datos)

# ////////////////////////////////////////////////////////////////////////////////////////

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

# lista = ["Ana", "laura", "Fernando", "Matias", "Miguel", "Cecilia", "Thiago", "Angel"]

# opcion = int(input("Ingrese una opcion:\n 1 - Agregar un alumno a lista\n 2 - Elimine un alumno de la lista"))
# if opcion == 1:
#     lista.append(str(input("Ingrese un nuevo alumno")))
# elif opcion ==2:
#     print(f"{lista}")

#     lista.remove(str(input("Ingrese el nombre del alumno que desea borrar:")))
# print(f"{lista}")

# ////////////////////////////////////////////////////////////////////////////////////////

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero). 

# lista = [10, 20, 30, 40, 50, 60, 70]

# # Rotar una posición a la derecha
# lista = [lista[-1]] + lista[:-1]

# print(lista)

# ////////////////////////////////////////////////////////////////////////////////////////

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

# clima = [[13, 26], [10, 24], [15, 29], [9, 22], [17, 28], [10, 26], [11, 30]]
# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# suma_min = 0
# suma_max = 0
# mayor_amplitud = 0
# dia_mayor_amplitud = ""

# for i in range(len(clima)):
#     temp_min = clima[i][0]
#     temp_max = clima[i][1]
#     amplitud = temp_max - temp_min

#     suma_min += temp_min
#     suma_max += temp_max

#     if amplitud > mayor_amplitud:
#         mayor_amplitud = amplitud
#         dia_mayor_amplitud = dias[i]

# promedio_min = suma_min / len(clima)
# promedio_max = suma_max / len(clima)

# print(f"El promedio de las mínimas es {promedio_min:.2f}°C")
# print(f"El promedio de las máximas es {promedio_max:.2f}°C")
# print(f"El día con mayor amplitud térmica fue {dia_mayor_amplitud} con {mayor_amplitud}°C de diferencia")

# ////////////////////////////////////////////////////////////////////////////////////////

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

# notas = [
#     [7, 8, 9],
#     [6, 5, 7],   
#     [9, 9, 10],  
#     [4, 6, 5],  
#     [8, 7, 6]   
# ]

# materias = ["Matemática", "ingles", "sociales"]
# estudiantes = ["Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4", "Estudiante 5"]

# # Promedio por estudiante
# print("Promedio de cada estudiante:")
# for i in range(len(notas)):
#     suma = sum(notas[i])
#     promedio = suma / len(notas[i])
#     print(f"{estudiantes[i]}: {promedio:.2f}")

# print("\nPromedio de cada materia:")
# # Promedio por materia
# for j in range(len(materias)):
#     suma = 0
#     for i in range(len(notas)):
#         suma += notas[i][j]
#     promedio = suma / len(notas)
#     print(f"{materias[j]}: {promedio:.2f}")

# ////////////////////////////////////////////////////////////////////////////////////////


        



