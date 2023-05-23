#Ejercicio 4
# ENTRADA DE DATOS
grados_deseados = input("Escribe Celsius, Fahrenheit o Kelvin para poder transfomarlo ")
grados_valor = float(input("Insertar el valor que tiene "))
#OPERACIONES
if grados_deseados == "Kelvin":
    kelvin = grados_valor
    celsius = grados_valor - 273.15
    fahrenheit = celsius*9/5 +32

if grados_deseados == "Celsius":
     kelvin = grados_valor + 273.15
     celsius = grados_valor
     fahrenheit= grados_valor*9/5 + 32

if grados_deseados == "Fahrenheit":
    kelvin = 5*(grados_valor -32)/9 +273.15
    celsius = 5*(grados_valor -32)/9
    fahrenheit = grados_valor

 #SALIDA DE DATOS
print( "En kelvin es ", round( kelvin,2))
print( "En celsius es ", round(celsius,2),"°C")
print( "En fahrenheit es ", round(fahrenheit,2), "°F")
