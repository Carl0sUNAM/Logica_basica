#Solicitar edad de la persona
#ENTRADA DE DATOS
import datetime
año_de_nacimiento= int(input("Ingresar la fecha de nacimiento "))
año_actual = datetime.datetime.now().year
#SALIDA DE DATOS
print("Tu edad es", año_actual-año_de_nacimiento, "años")
