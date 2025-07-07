

numero = 1989

millares = numero//1000
centenas = numero%1000//100
decenas = numero%1000%100//10
unidades = numero%1000%100%10

if numero < 4000:
    print(f"{numero} es {millares} millares + {centenas} centenas + {decenas} decenas + {unidades} unidades")