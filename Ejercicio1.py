#las califiaciones
#ENTRADA DE DATOS
#Declaración de variables
califación_1= float(input("Escribe la primera califiación "))
califación_2= float(input("Escribe la segunda califiación "))
califación_3= float(input("Escribe la tercera califiación "))
#PROCESOS  (Cálculos u operaciones matemáticas y/o lógicas)
#Sacar promedio
promedio= (califación_1 +califación_2 + califación_3) /3
#Uso de condicionales / SALIDA DE DATOS
if califación_1 >= 6 and califación_1 <=10 :
    print("Aprobado el primer examen")

elif(califación_1 >= 0 and califación_1 <=10):
    print("Reprobado el primer examen")
else:
    print("No válido")
if (califación_2 >= 6 and califación_2 <=10):
    print("Aprobado el segundo examen")   
elif(califación_2 >= 0 and califación_2 <= 10):
    print("Reprobado el segundo examen")
else:
    print("No válido")
if (califación_3 >=6 and califación_3 <=10):
   print("Aprobado el tercer examen")
elif(califación_3 >= 0 and califación_3 <=10): print("Reprobado el tercer examen")
else: 
    print("No válido")
# RESULTADO DEL PROMEDIO 

if (promedio >= 6 and promedio <= 10): 
    print("El promedio fue aprobatorio")
elif (promedio >=0 and promedio <= 10): 
    print("El promedio fue reprobatorio")
else: 
 print("No válido alguna de las calificaciones")
# Resultados de la califación
print("El promedio es =", round(promedio,2))
