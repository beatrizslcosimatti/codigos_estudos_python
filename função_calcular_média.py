#Crie uma função chamada “calcular média” que receba três notas (valores do tipo float) como parâmetros e retorne a média aritmética dessas notas.

a2 = float(input('a:'))
b2 = float(input('b:'))
c2 = float(input('c:'))


def calcular_media(a, b, c):
    return (a + b + c)/3
resultado = calcular_media(a2, b2, c2)
print(resultado)