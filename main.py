"""
1 - Crear una función que pase enteros > 0 y <4000 a romano
2 - cualquier otra entrada dar error
3 - límite 3999

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menos de 4000")
c) una cadena -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor que 0")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero y positivo")
f) 

M ---> 1000
D ---> 500
C ---> 100
L ---> 50
X ---> 10
V ---> 5
I ---> 1

"""

VALORES = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}


class RomanNumberError():
    pass

# Ingresar 1994 y retornar MCMXCIV
def entero_a_romano():
    return "MCMXCIV"


def introduce_numero():
    cadena = input("Introduce un número")
    try:
        numero = int(cadena)
        if numero > 0 and numero <4000:
            return numero
        else:
            print("El número debe estar entre 0 y 4000")
    except:
        print("Introduce un número entero")

diccionario = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

unidades = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:'IX'}
decenas = {10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
centenas = {100:"C",200:"CC", 300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
millares ={1000:"M",2000:"MM",3000:"MMM"}


numero = 1989

millares = numero//1000
centenas = numero%1000//100
decenas = numero%1000%100//10
unidades = numero%1000%100%10

if numero < 4000:
    print(f"{numero} es {millares} millares + {centenas} centenas + {decenas} decenas + {unidades} unidades")