#Faça um código que, dado um número, conte quantos números primos existem até ele (dica: use o laço while e, dentro dele, vá decrementando o número inserido e testando se é primo até chegar a zero).

nro = int(input('Insira o número:'))

count = 0

while(nro>1):
    
    for i in range (2,nro):
        if (nro % i == 0):
            break
    else:
        count = count + 1

    nro = nro - 1


print('Quantidade de números primos que existem até esse número:',count)
