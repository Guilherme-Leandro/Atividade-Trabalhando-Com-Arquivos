try:
    with open('notas.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    aluno_atual = None
    notas_atuais = []

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue

        try:
            nota = float(linha)
            notas_atuais.append(nota)

            if len(notas_atuais) == 3:
                media = sum(notas_atuais) / len(notas_atuais)

                if media >= 7.0:
                    status = "Aprovado"
                    nome_arquivo = 'aprovados.txt'
                elif media >= 5.0:
                    status = "Exame"
                    nome_arquivo = 'exame.txt'
                else:
                    status = "Reprovado"
                    nome_arquivo = 'reprovados.txt'

                with open(nome_arquivo, 'a', encoding='utf-8') as arq_status:
                    arq_status.write(f"Aluno(a): {aluno_atual} | Média: {media:.2f}\n")

                print(f"Aluno(a): {aluno_atual} | Média: {media:.2f}: {status}")

                notas_atuais = []

        except ValueError:
            aluno_atual = linha

except FileNotFoundError:
    print("O arquivo 'notas.txt' não existe, crie o arquivo antes")