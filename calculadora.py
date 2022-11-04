
print("1 - Para sumar")
print("2 - Para restar")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Para potenciar")
print("6 - Para raiz")


numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
operacion = int(input("Ingrese la operacion: "))

def dividir(num,div):
  return num/div

if operacion == 1:
    print(numero1 + numero2)
if operacion == 2:
    print(numero1 - numero2)

if operacion == 3:
    print("el producto entre {} y {} es {}".format(numero1,numero2,(numero1*numero2)))
if operacion == 4:
    try:
        print (dividir(numero1,numero2))
    except ZeroDivisionError:
        print("Trataste de dividir entre cero ")
if operacion == 5:
    print("la potencia de {} elevado a {} es {}".format(numero1,numero2,(numero1**numero2)))
if (operacion==6):
        try :
            if numero1>0:
                print("La raiz cuadrada de",numero1," es: ",numero1**(0.5))
            else:
                raise ValueError()
    
        except ValueError:
            print("el primer numero es negativo")

        try :
                    
            if numero2>0:
                print("La raiz cuadrada de",numero2," es: ",numero2**(0.5))
            else:
                raise ValueError()    


        except ValueError:
            print("el segundo numero es negativo")



