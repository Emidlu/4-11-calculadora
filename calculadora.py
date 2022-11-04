
print("1 - Para sumar")
print("2 - Para restar")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Para potenciar")
print("6 - Para raiz")


operacion = int(input("Ingrese la operacion: "))


numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))

if operacion == 1:
    print(numero1 + numero2)
if operacion == 2:
    print(numero1 - numero2)

if operacion == 3:
    print("el producto entre {} y {} es {}".format(numero1,numero2,(numero1*numero2)))

if operacion == 5:
    print("la potencia de {} elevado a {} es {}".format(numero1,numero2,(numero1**numero2)))



