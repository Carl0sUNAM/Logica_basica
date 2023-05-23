#Ejercicio7
#ENTRADA DE DATOS
agua= float(input("¿Cuál es el nivel de agua?"))
#OPERACIONES
if (agua > 6):
    print("Desbordamiento del agua de la Cisterna")
elif (agua == 6):
     print("Apagar Bomba")
elif(agua > 4  and agua < 6 ):
     print("Desacelerar Bomba")
elif(agua > 2 and agua <= 4 ):
     print("Bomba Trabajando!")
elif(agua > 0 and agua <= 2 ):
    print("Acelerar Bomba de Agua")
elif(agua == 0 ):
     print("Encender Bomba de Agua")
elif(agua < 0):
     print("Fuga en Cisterna")