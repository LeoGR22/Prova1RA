valor1 = float(input("Digite um valor"))
valor2 = float(input("Digite outro valor"))
valor3 = float(input("Digite outro valor"))
maior = 0

if valor1 > valor2:
    maior = valor1
elif valor2 > valor1:
    maior = valor2

if valor1 > valor3:
    maior = valor1
elif valor3 > valor1:
    maior = valor3

print(maior)