#Reutilizo parte del codigo de la calculadora para crear este convertidor

def Menu():

	print("Convertidor de unidades de distancia")
	print """
----------------------

Ingrese 1 para milimetros
Ingrese 2 para centimetros
Ingrese 3 para metros
Ingrese 4 para kilometros

----------------------"""

def Calculadora():

	Menu()
	opt = int(input("Seleccione opcion\n"))
	
	if(opt == 1):
		x=float(input("Ingrese los milimetros a convertir: \n"))
		print "Usted tiene: ", x, "Milimetros", x/10, "Centimetros ", x/1000, "Metros", x/1000000, "Kilometros"
	
	elif(opt == 2):
		x=float(input("Ingrese los centimetros a convertir: \n"))
		print "Usted tiene: ", x*10, "Milimetros", x, "Centimetros ", x/100, "Metros", x/100000, "Kilometros"
	
	elif(opt == 3):
		x=float(input("Ingrese los metros a convertir: \n"))
		print "Usted tiene: ", x*1000, "Milimetros", x*100, "Centimetros ", x, "Metros", x/1000, "Kilometros"
	
	elif(opt == 4):
		x=float(input("Ingrese los kilometros a convertir: \n"))
		print "Usted tiene: ", x*1000000, "Milimetros", x*100000, "Centimetros ", x*1000, "Metros", x, "Kilometros"

Calculadora()