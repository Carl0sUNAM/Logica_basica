#Ejercicio5_prueba
# ENTRADA DE DATOS
import math
a= float(input("Insertar valor para el coeficiente de x cuadrado "))
b=float(input("Insertar valor para el coeficiente de x "))
c=float(input("Instertar valor para la constante "))
#Operaciones / Declaraciones 
discriminante = b**2 -(4*a*c)
x1= (-b + math.sqrt(discriminante))/(2*a)
x2= (-b - math.sqrt(discriminante))/(2*a) 
#SALIDA DE DATOS
print("x1 es =",x1)
print( "x2 es =",x2)
