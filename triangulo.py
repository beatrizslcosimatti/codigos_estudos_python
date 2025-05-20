# Faça um código que, dado o valores dos 3 lados de um triângulo, diga se ele é equilátero, isósceles ou escaleno (Para isso, utiliza as estruturas condicionais if, elif e else)

print('Digite os 3 lados do triângulo:')
lado1 = input('Lado 1:')
lado2 = input('Lado 2:')
lado3 = input('Lado 3:')

if (lado1 == lado2 == lado3): 
    print("o triângulo é equilátero")

elif (lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2):
    print('o triângulo é isósceles')

else:
    print('o triângulo é escaleno')