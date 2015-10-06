#quiz

#Dado intervalo de tiempo en segundos calcular los segundos restantes
#que corresponden para convertise exactamente en minutos.
#Este programa debe funcionar para 5 oportunidades

for x <= 5:
	seg = input ("De segundos a calcular: ")
	min = seg/60
	if min != 0:
		mod = seg%60
		dif = 60-mod
		print("Segundo faltantes del minuto: "+ str(dif))
	
