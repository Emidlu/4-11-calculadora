

print("1 - Para sumar")
print("2 - Para restar")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Para potenciar")
print("6 - Para raiz")



numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
operacion = int(input("Ingrese la operacion: "))


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



