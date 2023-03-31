from gerar_palpites import ler_arquivo


def tabela_final():

    with open(f'pontuacao.csv', 'r') as arq:
        pontuacao = [linha.strip().split(',') for linha in arq.readlines()]

    usuarios = ler_arquivo('usuarios')

    texto = 'Nome Pontos\n'

    for usuario in usuarios:
        nome_user = usuario[0]

        print(nome_user)

        sum = 0

        for pontos in pontuacao:
            nome, ponto = pontos

            if nome == nome_user:
                sum += int(ponto)

        texto += f'{nome_user} {sum}\n'

    with open('tabela_final.txt', 'w') as tabela_final:
        tabela_final.write(texto)


tabela_final()
