#Desarrolle un programa que guarde, en un archivo de texto, las diferentes calificaciones de los 5 quizzes realizados por 3 estudiantes. cada estudiante tendra su propio archivo de texto 
#cuyo nombre de archivo sera igual al nombre del estudiante. ademas debe mostrar en pantalla, el valor promedio de las calificaciones de cada estudiante.
estudiante = 0
while estudiante <= 3
	estudiante += 1
	nombre =	input("nombre: ")
	quiz1 =	input(int("quiz1: "))
	quiz2 =	input(int("quiz2: "))
	quiz3 =	input(int("quiz3: "))
	quiz4 =	input(int("quiz4: "))	
	quiz5 =	input(int("quiz5: "))
		prom=quiz1+quiz2+quiz3+quiz4+quiz5
		prom=prom/5
	guardarNombre(nombre)
	archivo = open(nombre, "w")
	archivo.write(nombre + ":" + str(quiz1) + "+" + str(quiz2) + "+" + str(quiz3) + "+" + str(quiz4) + "+" + str(quiz5) + "\n Promedio: " + str(prom) + "\n")
	archivo.close	
	
	def verProm
		if x == si:
			print("Promedio: " + str(prom))
		else 
			break
if __nombre__ == '__main__':
	seleccion = {}
	x = 0
	while True
		verProm()
		try:
			x = int(input("Deseas ver tu promedio? Responda si o no")
		except:
			print("Hasta luego.")
		

	
