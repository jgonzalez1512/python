print("Calculadora de impuestos")

salarioMensual = float(55000) 
salarioanual = salarioMensual * 12

excedente = salarioanual - 624329.01
tasa = 31216.00 
rentaAnual = tasa + excedente * 0.20 
rentamensual = rentaAnual / 12

print("A Luis se le descontara mensualmente: $" +str(rentamensual))
