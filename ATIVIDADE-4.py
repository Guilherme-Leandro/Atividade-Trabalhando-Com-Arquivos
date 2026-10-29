def exibir_situacao_alunos():

    arquivos_status = {
        'aprovados.txt': 'Aprovado',
        'reprovados.txt': 'Reprovado'
    }

    for nome_arquivo, situacao in arquivos_status.items():
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()

                for linha in linhas:
                    linha = linha.strip()
                    if linha:

                        print(f"{linha} | Situação: {situacao}")

        except FileNotFoundError:
            print(f"Aviso: O arquivo '{nome_arquivo}' ainda não foi criado ou não foi encontrado.")


if __name__ == "__main__":
    exibir_situacao_alunos()