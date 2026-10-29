aluno = input('Digite o nome do aluno:')

lista_notas = []

for i in range(1, 4):
    nota = float(input(f'Digite a {i}ª nota do aluno:'))

    lista_notas.append(nota)

with open('notas.txt', 'a', encoding = 'utf-8') as arquivo:

    notas_em_linhas = '\n'.join(map(str, lista_notas))

    arquivo.write(f'{aluno}\n{notas_em_linhas}\n')