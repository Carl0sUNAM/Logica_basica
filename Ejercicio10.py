#Ejercicio10
#Entrada de datos
Acumulador = 0
Contador = 0
#Operaciones
while True:
 número= int(input("Insertar un número entero"))
 if (número >= 0):
  Acumulador = número + Acumulador
  Contador +=1
 elif(Contador == 0 and número < 0):
  # Error
  print("No hay número para dividir")
 else:  
  break 
  #Salida de datos
print ("Tu promedio es de ", Acumulador/ Contador)
