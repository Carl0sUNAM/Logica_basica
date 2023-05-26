#Ejercicio 12
#Para desarrollar objetos
class Estado_Mex:
    def __init__(Estado,población, extensión_territorial):
        Estado.población = población
        Estado.extensión_territorial = extensión_territorial
        Estado.densidad_de_población = Estado.población/extensión_territorial
    def navegación(Densidad_de_población):
        return Densidad_de_población

    

        
# Variables 
#Diccionario
Edomex = Estado_Mex(16992418, 22351.8)
Oaxaca = Estado_Mex(4132148, 93757.6)
Chihuahua= Estado_Mex(3741869, 247412.6)
Veracruz = Estado_Mex(8062579, 71823.5)
Baja_California_Norte = Estado_Mex( 3769020,71450.0)
print(Edomex.densidad_de_población)
 #Areglo
México = [Edomex, Oaxaca, Chihuahua, Veracruz, Baja_California_Norte]
# Este es el correcto, perdón
Estados_de_México = [
    {
        'nombre': 'Estados de México',
        'poblacion': 16992418,
        'extension': 22351
    },
    {
        'nombre': 'Oaxaca',
        'poblacion': 4132148,
        'extension': 93757
    },
    {
        'nombre': 'Veracruz',
        'poblacion': 8062579,
        'extension': 71823
    },
    {
        'nombre': 'Chihuahua',
        'poblacion': 3741869,
        'extension': 247412
    },
    {
        'nombre': 'Baja_California_Norte',
        'poblacion': 3769020,
        'extension': 71450
    }
]

