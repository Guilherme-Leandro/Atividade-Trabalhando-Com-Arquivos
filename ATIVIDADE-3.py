def processar_exame():

    try:
        with open('exame.txt', 'r', encoding='utf-8') as arquivo_exame:
            linhas = arquivo_exame.readlines()

            for linha in linhas:

                linha = linha.strip()

                if not linha:
                    continue

                partes = linha.split(';')
                nome = partes[0].strip()
                media_anterior = float(partes[1].strip())

                print(f"\n Aluno(a): {nome}")
                print(f"Média anterior: {media_anterior}")
                nota_exame = float(input(f"Digite a nota do exame para {nome}: "))

                nova_media = (media_anterior + nota_exame) / 2
                if nova_media >= 5:
                    print(f'Aluno aprovado com média {nova_media}')
                    with open('aprovados.txt', 'a', encoding='utf-8') as arquivo_aprovado:
                        arquivo_aprovado.write('Aluno aprovado')
    except:

    finally:
