#resolver eq de seg grau

from math import sqrt #para fazer a raiz

a = float(input("insira o a: "))
b = float(input("insira o b: "))
c = float(input("insira o c: "))

delta = (b**2) - (4*a*c)

if delta<0 or a==0:
	print("nao existe solucao real")

else:
	x1 =  ((- b + (sqrt(delta))) / (a*2))
	print(x1)
	
	#se o delta for 0, x1 e x2 sao iguais
	if delta>0:
		x2 =  ((- b - (sqrt(delta))) / (a*2))
		print(x2)
	
