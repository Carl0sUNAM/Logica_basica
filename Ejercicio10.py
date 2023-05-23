#Ejercicio10
lista_de_números= []
def ciclo( ):
 número= int(input("Insertar un número entero"))
 if (número >= 0):
  lista_de_números.append(número)

  return ciclo() 
 else: 
  promedio = sum(lista_de_números) / len(lista_de_números)
  return print(promedio)
ciclo()