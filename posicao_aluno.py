#Faça uma lista de 10 alunos, então o usuário deve inserir uma posição e o programa deve dizer qual aluno está naquela posição da lista.

alunos = ['Ana', 'Bianca', 'Carlos', 'Diego', 'Estefani', 'Francisco', 'Gabriela', 'Heitor', 'Isabela', 'Joana']

pos = int(input('Insira uma posição:'))

print(f'A pessoa na posição {pos} é:', alunos[pos-1])