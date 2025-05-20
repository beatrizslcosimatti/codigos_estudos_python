#Faça um dicionário associando 20 alunos e suas notas na P1 de cálculo 1 (valores e nomes imaginários), então quando o usuário inserir um nome, o código deve dizer a nota do aluno.

al_notas = dict()
al_notas = {'Ana':'8,1', 'Bianca':'7,2', 'Carlos':'4,5', 'Diego':'7,6', 'Estefani':'6,7', 'Francisco':'3,8', 'Gabriela':'7,9', 'Heitor':'2,5', 'Isabela':'8,4', 'Joana':'6,4','Kleber':'4,8', 'Lorena':'9,0', 'Marcos':'6,2', 'Nicolas':'7,3', 'Olivia':'9,5', 'Pedro':'5,5' , 'Quesia':'7,7', 'Ricardo':'5,3' , 'Samanta':'8,8', 'Thiago':'1,5'}



print('Alunos que realizaram a prova de Calculo 1:')
for aluno in al_notas.keys():
    print(aluno)

nome = input('Digite o nome de um dos alunos acima para descobrir sua nota: ')

print(f'A nota de {nome} foi:',al_notas[nome])
