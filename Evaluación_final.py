#ENTRADA DE DATOS
pregunta1= "1. Herramienta de programación, parecido al lenguaje español utilizado para crear código."
#IDE
opciones1= "a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO"

pregunta2= "2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados"
#Imformacion
opciones2=  "a) Información     b) Datos     c) Programa     d) Código"

pregunta3= "3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo."
# ANSI/ISO
opciones3= "     a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode"

pregunta4= "4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema."
#algoritmo
opciones4= "     a) Proceso     b) Solución     c) Función     d) Algoritmo"

pregunta5= "5. Conjunto de elementos que se relacionan para cumplir una función determinada."
#Sistema 
opciones5= "     a) Estructura     b) Datos     c) Operación     d) Sistema"

pregunta6 = "6. Componente de un IDE que se encarga de traducir el código fuente a código máquina."
#comiplador
opciones6= "     a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete"
pregunta7= "7. Elemento que se usa para almacenar una cantidad donde cambia su valor."
#Variable
opciones7= "     a) Constante     b) Variable     c) Librería     d) Tipo de Dato"
pregunta8 = "8. Conjunto de símbolos, letras, números que no tienen un significado."
#Información
opciones8= "     a) Datos     b) Estructura     c) Información     d) Sistema"
pregunta9= "9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento."
#Lógica
opciones9= "     a) Filosofía     b) Sociología     c) Lógica     d) Argumentación"
pregunta10= "10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto."
#estandar
opciones10= "     a) Evento     b) Estándar     c) Calidad     d) Productividad"
pregunta11= "11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico."
#Sistema
opciones11= "     a) Estructura     b) Sistema     c) Objeto     d) Virtual"
pregunta12= "12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar."
#Programa de Computadora
opciones12= "     a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando"
opciones= [opciones1, opciones2, opciones3, opciones4, opciones5, opciones6, opciones7,opciones8, opciones9, opciones10,opciones11, opciones12]
preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10, pregunta11, pregunta12]
respuestas_correctas = ['a', 'a', 'c', 'd', 'd', 'd', 'b', 'c', 'c', 'b', 'b', 'c']
respuestas_usuario = []
resultados = 0
for i, pregunta in enumerate(preguntas):

    respuesta_usuario = input(f" {pregunta} \n {opciones[i]} \n ")
    respuestas_usuario.append(respuesta_usuario)
    respuesta_correcta = respuestas_correctas[i]
    opcion_correcta = opciones[i][0]

    if respuestas_usuario[i] == respuestas_correctas[i]:
       resultados +=1
#Salida de datos
# Mostrar resultados al final
promedio = resultados/12 *100
print(resultados)
print(f"{round(promedio,2)}%")
if (promedio >50):
 print("Aprobado")
else:
 print("Reprobado")