def Menu():

	print("Bienvenido a la calculadora")
	print """
----------------------

Ingrese 1 para sumar
Ingrese 2 para restar
Ingrese 3 para multiplicar
Ingrese 4 para dividir

----------------------"""

def Calculadora():

	Menu()
	opt = int(input("Seleccione opcion\n"))
	if(opt >0 and opt <5):
		x=int(input("Ingrese numero\n"))
		y=int(input("Ingrese otro numero\n"))
		if (opt==1):
			print "La suma es:", x+y
		elif(opt==2):
			print "La resta es:", x-y
		elif(opt==3):	
			print "La multiplicacion es:", x*y
		elif(opt==4):
			try:
				print "La division es:", x/y
			except ZeroDivisionError:
				print "No se puede dividir entre 0"
Calculadora()