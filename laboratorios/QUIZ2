#Laboratorio

#El Emperador está celebrando aniversario y ofrecerá a sus clientes una serie de ofertas que se traducirán en un incremento de sus ventas.
#Las reglas de las ofertas se basan en un porcentaje de descuente sobre el total de la compra, que estarían variando dependiendo del monto adquirido.
#Por un monto mayor o igual a 500, descuento del 30%
#Por un monto menor de 500 pero mayor o igual a 200, descuento del 20%
#Por un monto menor de 200 pero mayor o igual a 100 descuento del 10%
#Elabore este programa considerando 5 usuarios por ejecucion.

usuarios = 1
while usuarios <=5:
	monto = int(input("Monto: "))
	
	if monto >= 500:
		desc = monto*0.30
		mt = monto - desc
		print("El total a pagar del monto" + str(monto) +", con descuento de 30%, seria de" + str(mt))
	
		if monto < 500 and monto >= 200:
			desc = monto*0.2
			mt = monto - desc
			print("El total a pagar del monto" + str(monto) +", con descuento de 20%, seria de" + str(mt))
	
			if monto < 200 and monto >= 100:
				desc = monto*0.1
				mt = monto - desc
				print("El total a pagar del monto" + str(monto) +", con descuento de 10%, seria de" + str(mt))
	
	else:
		print("Su monto a pagar es " + str(monto))
		
	usuarios = usuarios +1
	
	
print("Gracias por su compra")
