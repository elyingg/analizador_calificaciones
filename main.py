print("====================================")
print(" ANALIZADOR DE CALIFICACIONES")
print("====================================")
nombre = input("Nombre del estudiante: ")
cantidad = int(input("Cantidad de calificaciones: "))
calificaciones = []
for i in range(cantidad):
 nota = float(input(f"Ingrese la calificación {i + 1}: "))
 calificaciones.append(nota)
print("\nDatos registrados correctamente.")
print("Estudiante:", nombre)
print("Calificaciones:", calificaciones)
