print ("CALCULADORA DE PRESTAMO")

montoPrestamo = 1000000
tasaInteresAnual = 16.33

tasaInteresMensual =  tasaInteresAnual / 100 / 12

cuota_mensual = montoPrestamo * (tasaInteresMensual * (1 + tasaInteresMensual) ** 12) / ((1 + tasaInteresMensual) ** 12 - 1)

print("Maria deberea pagar una cuota de $" + str(cuota_mensual))