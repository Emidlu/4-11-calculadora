
print("1 - Para sumar")
print("2 - Para restar")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Para potenciar")
print("6 - Para raiz")


numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
operacion = int(input("Ingrese la operacion: "))


if operacion == 1:
    print(numero1 + numero2)
if operacion == 2:
    print(numero1 - numero2)


