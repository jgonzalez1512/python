print("Cajero")
saldo = 1584.23
billete = 100
montoRetiro = float(input("Digite el monto que desea retirar: "))

if montoRetiro > saldo:
    print("no tiene suficiente fondos")
else:
    if montoRetiro % billete != 0:
        print("El monto solicitado no puede ser dispensado con billetes de 100.")
    else:
        # Calcular la cantidad de billetes a dispensar
        resultado = montoRetiro // billete
        print("Se dispensarán "+ str(resultado) + " billetes de 100.")