#ejercicio9
#ENTRADA DE DATOS
#Salario se podría convertir en una entrada del usuario
salario = 250 
Días_de_Mayo = 31
#OPERACIONES
salario_bruto = salario *Días_de_Mayo
iva_transladado = salario_bruto *0.16
subtotal = salario_bruto + iva_transladado
iva_retenido =2/3* iva_transladado
isr_retenido = salario_bruto * 0.1
pago_neto = subtotal - iva_retenido - isr_retenido
#SALIDA DE DATOS
print("Tu salario diario es de ", salario)
print("Días trabajos son de ", Días_de_Mayo)
print("Salario bruto es de ", salario_bruto)
print("Iva transladado es de ",iva_transladado)
print("Subtotal es de ", subtotal)
print("Iva retenido es de ", round(iva_retenido),2)
print("ISR retenido es de " , isr_retenido)
print("Pago neto es de ", round(pago_neto,2))
