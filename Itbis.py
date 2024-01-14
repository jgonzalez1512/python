print("CALCULADORA DE ITBIS")
compraSIN = float(input("Digita el monto de la compra sin impuestos"))
itbis = 0.18
descuento = 0.05

TITBIS = itbis * compraSIN
compraDES = compraSIN * descuento
total = compraSIN + TITBIS - compraDES 

print("El ITBIS es de = " + str(TITBIS))
print("EL descuento es de = " + str(compraDES))
print("EL total a pagar es = " + str(total))