#quiz5

class Hola(object):

	mensaje = "Hola mundo"
	__contador = 0

	def ingresar(self,texto):	

		texto = input("Ingrese mensaje")
		self.texto = texto

	def comparar(object):
		if texto == mensaje:
			return(+str"mensaje"+)
		else:
			return("Adios mundo")

	def guardarTexto():
		out_file = open(archivo, "wt")
		out_file.write(mensaje)
		out_file.close()
		
	def mostrarContador():
		print("Contador: " + str(__contador))

	def salir():
		print("Adios!")

	def menuQuiz():
		print("1-Ingresar mensaje")
		print("2-Comparar ")
		print("3-Guardar ")
		print("4-Mostrar contador ")
		print("5-Salir ")
		print()


if __name__ == '__main__':
	mensaje = "Hola mundo"
	__contador = 0	
	opcion_menu = 0
	while True:
		menuQuiz()
		try:
			opcion_menu = int(input("Seleccionar accion 1-5: "))
		except:
			print("Invalido")
		else:
			if opcion_menu == 1:
				ingresar(texto)
			elif opcion_menu == 2:
				comparar(mensaje)
		elif opcion_menu == 3:
			guardarTexto(mensaje, archivo)
		elif opcion_menu == 4:
			motrarContador(__contador)
		elif opcion_menu == 5:
			salir()
			break
		else:
			print("Opcion no valida")
			menuQuiz()
	print("Hasta luego!")
