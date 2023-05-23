#Ejercicio 8
#preguntar por la información 
número = int(input("Esperando a recibir un número: "))
# declarando variables
start = 0
límite_negativo = -100
límite_positivo  = 100
crecimiento_negativo = -1
crecimiento_positivo = 2
if (número == 0 or número  <= límite_negativo or número >= límite_positivo ):
  print("No Válido")
while start > número > límite_negativo:
    #Para números  impares
 if número == crecimiento_negativo :
    print(número)
    número = límite_negativo
 elif número < crecimiento_negativo:
  print(crecimiento_negativo)
  crecimiento_negativo -= 2
 
        
 


while start < número < límite_positivo:
  #Para números pares
   if (número == crecimiento_positivo):
     print(número)
     número = límite_positivo
   elif número > crecimiento_positivo:
     print(crecimiento_positivo)
     crecimiento_positivo +=2 
        