# UTN-TUPaD-Programacion1

""" 1)  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  """

print("Hola mundo")


""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. """
 

nombre=input("Ingrese su nombre")
print("Hola " + nombre + "!")


""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla.  """

nombre= input("Ingrese su nombre")
apellido= input("Ingrese su apellido")
edad= input("Ingrese su edad")
residencia= input("Ingrese su residencia")

print("Soy" +nombre+ apellido+" tengo " +edad+ " años y vivo " +residencia+ ", hola!" )


""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.  """

from math import pi

radio = float(input("Ingrese radio: "))

Area = pi * radio * radio
Perimetro = 2 * pi * radio

print("El area del circulo sera de: " ,float(Area) , " y el perimetro es de: " , float(Perimetro))


""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale.  """

segundos = float(input("Ingrese los segundos a convertir: "))

conversion = segundos / 3600;

print("La equivalencia en horas de " , segundos, " sera de: ", conversion)


""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.  """ 

num = int(input("Ingrese un numero: "))

num1 = num * 1
num2 = num * 2
num3 = num * 3
num4 = num * 4
num5 = num * 5
num6 = num * 6
num7 = num * 7
num8 = num * 8
num9 = num * 9
num10 = num * 10

print("La tabla de multiplicar del numero ingresado seria la siguiente: ")
print(num, "x 1: ", num1)
print(num, "x 2: ", num2)
print(num, "x 3: ", num3)
print(num, "x 4: ", num4)
print(num, "x 5: ", num5)
print(num, "x 6: ", num6)
print(num, "x 7: ", num7)
print(num, "x 8: ", num8)
print(num, "x 9: ", num9)
print(num, "x 10: ", num10)

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.  """

num1 = int(input("Ingrese el primer numero distinto de cero: "))
num2 = int(input("Ingrese el segundo numero distinto de cero: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

print("La operaciones aritmeticas de los numeros ingresados", num1, " y ", num2, "son las siguientes: ")
print("Suma: ", num1, " + ", num2, ": " ,suma)
print("resta: ", num1, " - ", num2, ": " ,resta)
print("Multiplicacion: ", num1, " x ", num2, ": " ,multi)
print("Division: ", num1, " / ", num2, ": " ,div)


""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
modo:  
𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2 """


alt = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / alt

print("Su IMC es de: ", imc)


"""  9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32 """

celsius = float(input("Ingrese los grados celsius a convertir: "))

fahrenheit  =  9/5 * celsius + 32

print("La temperatura den grados faranheit es de: ", fahrenheit )



"""  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números. """

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3 )/3

print("El promedio de los tres numeros ingresados es: ", promedio)